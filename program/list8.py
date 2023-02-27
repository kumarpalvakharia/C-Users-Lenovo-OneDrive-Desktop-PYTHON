print("Simple Queue Data Structure Program")  
queue = [] 

while True:  
    print("\nSELECT APPROPRIATE CHOICE")                    
    print("1. Enqueue")  
    print("2. Dequeue") 
    print("3. Display Elements of the Queue")  
    print("4. Exit")  
    choice = int(input("Enter the Choice:"))

    if choice == 1:   
        userIn=input("Enter Item to Queue: ")
        queue.append(userIn)
        print(f"PUSHED TO Queue")
  
    elif choice == 2:
        if len (queue) == 0:
            print('The Queue is EMPTY') 
        else:    
            print('\nElement Dequeue is:')  
            print (queue.pop(0))
    elif choice == 3:
        if len (queue) == 0:                       
            print('The Queue is EMPTY') 
        else:
            print("The Size of the Queue is: ",len (queue))         
            print('\nQueue elements are as follows:')            
            for ele in queue:
                print(ele)                  

    elif choice == 4:  
        break   
    else:  
        print("Oops! Incorrect Choice")