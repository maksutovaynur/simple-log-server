from src import db

tokens = db.get_allowed_tokens()

print("\n".join(tokens))
