# OOP: way to organize code by grouping the related data and functions together 
# instead of having seperate variables and functions scattered around, you bundle them into objects
# without OOP : tools scattered everywhere
# with OOP : tools organised in labeled compartments


# A class is a blueprint for creating objects
# Attributes : what data the object stores
# Methods : what the object can do

# without classes
name = "OpenAI"
model = "gpt-4o-mini"

def generate_response(prompt):
    # process prompt . . . 
    response = "some output"
    return response 


# with classes - everything bundled together 

class OpenAIClient:
    def __init__(self,provider,model):
        self.provider = provider
        self.model = model 
        pass

    def model_info(self):
        print(f"Provider => {self.provider}, Model => {self.model}")

    def generate_response(self,prompt):
        # some logic
        hardcoded_response = "I am chatGPT by OPENAI"
        print(f"Prompt : {prompt}")
        print(f"Response : {hardcoded_response}")

ins = OpenAIClient("OpenAI","GPT-5.5")
ins.model_info()
ins.generate_response("Hi, who are you?")