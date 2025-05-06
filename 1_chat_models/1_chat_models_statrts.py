from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model = "gpt-4o-mini")
llm_response = llm.invoke("sqare root of 49")
print(llm_response)
print(llm_response.content)