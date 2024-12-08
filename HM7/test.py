import torch
print(dir(torch._dynamo))  # Inspect available attributes
print(torch._dynamo.__doc__)  # Print the docstring
print('external_util' in dir(torch._dynamo))  # Check if an attribute is available