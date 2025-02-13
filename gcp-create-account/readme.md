#### 1. Create a Google Cloud Project:
- Go to the Google Cloud Console.
- Select a Project "gcp-terraform-udemy-course"  (or other Project)

### 2. Enable the Admin SDK API
- Go to the Google Cloud Console
- Click 3 lines or "hamburger"
- Select API APIs & Services
- In search bar (Search for APIs & Services)
- Search for "Admin SDK API" 
- Ensure "Admin SDK API" is enabled 
- Select Google Admin SDK and click Enable.

### 3 Set Up OAuth 2.0 & Service Account
- You’ll need to authenticate your script using a Service Account with Domain-wide delegation. Here’s how to set it up:

&nbsp;&nbsp;&nbsp;&nbsp;Create a Service Account
- Go to the Google Cloud Console
- Click 3 lines or "hamburger"
- Select IAM & Admin
- Select Service Accounts 
- Create or Ensure you have a Service Account
- Required Parameters
    Name "Admin SDK Service Account"
    Description "Manage admin users"
 - Under Role, assign it the Project > Owner role
 - This will give root or analyze granular permissions 
 - Click Done

&nbsp;&nbsp;&nbsp;&nbsp;Enable Domain-Wide Delegation
- After creating the service account, click the service account name.
- Example: admin-sdk-service-account@gcp-terraform-udemy-course.iam.gserviceaccount.com
- Select Service Account email
- Select "Client ID" Example: 101415368317943506973
- Click Google Workspace Admin Console
- Go to the Admin Console of your Google Workspace domain.
- Go to Security > Access and data control > API Controls > Domain-Wide Delegation
- Click MANAGE DOMAIN WIDE DELEGATION
- Click Add new
- FYI Need client ID of the Service Account: "Client ID" Example: 101415368317943506973
- in Client ID: "101415368317943506973"
- In the OAuth Scopes "https://www.googleapis.com/auth/admin.directory.user"
<br>
- FYI This will allow the service account to manage users on behalf of the domain.

### 4 Create and Download the Service Account Key
- Go to the Google Cloud Console
- Click 3 lines or "hamburger"
- Select IAM & Admin
- Select Service Accounts 
- After creating the service account, click the Actions menu (three dots) next to your service account, then select Create Key.
- Choose the JSON key type and click Create.
- This will download the service account credentials to your machine. Save this JSON file securely because you’ll need it later to authenticate.
<br>
- This is the KEY JSON FILE THAT IS NEEDD

### 4 Create and Download the Service Account Key
- tops of each of add_user.py, del_user.py, list_users.py will need to have updates 
- check the first 10 lines for key and attributes for environment there 

### 

## Run:
<pre>
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

python3 -m venv env && source env/bin/activate && pip3 install -r requirements.txt
</pre>

### Add users:
<pre>
python3 add_user.py
</pre>