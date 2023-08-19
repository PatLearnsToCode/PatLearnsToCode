level = float(input("Enter pH Level:  "))

if level < 7:
  print("pH level: Acidic")
elif level > 7:
  print("pH level: Basic")
else: 
  print("pH level: Neutral")