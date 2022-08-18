unit = int(input("please enter a unit "))


if unit <= 100:
    print("No charge, Enjoy free light bro! ")

elif unit > 200:
    pay = (unit - 200)*10
   
    
    print("your charge is ",  pay + 500) 


elif unit > 100:
    first = unit - 100
    pay = first * 5
    print("your charge is ",  pay) 



    
    
       


