from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent

app = FastAPI()

class Message(BaseModel):
    Message: str

@app.post('/chat')
async def chat(data: Message):
    response = agent.run(data.Message)
    return{'response': response}