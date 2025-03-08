
def numlet(string):
  index = 1 
  string = string.lower()
  for letter in "abcdefghijklmnopqrstuvwxyz":
    if string == letter:
      number = str(index) + " "
      return number
    index = index + 1
  return ""

def cipher(string):
  code = ""
  for a in string:
    code = code + numlet(a)
  return code

string = input("Input text! ")
print(cipher(string))