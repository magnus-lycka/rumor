import datetime
import pathlib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data_dir = pathlib.Path('./data')
if not data_dir.exists():
    data_dir.mkdir()


class Message(BaseModel):
    text: str


@app.post("/{user}")
async def say(user: str, message: Message):
    user_path = data_dir / user
    with user_path.open("a", encoding='utf-8') as log:
        now = datetime.datetime.now().isoformat()
        msg = f"{now}: {message.text}\n"
        log.write(msg)
    return message


@app.get("/")
async def hear():
    messages = {}
    for file in data_dir.iterdir():
        messages[file.name] = file.read_text(encoding='utf-8')
    return messages

