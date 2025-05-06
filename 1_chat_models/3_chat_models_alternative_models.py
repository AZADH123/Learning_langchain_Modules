from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

messages = [
     
      SystemMessage("you are a expert in social meadia content strategy"),
      HumanMessage("Give a short tip to creste engaging post on instagram")

      
       ]

#OPENAPI
model = ChatOpenAI(mode= "gpt-4o-mini")
result = model.invoke(messages)
print(f"Answer from OpenAI:{result.content}")

#ANTHROPIC

model = ChatAnthropic(model="claude-3-opus-20240229")

result = model.invoke(messages)
print(f"Answer from Anthropic: {result.content}")


#GEMINI
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

result = model.invoke(messages)
print(f"Answer from Google: {result.content}")

