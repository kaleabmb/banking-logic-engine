import hashlib
import json
import logging
import os
import re

# Setup professional logging
logging.basicConfig(
    filename="auth.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_FILE = "users.json"

def hash_pw(password):
    # Convert string to bytes, hash it, and return the hex string
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    # If no db exists, create one with a default admin
    # The password is 'Admin123!' but we only store the hash
    if not os.path.exists(DB_FILE):
        default_data = {
            "admin": hash_pw("Admin123!")
        }
        with open(DB_FILE, "w") as f:
            json.dump(default_data, f)

def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def is_complex(pw):
    # Must be 8+ chars, have a letter, and have a number
    if len(pw) < 8: return False
    if not re.search(r"[A-Za-z]", pw): return False
    if not re.search(r"[0-9]", pw): return False
    return True

def main():
    init_db()
    db = load_db()

    while True:
        print("\n--- System Login ---")
        uid = input("User (or 'exit'): ").strip()
        
        if uid.lower() == 'exit':
            break
            
        pwd = input("Pass: ").strip()

        # Check if user exists first to prevent errors
        if uid not in db:
            logging.warning(f"Failed login: Unknown user '{uid}'")
            print("Access Denied.")
            continue

        # Check password against hash
        if db[uid] == hash_pw(pwd):
            logging.info(f"Successful login for '{uid}'")
            print(f"Welcome, {uid}.")
        else:
            logging.warning(f"Failed login: Bad password for '{uid}'")
            print("Access Denied.")

if __name__ == "__main__":
    main()