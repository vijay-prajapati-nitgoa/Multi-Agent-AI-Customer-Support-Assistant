from pymongo import MongoClient

from datetime import datetime

from config import MONGODB_URL, DATABASE_NAME


# -----------------------------
# MongoDB Connection
# -----------------------------

client = MongoClient(
    MONGODB_URL
)

db = client[
    DATABASE_NAME
]

history = db[
    "chat_history"
]


# -----------------------------
# Save Chat
# -----------------------------

def save_chat(
    session_id,
    question,
    answer
):

    history.insert_one({

        "session_id": session_id,

        "question": question,

        "answer": answer,

        "timestamp": datetime.utcnow()

    })


# -----------------------------
# Get Chat History
# -----------------------------

def get_chat_history(
    session_id
):

    chats = history.find(

        {
            "session_id": session_id
        }

    ).sort(
        "timestamp",
        1
    )

    result = []

    for chat in chats:

        result.append({

            "question": chat["question"],

            "answer": chat["answer"],

            "timestamp": chat["timestamp"]

        })

    return result


# -----------------------------
# Get All Sessions
# -----------------------------

def get_all_sessions():

    return history.distinct(
        "session_id"
    )


# -----------------------------
# Delete Session
# -----------------------------

def delete_session(
    session_id
):

    history.delete_many({

        "session_id": session_id

    })