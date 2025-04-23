import jwt
import os
from datetime import datetime , UTC , timedelta

SERVER_SECRET_KEY = os.getenv('SECRET_KEY')

#payload is dictionary that contain the claims.
def encode_jwt(payload : dict) -> str:
    token_expire_time = datetime.now(UTC) + timedelta(hours=1)
    payload["exp"] = token_expire_time
    return jwt.encode(payload, SERVER_SECRET_KEY, algorithm='HS256')

def decode_jwt(token: str) -> dict | None:
    try :
        return jwt.decode(token, SERVER_SECRET_KEY, algorithms=['HS256'])
    except:
        return None

print(encode_jwt({
    "name" : "mohammadreza"
}))

