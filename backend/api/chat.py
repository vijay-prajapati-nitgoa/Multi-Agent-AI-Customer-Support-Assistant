from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from rag.rag_pipeline import RAGPipeline

from agents.router import AgentRouter

from database.chat_history import (
    save_chat,
    get_chat_history,
    get_all_sessions,
    delete_session
)


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


class ChatRequest(BaseModel):

    session_id: str
    query: str


rag_pipeline = RAGPipeline()

agent_router = AgentRouter(rag_pipeline)

@router.post("")
async def chat(request: ChatRequest):

    print("\n")
    print("=" * 60)
    print("CHAT API")
    print("=" * 60)

    print("SESSION ID:", request.session_id)
    print("USER QUERY:", request.query)

    if not request.query.strip():

        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty."
        )

    try:

        agent_responses = agent_router.route(
            request.query
        )

        if agent_responses:

            answer = "\n\n".join(
                agent_responses
            )

        else:

            answer = rag_pipeline.answer(
                request.query
            )

        print("ANSWER:", answer)

        save_chat(
            request.session_id,
            request.query,
            answer
        )

        return {
            "response": answer
        }

    except Exception as e:

        print(
            "CHAT ERROR:",
            e
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/sessions")
async def get_sessions():

    try:

        sessions = get_all_sessions()

        return {
            "sessions": sessions
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/{session_id}")
async def get_session(session_id: str):

    try:

        chats = get_chat_history(
            session_id
        )

        messages = []

        for chat in chats:

            messages.append({
                "role": "user",
                "content": chat["question"]
            })

            messages.append({
                "role": "assistant",
                "content": chat["answer"]
            })

        return {
            "messages": messages
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.delete("/{session_id}")
async def delete_chat(session_id: str):

    try:

        delete_session(
            session_id
        )

        return {
            "message": "Chat deleted successfully"
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )