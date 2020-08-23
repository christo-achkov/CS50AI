from logic import *

rain = Symbol("It is raining.")
hagrid = Symbol("Harry visited Hagrid.")
dumbledore = Symbol("Harry visited Dumbledore.")

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(knowledge.formula())
print(model_check(knowledge, rain))
print(model_check(knowledge, hagrid))
print(model_check(knowledge, dumbledore))
