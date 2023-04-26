from fastapi import FastAPI, Header
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


@app.get('/example')
def example_get(CONTAINER_ID: str = Header()):
    # Использование значения из хедера
    return {'CONTAINER_ID': CONTAINER_ID}


@app.post('/example')
def example_post(CONTAINER_ID: str = Header()):
    # Использование значения из хедера
    return {'CONTAINER_ID': CONTAINER_ID}
