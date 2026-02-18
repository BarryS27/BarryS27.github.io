import requests
import os

DOC_ID = "14wCOJB7mNQwr5xaw5sdh6pRgbPUSFQQgsN4VWesXpRI"
OUTPUT_PATH = os.path.join("static", "resume.pdf") 

def sync_resume():
    url = f"https://docs.google.com/document/d/{DOC_ID}/export?format=pdf"
    print(f"🚀 Attempting to sync Google Doc resume to {OUTPUT_PATH}...")
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            with open(OUTPUT_PATH, "wb") as f:
                f.write(response.content)
            print("✅ Resume synced successfully!")
        else:
            print(f"❌ Download failed. Status Code: {response.status_code}")
    except Exception as e:
        print(f"💥 Exception occurred during sync: {e}")

if __name__ == "__main__":
    sync_resume()