import csv
from handlers import GoogleWorkspace

# Configuration
key_file_path = "key.json"
admin_email = "ej@nextresearch.io"
api_scopes = ["https://www.googleapis.com/auth/admin.directory.user"]
customer_id = "C04189rtm"

# Initialize Google Workspace Client
google_client = GoogleWorkspace(
    key_file_path=key_file_path,
    admin_email=admin_email,
    api_scopes=api_scopes,
    customer_id=customer_id,
)

# Authenticate and Fetch Existing Users
access_token = google_client.auth()
existing_users = google_client.list_users()


# Load users from CSV file
csv_file = "users.csv"
users_list = []

with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        primary_email = row["primary_email"]

        # Check if the user already exists
        print(f"Checking  if user with email {primary_email} exists..")
        if primary_email in existing_users:
            print(f"User {primary_email} already exists. Skipping creation.")
            continue  # Skip existing users

        # Prepare user data for creation
        user_data = {
            "name": {
                "givenName": row["first name"],
                "familyName": row["last name"],
            },
            "password": row["password"],
            "primaryEmail": primary_email,
        }
        users_list.append(user_data)

# Create only new users
if users_list:
    create_response = google_client.create_users(users_list)
    print(create_response)
else:
    print("No new users to create.")
