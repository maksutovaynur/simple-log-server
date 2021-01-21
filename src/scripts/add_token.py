from src import db
import uuid
import sys

if len(sys.argv) < 2:
    token = input("Enter new user's token (leave empty to generate random): ")
else:
    token = sys.argv[1]

if token == "gen" or len(token) == 0:
    token = uuid.uuid4().hex

if len(sys.argv) < 3:
    comment = input("Any comment to bind with token (leave empty to skip)? ")
else:
    comment = sys.argv[2]

kwargs = dict()

if comment:
    kwargs.update(comment=comment)

db.update_or_create_user_by_token(token, **kwargs)

print(f"New user with token '{token}' was generated")
