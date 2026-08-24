from fastapi import APIRouter
from fastapi import HTTPException

from models.user import RegisterUser
from models.user import LoginUser

from database.mongodb import users

from utils.security import *

from services.auth_service import create_access_token

router=APIRouter(

    prefix="/auth",

    tags=["Authentication"]

)


@router.post("/register")

async def register(user:RegisterUser):

    existing=await users.find_one(

        {

            "email":user.email

        }

    )

    if existing:

        raise HTTPException(

            status_code=400,

            detail="Email already exists"

        )

    await users.insert_one(

        {

            "username":user.username,

            "email":user.email,

            "password":hash_password(user.password)

        }

    )

    return{

        "message":"Registration Successful"

    }


@router.post("/login")

async def login(user:LoginUser):

    db_user=await users.find_one(

        {

            "email":user.email

        }

    )

    if db_user is None:

        raise HTTPException(

            status_code=401,

            detail="Invalid Email"

        )

    if not verify_password(

        user.password,

        db_user["password"]

    ):

        raise HTTPException(

            status_code=401,

            detail="Wrong Password"

        )

    token=create_access_token(

        db_user["email"]

    )

    return{

        "access_token":token,

        "token_type":"bearer"

    }