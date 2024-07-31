
from fastapi import FastAPI, Request
from src.ai.ai import chat as chat_llm
from pydantic import BaseModel
server = FastAPI()


class MessageRequest(BaseModel):
    message: str


@server.get("/")
async def root():
    return {"message": "Hello, World!"}

@server.post("/chat/")
async def chat(request: MessageRequest):
    message = request.message
    response = await chat_llm(message)
    return {"message": response}