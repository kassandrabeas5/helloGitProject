# Updated hello.py that imports a list from another file
from facts import fun_facts

def say_hello():
    print("Hey there! Time for some fun facts:\n")
    for fact in fun_facts:
        print("-", fact)

say_hello()
