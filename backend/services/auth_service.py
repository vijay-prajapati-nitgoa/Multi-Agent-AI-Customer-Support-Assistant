from jose import jwt

from datetime import datetime,timedelta

from config import *


def create_access_token(email):

    expire = datetime.utcnow()+timedelta(

        minutes=ACCESS_TOKEN_EXPIRE_MINUTES

    )

    payload={

        "sub":email,

        "exp":expire

    }

    token=jwt.encode(

        payload,

        SECRET_KEY,

        algorithm=ALGORITHM

    )

    return token