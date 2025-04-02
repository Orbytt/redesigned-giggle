def collatz_sequence(x):

    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x // 2
       else:
         x = 3 * x + 1 
       seq.append(x)
    seq = ' '.join(str(y) for y in seq)
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
def num_to_let(current_no):
  current_no = int(current_no)
  if current_no > 26:
    new_current_no = current_no % 26
  else:
    new_current_no = current_no
  print("the number " + str(current_no) + " currently translates to the divided # "+ str(new_current_no)+ " and the letter "+ chr(ord('a') + new_current_no - 1))
  return chr(ord('a') + new_current_no - 1)

def cipher(string):
  code = ''
  for a in string:
    code = code + collatz_sequence(int(let_to_num(a)))
  return code
def decipher(number_list):
  code = ''
  for b in number_list:
    code = code + num_to_let(number_list[int(b)])
  return code

string = input("Input text! ")
string = string.replace(" ", "") 
number_list = cipher(string).split()
print(number_list)
print(decipher(number_list))