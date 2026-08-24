from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat import router as chat_router
from api.upload import router as upload_router


app = FastAPI(
    title="Multi-Agent AI Customer Support"
)


# -----------------------------
# CORS
# -----------------------------

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# -----------------------------
# Routes
# -----------------------------

app.include_router(
    chat_router
)

app.include_router(
    upload_router
)


# -----------------------------
# Root
# -----------------------------

@app.get("/")
async def root():

    return {
        "message":
            "Multi-Agent AI Backend is running"
    }