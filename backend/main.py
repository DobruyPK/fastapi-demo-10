from fastapi import FastAPI, Header
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()


@app.get('/example')
def example_get(CONTAINER_ID: str = Header()):
    return {'CONTAINER_ID': CONTAINER_ID, 'data': 'Im Container 1'}


@app.post('/example')
def example_post(CONTAINER_ID: str = Header()):
    return {'CONTAINER_ID': CONTAINER_ID, 'data': 'Im Container 1'}
