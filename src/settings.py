from os.path import join, dirname, abspath, isfile, pardir
from environs import Env

env = Env()

SRC_DIR = abspath(dirname(__file__))
BASE_DIR = abspath(join(SRC_DIR, pardir))
ENV_FILENAME = join(BASE_DIR, ".env")
if isfile(ENV_FILENAME):
    env.read_env(ENV_FILENAME)

MONGO_URL = env.str("MONGO_URL", "mongodb://db:27017")
MIN_TOKEN_LEN = env.int("MIN_TOKEN_LEN", 5)
