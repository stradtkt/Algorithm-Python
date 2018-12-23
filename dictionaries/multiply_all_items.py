the_dict = {'1': 100, '2': 200, '3': 300, '4': 400, '5': 500}

result = 1
for key in the_dict:
    result *= the_dict[key]

print(result)
