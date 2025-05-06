from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()
model = ChatOpenAI(model = "gpt-4o-mini")
chat_history = []
system_messages = SystemMessage(content="you are a healpful AI asisstent")
chat_history.append(system_messages)

while True:
    query = input("you :")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))
    print(f"AI : {response}")


