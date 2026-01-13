import os
import shutil
import sass
from flask_frozen import Freezer
from app import app

def compile_scss():
    """Compile SCSS to CSS with error handling and validation"""
    scss_file = os.path.join('static', 'styles.scss')
    css_file = os.path.join('static', 'style.css')  
    
    if not os.path.exists(scss_file):
        return False
    
    try:
        # Compile with compression for production
        compiled_css = sass.compile(
            filename=scss_file, 
            output_style='compressed',
            precision=5
        )
        
        # Write to file with UTF-8 encoding
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(compiled_css)
        
        # Verify output
        file_size = os.path.getsize(css_file) / 1024
        return True
        
    except sass.CompileError as e:
        return False
    except Exception as e:
        return False

def clean_build_dir():
    """Clean build directory before freezing"""
    build_dir = app.config['FREEZER_DESTINATION']
    
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

def verify_build():
    """Verify the build output"""
    build_dir = app.config['FREEZER_DESTINATION']
    
    if not os.path.exists(build_dir):
        return False
    
    # Check for essential files
    essential_files = ['index.html', 'work.html', '404.html']
    missing_files = []
    
    for file in essential_files:
        if not os.path.exists(os.path.join(build_dir, file)):
            missing_files.append(file)
    
    if missing_files:
        return False
    
    return True

# Configure Freezer
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_REMOVE_EXTRA_FILES'] = True  # Clean old files

freezer = Freezer(app)

if __name__ == '__main__':
    # Step 1: Compile SCSS
    if not compile_scss():
        exit(1)
    
    # Step 2: Clean build directory
    clean_build_dir()
    
    # Step 3: Freeze the site
    try:
        freezer.freeze()
    except Exception as e:
        exit(1)
    
    # Step 4: Verify build
    if not verify_build():
        exit(1)