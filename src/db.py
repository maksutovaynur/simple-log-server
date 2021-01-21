import pymongo as pm

from src import settings as S


_client = pm.MongoClient(S.MONGO_URL)
_db = _client.get_database("cash_logs")
_db_users = _db.get_collection("users")
_db_logs = _db.get_collection("logs")


def get_user_by_token(token: str):
    return _db_users.find_one({"user_token": token})


def get_allowed_tokens():
    return list(_db_users.find({}))


def update_or_create_user_by_token(token: str, **kwargs):
    token_len = len(token)
    if token_len < S.MIN_TOKEN_LEN: raise Exception(f"token is too short: {token_len} < {S.MIN_TOKEN_LEN}")
    _db_users.update_many({"user_token": token}, {"$set": {"user_token": token, **kwargs}}, upsert=True)


def add_log(token: str, log_data: dict):
    _db_logs.insert_one({"user_token": token, "log_data": log_data})

