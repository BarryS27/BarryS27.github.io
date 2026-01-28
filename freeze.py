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

def compile_scss():
    """Compile SCSS to CSS with proper directory handling"""
    print("Compiling SCSS...")
    
    # Define paths based on your structure
    scss_file = os.path.join('static', 'css', 'styles.scss')
    css_out_dir = os.path.join('static', 'css')
    css_file = os.path.join(css_out_dir, 'styles.css')
    
    # Check if source exists
    if not os.path.exists(scss_file):
        print(f"Error: Source file not found: {scss_file}")
        return False
    
    # Create static/css directory if it doesn't exist
    os.makedirs(css_out_dir, exist_ok=True)
    
    try:
        compiled_css = sass.compile(
            filename=scss_file, 
            output_style='compressed',
            precision=5
        )
        
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(compiled_css)
        
        print(f"✅ SCSS compiled successfully: {css_file}")
        return True
            
    except sass.CompileError as e:
        print(f"❌ SCSS Compilation Error:\n{e}")
        return False
    except Exception as e:
        print(f"❌ SCSS Unknown Error: {e}")
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
        print("❌ Error: Build directory does not exist")
        return False
    
    # Only verify files that strictly exist in your project
    essential_files = [
        'index.html',
        os.path.join('static', 'css', 'styles.css') # Verify CSS was built and copied
    ]
    
    missing_files = []
    
    for file_path in essential_files:
        target = os.path.join(build_dir, file_path)
        if not os.path.exists(target):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Error: Missing essential files in build: {missing_files}")
        return False
    
    print("✅ Verification passed! Build complete.")
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
        print(f"❌ Critical error during freezing:\n{e}")
        exit(1)
    
    # Step 4: Verify build
    if not verify_build():
        print("Build verification failed")
        exit(1)# Final success message
