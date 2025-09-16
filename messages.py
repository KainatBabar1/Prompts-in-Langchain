from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')
messaages=[
    SystemMessage(content="you are a helpful asssistant"),
    HumanMessage(content='tell me about ai')
]


result =model.invoke(messaages)

messaages.append(AIMessage(content=result.content))
print(messaages)