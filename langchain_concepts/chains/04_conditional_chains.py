from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel , RunnableBranch ,RunnableLambda
from langchain_core.output_parsers import StrOutputParser

from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="The sentiment analysis classification label")

parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template="Classify the sentiment feedback text into positive and negative.\n\n{format_instructions}\n\nFeedback text to analyze: {feedback}", 
    input_variables=['feedback'],
    partial_variables={"format_instructions": parser2.get_format_instructions()} # Spelt correctly!
)

classifier_chain = prompt1 | model | parser2



prompt2 = PromptTemplate(
    template="Write appropriate response for the positive feedback \n {feedback}", 
    input_variables=['feedback'],
    )


prompt3 = PromptTemplate(
    template="Write appropriate response for the negative feedback \n {feedback}", 
    input_variables=['feedback'],
    )

chain1 = prompt2 | model | parser
chain2 = prompt3 | model | parser

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive' , chain1), 
    (lambda x:x.sentiment == 'negative' , chain2),
    RunnableLambda(lambda x : "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({"feedback" : "This is terrible phone"}))