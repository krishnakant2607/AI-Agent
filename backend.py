from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent

from fastapi import FastAPI

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool
    

#from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = ["gemma2-9b-it"]

app = FastAPI(title="LangGraph Chatbot API")

@app.post("/chat")
def chat_endpoint(request : RequestState):
    """
    Endpoint to interact with the chatbot using LangGraph and searchtools 
    It dynamically selects the model based on the request.
    """

    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Model not allowed. Kindly select a valid model name "}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Crearting a model and getting response from it
    reponse = get_response_from_ai_agent(llm_id, query , allow_search , system_prompt, provider)
    return reponse    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "127.0.0.1", port = 9999)

