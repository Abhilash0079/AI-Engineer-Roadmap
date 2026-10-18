## Inheritance — “is a” relationship
class Animal:
    def eat(self):
        print("Animal is eating.")

class Cat(Animal):
    def meow(self):
        print("Meow!")

cat = Cat()
cat.eat()
cat.meow()

## Composition — “has a” relationship
class PredictionModel:
    def predict(self):
        print("Prediction generated")

class ModelService:
    def __init__(self, model):
        self.model = model

    def make_prediction(self):
        self.model.predict()

model = PredictionModel()
service = ModelService(model)
service.make_prediction()