import datetime
import pathlib
from typing import Mapping
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data_dir = pathlib.Path('./data')
if not data_dir.exists():
    data_dir.mkdir()

class Message(BaseModel):
    text: str

@app.post("/{user}", response_model=Message)
def say(user: str, message: Message):
    now = datetime.datetime.now().isoformat()
    user_path = data_dir / user
    msg = f"{now}: {message.text}\n"
    with user_path.open("a", encoding='utf-8') as log:
        log.write(msg)
    return message

@app.get("/", response_model=Mapping[str, str])
def hear():
    messages = {}
    for file in data_dir.iterdir():
        messages[file.name] = file.read_text(encoding='utf-8')
    return messages
