import csv
from handlers import GoogleWorkspace

key_file_path = "key.json"
admin_email = "ej@nextresearch.io"
api_scopes = ["https://www.googleapis.com/auth/admin.directory.user"]
customer_id = "C04189rtm"
google_client = GoogleWorkspace(
    key_file_path=key_file_path,
    admin_email=admin_email,
    api_scopes=api_scopes,
    customer_id=customer_id,
)

access_token = google_client.auth()

csv_file = "users_to_delete.csv"
users_list = []

with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        primary_email = row["primary_email"]
        # Prepare user data for creation
        user_data = primary_email
        users_list.append(user_data)

if users_list:
    print(users_list)
    delete_response = google_client.delete_users(users_list)

    print(delete_response)
