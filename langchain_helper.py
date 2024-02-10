from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain 
from dotenv import load_dotenv 

load_dotenv()

def plant(typeOfPlant, question):
    llm = OpenAI(temperature=.5,max_tokens = 4000,model="gpt-3.5-turbo-instruct")
    plantTemplate = PromptTemplate(
        input_variables= ["typeOfPlant","question"],
        template = """
        You are a helpful gardening/nursery assistant that that can answer questions about plants
        
        Answer the following question: {question}
        By searching the following plant: {typeOfPlant}
        
        Only use the factual information to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed.
        """, 
    )
    
    plantChain = LLMChain(llm = llm, prompt = plantTemplate, output_key="answer")

    response = plantChain.invoke({'typeOfPlant':typeOfPlant,'question':question})

    return response 

if __name__ == "__main__":
    print(plant('mini monstera','why are the leaves turning yellow?'))