import os
import shutil
import sass
from flask_frozen import Freezer
from app import app

# Configure Freezer
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_REMOVE_EXTRA_FILES'] = True 

freezer = Freezer(app)

# --- Fix 1: Explicitly tell Freezer to generate the 404 page ---
@freezer.register_generator
def error_handlers():
    # Yield the URL for the 404 page so Freezer knows to visit it
    yield '/404.html'

def compile_scss():
    """Compile SCSS to CSS with error handling and validation"""
    print("Compiling SCSS...")
    scss_file = os.path.join('static', 'styles.scss')
    css_file = os.path.join('static', 'style.css')  
    
    if not os.path.exists(scss_file):
        print(f"Error: Source file not found: {scss_file}")
        return False
    
    try:
        compiled_css = sass.compile(
            filename=scss_file, 
            output_style='compressed',
            precision=5
        )
        
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(compiled_css)
        
        # Verify output
        if os.path.exists(css_file):
            print(f"SCSS compiled successfully: {css_file}")
            return True
        else:
            print("Error: CSS file could not be written")
            return False
            
    except sass.CompileError as e:
        # --- Fix 2: Print specific SCSS syntax errors ---
        print(f"SCSS Compilation Error:\n{e}")
        return False
    except Exception as e:
        print(f"SCSS Unknown Error: {e}")
        return False

def clean_build_dir():
    """Clean build directory before freezing"""
    build_dir = app.config['FREEZER_DESTINATION']
    if os.path.exists(build_dir):
        print("Cleaning build directory...")
        shutil.rmtree(build_dir)

def verify_build():
    """Verify the build output"""
    print("Verifying build output...")
    build_dir = app.config['FREEZER_DESTINATION']
    
    if not os.path.exists(build_dir):
        print("Error: Build directory does not exist")
        return False
    
    # Check for essential files
    essential_files = ['index.html', 'work.html', '404.html']
    missing_files = []
    
    for file in essential_files:
        target = os.path.join(build_dir, file)
        if not os.path.exists(target):
            missing_files.append(file)
    
    if missing_files:
        print(f"Error: Missing essential files: {missing_files}")
        if '404.html' in missing_files:
            print("Hint: Missing 404.html usually means no links point to it. Ensure @freezer.register_generator is used.")
        return False
    
    print("Verification passed! Build complete.")
    return True

if __name__ == '__main__':
    # Step 1: Compile SCSS
    if not compile_scss():
        print("Build failed due to SCSS errors")
        exit(1)
    
    # Step 2: Clean build directory
    clean_build_dir()
    
    # Step 3: Freeze the site
    print("Freezing site...")
    try:
        freezer.freeze()
    except Exception as e:
        # --- Fix 3: Print Flask/Freezer runtime errors ---
        print(f"Critical error during freezing:\n{e}")
        exit(1)
    
    # Step 4: Verify build
    if not verify_build():
        print("Build verification failed")
        exit(1)
