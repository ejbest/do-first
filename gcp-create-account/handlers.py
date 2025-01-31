import requests
import json
from google.oauth2 import service_account
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request


class GoogleWorkspace:

    def __init__(self, key_file_path, admin_email, api_scopes, customer_id):
        self.key_file_path = key_file_path
        self.admin_email = admin_email
        self.api_scopes = api_scopes
        self.customer_id = customer_id
        self.api_url = f"https://admin.googleapis.com/admin/directory/v1/users"

    def auth(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.key_file_path, scopes=self.api_scopes
            )

            delegated_credentials = credentials.with_subject(self.admin_email)
            auth_request = Request()
            delegated_credentials.refresh(auth_request)

            access_token = delegated_credentials.token
            return access_token
        except RefreshError as e:
            return e

    def list_users(self):
        access_token = self.auth()
        if not access_token:
            print("Failed to get access token.")
            return

        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(
            f"{self.api_url}?customer={self.customer_id}",
            headers=headers,
        )

        if response.status_code == 200:
            users = response.json().get("users", [])
            emails = []
            for user in users:
                # Extracting primary email and other emails if present
                user_emails = [email["address"] for email in user.get("emails", [])]
                emails.extend(user_emails)

            print("User Emails:", emails)
            return emails
        else:
            print(
                f"Failed to fetch users. Status: {response.status_code}, Error: {response.text}"
            )
            return None

    def create_user(self, user_data):
        access_token = self.auth()
        if not access_token:
            print("Failed to get access token.")
            return

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        response = requests.post(
            f"{self.api_url}?customer={self.customer_id}",
            headers=headers,
            data=json.dumps(user_data),
        )

        if response.status_code == 200:
            print(f"User {user_data['primaryEmail']} created successfully.")
        else:
            print(
                f"Failed to create user {user_data['primaryEmail']}. Status: {response.status_code}, Error: {response.text}"
            )

    def create_users(self, users_list):
        for user_data in users_list:
            print(f"Creating user with email {user_data.get('primaryEmail')}")
            self.create_user(user_data)

    def delete_user(self, email):
        access_token = self.auth()
        if not access_token:
            print("Failed to get access token.")
            return

        headers = {
            "Authorization": f"Bearer {access_token}",
        }

        url = f"{self.api_url}/{email}"
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            print(f"User {email} has been successfully deleted.")
        else:
            print(
                f"Failed to delete user {email}. Status: {response.status_code}, Error: {response.text}"
            )

    def delete_users(self, email_list):
        for email in email_list:
            print(f"Deleting user with email {email}")
            self.delete_user(email)
