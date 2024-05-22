def main():
  print('''PASSWORD VERIFIER:\n==================== \nPasswords must:
  - be 6 or more characters
  - have at least one lower case letter
  - have at least one upper case letter
  - have at least one digit \n ''') 

  while True:
    string = input("Enter your password: ")
    print()
    if is_valid(string):
      break
    else:
      print()
      continue
      
  
def has_upper(up):
  for ch in up:
    if ch.isupper():
      return True
  return False

def has_lower(low):
  for ch in low:
    if ch.islower():
      return True
  return False

def has_digit(dig):
  for ch in dig:
    if ch.isdigit():
      return True
  return False

def has_length(lg):
  return len(lg) > 5

def is_valid(pw):
  # does it have lower, upper, digit, and length
  valid = has_upper(pw) and has_lower(pw) and has_digit(pw) and has_length(pw)
  if valid:
    print("Password is valid")
  else:
    print("Password is invalid for the following reasons:")
  # display messages
  # if no upper - message need upper
  if not has_upper(pw):
   print("-Missing an uppercase letter")
  #if no lower - message need lower
  if not has_lower(pw):
    print("-Missing a lowercase letter")  
  # if no digit - message need digit
  if not has_digit(pw):
    print("-Missing a digit")
  # if not long enough - message need longer
  if not has_length(pw):
    print("-Password must be at least 6 characters long")
  # return valid
  return valid

main()
  




