class APIConfig:
    def __init__(self, api_key, model = "gpt-5.5", max_tokens = 100):
        self.api_key = api_key
        self.model = model 
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"


# create different configurations 
# using positional for required arg, named for optional 
dev_config = APIConfig("sk-dev-key",max_tokens=50)

# using all named arguments 
prod_config = APIConfig(api_key="sk-prod-key",model="gpt-5.6",max_tokens=1000)


# Access the configuration
print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens)