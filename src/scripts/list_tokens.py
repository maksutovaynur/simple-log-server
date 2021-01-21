from src import db

tokens = db.get_allowed_tokens()

print("\n".join((f"'{t.get('user_token', '')}' {t.get('comment', '')}" for t in tokens)))
