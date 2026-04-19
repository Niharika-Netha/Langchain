# from langchain_ollama import OllamaLLM
# llm=OllamaLLM(model="kimi-k2.5:cloud",temperature=0.6,max_tokens=50)
# response=llm.invoke("suggest me a cute puppy name")
# print(response)


from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

''' Model creation'''
google_model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

''' Tool creation'''
def solve_quries(query:str)-> str:
    ''' get the solution for the query'''
    return f'here is your answer for the query {query}'

''' AGENT CREATION'''
agent=create_agent(
    model=google_model,
    tools=[solve_quries],
    system_prompt="You are a creative assistant that helps users to solve the quries in a creative way,answer in 20 words."
)

''' Agent invocation'''
response=agent.invoke(
    {
        "messages":[ {"role":"user","content":"Give me 5 unique startup ideas that don’t exist yet?"}]
    }
)
print(response["messages"][-1].content)