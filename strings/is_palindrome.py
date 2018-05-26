string = "racecar"
string2 = "car"
def is_palindrome(str):
  if str == str[::-1]:
    return True
  else:
    return False

print(is_palindrome(string))
#True
print(is_palindrome(string2))
#False
