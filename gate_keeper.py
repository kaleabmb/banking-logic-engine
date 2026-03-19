import os
from datetime import datetime

# Hardcoded list of allowed users
authorized_ids = ["admin_01", "system_user", "engineer_v4"]

def log_breach(attempted_id):
    # Open the text file in append mode
    with open("security_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] UNAUTHORIZED ATTEMPT: ID '{attempted_id}'\n")

while True:
    print("\n--- Standard Security Checkpoint ---")
    user_id = input("Enter User ID (or type 'exit' to close): ")
    
    if user_id.lower() == 'exit':
        print("Shutting down gate checkpoint.")
        break
        
    access_key = input("Enter Access Key: ")
    
    # Validation Logic
    is_authorized = user_id in authorized_ids
    is_valid_key = len(access_key) == 8
    
    if is_authorized and is_valid_key:
        print("ACCESS GRANTED. Welcome, " + user_id)
    else:
        print("ACCESS DENIED. This incident will be reported.")
        log_breach(user_id)