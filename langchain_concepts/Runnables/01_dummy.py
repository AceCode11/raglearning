import random

class fakellm:
    def __init__(self):
        
        print("llm created")

    def predict(self , prompt):
        response_list = [
            "Delhi is the capital of India" , 
            "AI stands for Artificial Intelligenc" ,
            "Should learn the Rag pipeline"
        ]

        return{'repsonse' : random.choice(response_list)}
    
llm =  fakellm()
print(llm.predict("what is the capital of india"))


    