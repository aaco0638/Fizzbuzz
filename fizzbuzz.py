def fizzbuzz(n): #function that prints up to n sequence
   for i in range(1, n+1): #i is at least 1 and after every pass through goes up by 1
      if i%15 == 0: #checks if i is divisable by 15, if a remainder is returned moves on to next elif.
         print("fizzbuzz") #prints fizzbuzz in that position
      elif i%3 == 0: #checks if i is divisable by 3, if a remainder is returned moves on to next elif.
         print("fizz") #prints fizz in that position
      elif i%5 == 0: #checks if i is divisable by 5, if a remainder is returned moves on to next elif.
         print("buzz") #prints buzz in that position 
      else: 
         print(i) #prints i  