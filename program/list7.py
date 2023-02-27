print("Simple STACK Data Structure Program")  
stack = [] 

while True:  
    print("\nSELECT APPROPRIATE CHOICE")                    
    print("1. PUSH Element into the Stack")  
    print("2. POP Element from the Stack") 
    print("3. Display Elements of the Stack")  
    print("4. Exit")  
    choice = int(input("Enter the Choice:"))

    if choice == 1:   
        userIn=input("Enter Item to be pushed : ")
        stack.append(userIn)
        print(f"PUSHED TO STACK")
  
    elif choice == 2:
        if len(stack) == 0:
            print('The STACK is EMPTY No element to POP out') 
        else:    
            print('\nElement POP out from the STACK is:')  
            print(stack.pop())
    elif choice == 3:
        if len(stack) == 0:                       
            print('The STACK is EMPTY') 
        else:
            print("The Size of the STACK is: ",len(stack))         
            print('\nSTACK elements are as follows:')            
            for ele in stack:
                print(ele)                  

    elif choice == 4:  
        break   
    else:  
        print("Oops! Incorrect Choice")