#pip install boto3
#pip install langchain
#pip install langchain-aws
#pip isntall streamlit

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain_aws import ChatBedrock


def demo_chatbot():
    max_gen_len = 128
    temperature = 0.1
    top_p = 0.9
    demo_llm=ChatBedrock(
        credentials_profile_name="default",
        model_id="meta.llama3-8b-instruct-v1:0",
        model_kwargs={
            "max_gen_len": max_gen_len,
            "temperature": temperature,
            "top_p": top_p
        }
    )
    return demo_llm

store = {}  # memory is maintained outside the chain

def demo_memory(session_id):
    llm_data=demo_chatbot()
    memory=ConversationBufferMemory(
        llm=llm_data, 
        max_token_limit=128,
        chat_memory=store[session_id],
        k=3,
        return_messages=True
        )
    return memory

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

    memory = demo_memory(session_id)
    assert len(memory.memory_variables) == 1
    key = memory.memory_variables[0]
    messages = memory.load_memory_variables({})[key]
    store[session_id] = InMemoryChatMessageHistory(messages=messages)
    return store[session_id]

def demo_conversation(input_text, session_id):
    llm_chain_data=demo_chatbot()
    llm_conversation = RunnableWithMessageHistory(
        llm_chain_data,
        get_session_history
    )

    chat_reply=llm_conversation.invoke(
        input_text,
         config={"configurable": {"session_id": session_id}})
    return chat_reply

