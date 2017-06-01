def factorial(n):
  total = 1
  total1 = 0
  for i in range(1, 100):
    total = total * i 
    
  d = str(total)
  for i in d:
    total1 = total1 + int(i) 
  print total1
  
  return 



factorial(10)

