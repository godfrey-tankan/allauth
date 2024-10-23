from django.test import TestCase

# Create your tests here.

def testMyFunc(**params):
    print(params)
    return params.get("name")

call_it = testMyFunc(name="tnqn", age=23,hobby="coding", country="Zim")
print(call_it)
