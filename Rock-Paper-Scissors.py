import random

print("""
    
    ***************************************

    
    Rock Paper Scissors! 

    For Rock - 1, For Scissors - 2 , For Paper - 3 Enter the number you chose! . 

    Good Luck !!


    ***************************************
    """)

values= {1:"Rock",2:"Scissors",3:"Paper"}

def Rock_Paper_Scissors(value):
    computer = random.randint(1,3)
    if value ==  computer:
        print(f"""
        
            It ended in a draw...

            I choosed {values[computer]} , And you did {values[value]} .

            Wanna try again ? 
        
              """)
    elif value < computer:
        print(f"""
        
            You win !! 

            I did {values[computer]} , And you did {values[value]} .

            The defeated wrestler is insatiable for wrestling; how about playing again? !
             
        """)
    elif  value >= 4 or value <= 0:
            print("""
        
        I think you writed it wrong. 
        
        Try Again ...

        """)
    else:
            print(f"""
        
            You lose ! 

            I did {values[computer]}, And you did {values[value]}.
            
            Wanna try again ?
            
                  """)
myvalue=input("Enter your value: ")
if(myvalue.isnumeric()):      
        Rock_Paper_Scissors(int(myvalue))