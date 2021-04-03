myVar = input("What is your answer to my 1st question? (yes/no) ")  
if myVar == "yes":
  myNextVar = input("What is your answer to my 2nd question? (yes/no) ")
  if myNextVar == "yes":
    print("you got 100% :D")
  elif myNextVar == "no":
    print("damn you got 50%")
  else:
    print("Answer my question! You didn't type yes or no.")
elif myVar == "no":
  print("you failed...")
else:
  print("Answer my question! You didn't type yes or no.")