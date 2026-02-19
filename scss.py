import requests
import os

FILES = ['_core.scss']
BASE_URL = "https://raw.githubusercontent.com/BarryS27/Common-Elements/main/scss/"
TARGET_DIR = "static/css/common/scss"

def fetch():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
    
    for file in FILES:
        print(f"Fetching {file}...")
        r = requests.get(BASE_URL + file)
        with open(os.path.join(TARGET_DIR, file), 'wb') as f:
            f.write(r.content)
    print("✅ All styles synced. No Git bloat.")

if __name__ == "__main__":
    fetch()