string = "Hello my name is Kevin"

def reverse_string(str):
  reverse = list(reversed(str))
  return "".join(reverse)

print(reverse_string(string))