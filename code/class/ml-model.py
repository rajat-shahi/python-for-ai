class MLModel:
    def __init__(self):
        self.name = "Neural Network"
        self.__api_key = "secret"

    def predict(self,data):
        # Prediction logic
        pass 


model = MLModel()
model.__api_key = "changed"
print(model._MLModel__api_key) # name mangling
print(model.__api_key)
print(vars(model))