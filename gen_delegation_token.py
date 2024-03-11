import argparse
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials



def generate_oauth_token(service_account_file, user_email, scopes):
    """
    Generate an OAuth token for a user by using domain-wide delegation.

    Parameters:
    - service_account_file: Path to the service account JSON key file.
    - user_email: The email of the user to impersonate.

    Returns:
    A credentials object that includes the token.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        service_account_file,
        scopes=scopes,
    )

    credentials = credentials.create_delegated(user_email)
    token_obj = credentials.get_access_token()

    return token_obj.access_token

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate OAuth token using domain-wide delegation")
    parser.add_argument("--user-email", required=True, help="Email of the user to impersonate")
    parser.add_argument("--key-file", required=True, help="Path to the service account JSON key file")
    parser.add_argument("--scopes", help="Add comma separated list of scopes (by default only https://www.googleapis.com/auth/admin.directory.user)")
    
    args = parser.parse_args()

    key_file_path = args.key_file
    user_email = args.user_email
    scopes = [s.strip() for s in args.scopes.split(",")] if args.scopes else ['https://www.googleapis.com/auth/admin.directory.user']

    token = generate_oauth_token(key_file_path, user_email, scopes)

    print(f"Access Token: {token}")
    print()
    print(f"export CLOUDSDK_AUTH_ACCESS_TOKEN={token}")