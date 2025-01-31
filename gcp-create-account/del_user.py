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

# List of email addresses to delete
email_list = ["mike@nextresearch.io"]


delete_response = google_client.delete_users(email_list)

print(delete_response)
