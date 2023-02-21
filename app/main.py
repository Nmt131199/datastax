import pathlib
from fastapi import FastAPI
from typing import Optional
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json
app = FastAPI()

BASE_DIR = pathlib.Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR.parent / "models"
SMS_SPAM_MODEL_DIR = MODEL_DIR / "spam-sms"
MODEL_PATH = SMS_SPAM_MODEL_DIR / "spam-model.h5"
TOKENIZER_PATH = SMS_SPAM_MODEL_DIR / "spam-classifer-tokenizer.json"
METADATA_PATH = SMS_SPAM_MODEL_DIR / "spam-classifer-metadata.json"

AI_MODEL = None
AI_TOKENIZER = None
# This run on strt-up to get our prediction model
@app.on_event("startup")
def on_startup():
    global AI_MODEL, AI_TOKENIZER
    if MODEL_PATH.exists():
        AI_MODEL = load_model(MODEL_PATH)
    if TOKENIZER_PATH.exists():
        t_json = TOKENIZER_PATH.read_text()
        AI_TOKENIZER = tokenizer_from_json(TOKENIZER_PATH.read_text())
        print(AI_TOKENIZER)

@app.get("/")
def read_index(q:Optional[str] = None):
    global AI_MODEL
    print(AI_MODEL)
    return {"hello": "world"}