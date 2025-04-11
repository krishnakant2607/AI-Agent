import os
from dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage



#openai_llm = ChatOpenAI(model = "gpt-4o-mini")
#groq_llm = ChatGroq(model = "gemma2-9b-it")

search_tool = TavilySearchResults(max_results=3)




def get_response_from_ai_agent(llm_id, query , allow_search , system_promt, provider):

    if provider == "groq":
        llm = ChatGroq(model = llm_id)
    elif provider == "openai":
        llm = ChatOpenAI(model = llm_id)  

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    system_prompt = "Act as a an AI assistant who is smart and friendly"
    agent = create_react_agent(
        model = llm,
        tools = tools,
        state_modifier = system_prompt
    )

    state = {"messages" : query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_message = [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_message[-1]