stock = 5 
if stock > 20: 
   print("Stock is fully available") 
elif stock > 0: 
     print("Limited stock available") 
else: 
    print("Out of stock") 

stock = 10 
premium_member = True 
if stock > 0: 
   print("Product is available") 
   if premium_member: 
      print("Priority delivery available") 
   else: 
         print("Standard delivery available") 
else: 
    print("Product is out of stock") 
   