from fastapi import FastAPI
from pydantic_models.chat_body import ChatBody

app = FastAPI()

@app.post("/chat")
def chat_endpoint(body: ChatBody):
    # search the web and find appropriate sources 
    # sort the sources by relevance
    # generate the response using LLM models 
    return body.query

