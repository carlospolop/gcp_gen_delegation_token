# Generate Delegation Token

This tool can be used to generate an authenticated OAuth token as a delegated user indicating the users email and the SA json credentials path.

```bash
# Install
pip3 install -r requirements.txt

# Help
python3 gen_delegation_token.py -h
usage: gen_delegation_token.py [-h] --user-email USER_EMAIL --key-file KEY_FILE [--scopes SCOPES]

Generate OAuth token using domain-wide delegation

options:
  -h, --help            show this help message and exit
  --user-email USER_EMAIL
                        Email of the user to impersonate
  --key-file KEY_FILE   Path to the service account JSON key file
  --scopes SCOPES       Add comma separated list of scopes (by default only
                        https://www.googleapis.com/auth/admin.directory.user)

# Impersonate indicated user
python3 gen_delegation_token.py --user-email <user-email> --key-file <path-to-key-file>

# Impersonate indicated user and add additional scopes
python3 gen_delegation_token.py --user-email <user-email> --key-file <path-to-key-file> --scopes "https://www.googleapis.com/auth/userinfo.email, https://www.googleapis.com/auth/cloud-platform, https://www.googleapis.com/auth/admin.directory.group, https://www.googleapis.com/auth/admin.directory.user, https://www.googleapis.com/auth/admin.directory.domain, https://mail.google.com/, https://www.googleapis.com/auth/drive, openid"
```