import re
import bcrypt
import os

# API_KEY = "token_do_alexandre_para_trabalhar_e_debugarae" #dev and stg

API_KEY = os.getenv("token_ecr_staging") #staging

SALT = os.getenv("DSALT")

def _hash_token(api_key: str) -> str:
    return str(bcrypt.kdf(
        password=api_key.encode('UTF-8'),
        salt=SALT.encode('UTF-8'),
        desired_key_bytes=32,
        rounds=len(SALT)**2))


print(API_KEY)

print(_hash_token(API_KEY))


token = _hash_token(API_KEY)

print (token)

st =  ("'"+token + "''")

sql = re.sub(r"b'", "b''", st, count=1)
print(sql)

