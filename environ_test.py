from os import environ

environ.setdefault("MY_VAR_1", "Hello")
environ.setdefault("MY_VAR_2", "World")

print(f"The value of MY_VAR_1 is: {environ['MY_VAR_1']}")
print(f"The value of MY_VAR_2 is: {environ['MY_VAR_2']}")
