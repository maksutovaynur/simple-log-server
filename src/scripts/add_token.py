from src import db
import uuid
import sys

if len(sys.argv) < 2:
    token = input("Enter new user's token (leave empty to generate random): ")
else:
    token = sys.argv[1]

if token == "gen" or len(token) == 0:
    token = uuid.uuid4().hex


db.update_or_create_user_by_token(token)

print(f"New user with token '{token}' was generated")
