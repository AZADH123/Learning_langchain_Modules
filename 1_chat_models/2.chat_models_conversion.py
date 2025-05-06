from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model = "gpt-4o-mini")
messages = [
     
      SystemMessage("you are a expert in social meadia content strategy"),
      HumanMessage("Give a short tip to creste engaging post on instagram")

      
]
result = llm.invoke(messages)
print(result.content)