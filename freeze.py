import os
import sass
from flask_frozen import Freezer
from app import app

def compile_scss():
    scss_file = os.path.join('static', 'styles.scss')
    css_file = os.path.join('static', 'styles.css')  
    
    if os.path.exists(scss_file):
        print(f"🎨 Compiling SCSS: {scss_file} -> {css_file} ...")
        
        try:
            compiled_css = sass.compile(filename=scss_file, output_style='compressed')
            
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(compiled_css)
            print("✅ SCSS compiled successfully!")
            
        except Exception as e:
            print(f"❌ Error compiling SCSS: {e}")
            exit(1)
            
    else:
        print(f"⚠️ Warning: Source file {scss_file} not found. Skipping compilation.")

app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    compile_scss()
    
    print("❄️  Freezing static site...")
    freezer.freeze()
    print("🚀 Site built successfully!")
