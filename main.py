from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/me")
def read_me(request: Request):
    container_id = request.headers.get('CONTAINER_ID')
    return {
        "hello": "container1",
        "yourIP": request.client.host,
        "headerinfo": container_id
    }