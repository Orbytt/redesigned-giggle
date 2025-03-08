def collatz_sequence(x):

    seq = [x]
    print(type(x))
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x // 2
       else:
         x = 3 * x + 1 
       seq.append(x)
    seq = ' '.join(str(y) for y in seq)
    print(type(seq),seq)
    return seq

def let_to_num(string):
  index = 0
  string = string.lower()
  for letter in " " + "abcdefghijklmnopqrstuvwxyz":
    if string == letter:
      number = str(index) + " "
      return number
    index = index + 1
  return ""
def num_to_let(num):
  for number in range (len(num)):
    number = number // 26
    print(int(number))

def cipher(string):
  code = ''
  for a in string:
    code = code + collatz_sequence(int(let_to_num(a)))
  return code

string = input("Input text! ")
string = string.replace(" ", "")
numbers = cipher(string)
number_list = numbers.split()
print(number_list)
num_to_let(number_list)
print(5//26)