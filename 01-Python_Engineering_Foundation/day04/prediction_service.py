class PredictionRequest:
    def __init__(self, features:dict):
        if not features:
            raise ValueError("Features cannot be empty.")
        
        self.features = features

    def display_results(self):
        print(f"Prediction features: {self.features}")

class ModelService:
    def make_prediction(self, request: PredictionRequest) -> str:
        features = request.features
        print(f"Received features: {features}")
        return "Prediction completed successfully"


request = PredictionRequest({
    "age": 30,
    "experience": 5
})

service = ModelService()
# result = service.make_prediction(request)
# print(result)

try:
    request = PredictionRequest({})
    result = service.make_prediction(request)
    print(result)

except ValueError as error:
    print(f"Input Validation error: {error}")
