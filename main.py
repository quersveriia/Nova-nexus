from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Nova AI backend is running"}

@app.post("/chat")
def chat(msg: Message):

    user_message = msg.text.lower()

    # simple example responses
    if "hello" in user_message:
        reply = "Hello! I'm Nova, your assistant."

    elif "how are you" in user_message:
        reply = "I'm doing great! How can I help you?"

    elif "call" in user_message:
        reply = "I can help you make calls once connected to your phone."

    else:
        reply = "That's interesting. Tell me more."

    return {"reply": reply}
