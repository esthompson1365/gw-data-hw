# The list of pies to print to the screen
pieList = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry","Buko", "Burek", "Tamale", "Steak"]

# The list used to store all of the candies selected inside of
pieCart = []

def CountFrequency(pieCart): 
  
    # Creating an empty dictionary  
    freq = {} 
    for items in pieCart: 
        freq[items] = pieCart.count(items) 
      
    for key, value in freq.items(): 
        print (value, key) 
  

# Print out options
print("Welcome to the House of Pies! Here are our pies:")
for i in range(len(pieList)):
    print("[" + str(i) + "] " + pieList[i])

x = "Yes"
while x == "Yes":
    choice = int(input("What would you like?"))
    
    print(f'Great! We will have that {pieList[choice]} pie right out for you.')
    
    pieCart.append(pieList[choice]) 
    
    x = input("Would you like to make another order?")

print("You purchased:")
CountFrequency(pieCart) 

