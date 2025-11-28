from fastapi import FastAPI
from pydantic import BaseModel
from agent import chat_agent

app = FastAPI()

class Message(BaseModel):
    Message: str

@app.post('/chat')
async def chat(data: Message):
    response = chat_agent(data.Message)
    return{'response': response}