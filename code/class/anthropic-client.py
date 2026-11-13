class AnthropicClient:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def connect(self,username,API_KEY):
        print(f"{username} is connected with {self.name} - {self.model}")


app = AnthropicClient("Claude","Sonnet-5.5")
app.connect("rajat-shahi","ant-1234k")