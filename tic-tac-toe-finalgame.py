a1="."
a2="."
a3="."
b1="."
b2="."
b3="."
c1="."
c2="."
c3="."
#STEP-2 Print inital cofiguration
print(a1,"|",a2,"|",a3)
print("--+---+--")
print(b1,"|",b2,"|",b3)
print("--+---+--")
print(c1,"|",c2,"|",c3)
gameover=False

#input of move 1
row1=int(input("Player 1:move 1: enter row(1,2,3)="))
column1=int(input("Player1:move1: enter column(1,2,3)="))
if(row1==1)and(column1==1)  :  
    a1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row1==1)and(column1==2):
    a2="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row1==1)and(column1==3):
    a3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row1==2)and(column1==1):
    b1="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
elif(row1==2)and(column1==2):
    b2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row1==2)and(column1==3):
    b3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row1==3)and(column1==1):
    c1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row1==3)and(column1==2):
    c2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row1==3)and(column1==3):
    c3="O"   
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
#input of move 2    
row2=int(input("Player 2: move 1 : enter row(1,2,3)="))
column2=int(input("Player 2: move 1 : enter colum(1,2,3)="))
if(row2==1)and(column2==1)  :  
    a1="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row2==1)and(column2==2):
    a2="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row2==1)and(column2==3):
    a3="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row2==2)and(column2==1):
    b1="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
elif(row2==2)and(column2==2):
    b2="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row2==2)and(column2==3):
    b3="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row2==3)and(column2==1):
    c1="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row2==3)and(column2==2):
    c2="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row2==3)and(column2==3):
    c3="X"   
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
#input of move 3    
row3=int(input("Player 1:move 2: enter row (1,2,3)="))
column3=int(input("Player 1:move 2: enter column (1,2,3)="))
if(row3==1)and(column3==1)   : 
    a1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row3==1)and(column3==2):
    a2="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row3==1)and(column3==3):
    a3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row3==2)and(column3==1):
    b1="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
elif(row3==2)and(column3==2):
    b2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row3==2)and(column3==3):
    b3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row3==3)and(column3==1):
    c1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row3==3)and(column3==2):
    c2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row3==3)and(column3==3):
    c3="O"   
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)  
#move 4
row4=int(input("Player 2:move 2: enter row (1,2,3)="))
column4=int(input("Player 2:move 2: enter column (1,2,3)="))    
if(row4==1)and(column4==1)   : 
    a1="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row4==1)and(column4==2):
    a2="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row4==1)and(column4==3):
    a3="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row4==2)and(column4==1):
    b1="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
elif(row4==2)and(column4==2):
    b2="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row4==2)and(column4==3):
    b3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row4==3)and(column4==1):
    c1="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row4==3)and(column4==2):
    c2="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row4==3)and(column4==3):
    c3="X"   
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)  
#move 5
row5=int(input("Player 1:move 3:enter row(1,2,3)="))  
column5=int(input("Player1:move 3:enter column(1,2,3)="))  
if(row5==1)and(column5==1)   : 
    a1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row5==1)and(column5==2):
    a2="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row5==1)and(column5==3):
    a3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row5==2)and(column5==1):
    b1="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
elif(row5==2)and(column5==2):
    b2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row5==2)and(column5==3):
    b3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row5==3)and(column5==1):
    c1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row5==3)and(column5==2):
    c2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row5==3)and(column5==3):
    c3="O"   
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
else:
     pass     

if((a1=='O')and(a2=="O")and(a3=="O") ) or ((b1=="O")and(b2=="O")and(b3=="O"))or((c1=="O")and(c2=="O")and(c3=="O"))or((a1=="O")and(b2=="O")and(c3=="O"))or((a3=="O")and (b2=="O")and(c1=="O")) or (a1==b1==c1=="O")or(a2==b2==c2=="O") or (a3==b3==c3=="O"):
  print("PLAYER 1 WINS")
  exit()
 
elif((a1=='X')and(a2=="X")and(a3=="X") ) or ((b1=="X")and(b2=="X")and(b3=="X"))or((c1=="X")and(c2=="X")and(c3=="X"))or((a1=="X")and(b2=="X")and(c3=="X"))or((a3=="X")and (b2=="X")and(c1=="X")) or(a1==b1==c1=="X")or(a2==b2==c2=="X") or(a3==b3==c3=="X"):
        print("PLAYER 2 WINS")
        exit()
else:
     pass         
    
#move 6
row6=int(input("Player 2: move 2: enter row(1,2,3)="))
column6=int(input("Player 2: move 2: enter colum(1,2,3)="))
if(row6==1)and(column6==1)   : 
    a1="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row6==1)and(column6==2):
    a2="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row6==1)and(column6==3):
    a3="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row6==2)and(column6==1):
    b1="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
elif(row6==2)and(column6==2):
    b2="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row6==2)and(column6==3):
    b3="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row6==3)and(column6==1):
    c1="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row6==3)and(column6==2):
    c2="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row6==3)and(column6==3):
    c3="X"   
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
else:
     pass    

if((a1=='O')and(a2=="O")and(a3=="O") ) or ((b1=="O")and(b2=="O")and(b3=="O"))or((c1=="O")and(c2=="O")and(c3=="O"))or((a1=="O")and(b2=="O")and(c3=="O"))or((a3=="O")and (b2=="O")and(c1=="O")) or (a1==b1==c1=="O") or (a2==b2==c2=="O") or (a3==b3==c3=="O"):

                  print("PLAYER 1 WINS")
                  exit()
elif((a1=='X')and(a2=="X")and(a3=="X") ) or ((b1=="X")and(b2=="X")and(b3=="X"))or((c1=="X")and(c2=="X")and(c3=="X"))or((a1=="X")and(b2=="X")and(c3=="X"))or((a3=="X")and (b2=="X")and(c1=="X"))or (a1==b1==c1=="X") or (a2==b2==c2=="X") or (a3==b3==c3=="X"):
         print("PLAYER 2 WINS")
         exit()
else:
     pass         
#move7
row7=int(input("player 1:move 4:enter row(1,2,3)="))         
column7=int(input("player 1:move 4:enter column(1,2,3)="))
if(row7==1)and(column7==1)   : 
    a1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row7==1)and(column7==2):
    a2="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row7==1)and(column7==3):
    a3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row7==2)and(column7==1):
    b1="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
elif(row7==2)and(column7==2):
    b2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row7==2)and(column7==3):
    b3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row7==3)and(column7==1):
    c1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row7==3)and(column7==2):
    c2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row7==3)and(column7==3):
    c3="O"   
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
else:
     pass     

if((a1=='O')and(a2=="O")and(a3=="O") ) or ((b1=="O")and(b2=="O")and(b3=="O"))or((c1=="O")and(c2=="O")and(c3=="O"))or((a1=="O")and(b2=="O")and(c3=="O"))or((a3=="O")and (b2=="O")and(c1=="O")) or (a1==b1==c1=="O") or (a2==b2==c2=="O") or (a3==b3==c3=="O"):

                  print("PLAYER 1 WINS")
                  exit()
elif (a1==b1==c1=="X" )or (a2==b2==c2=="X")or (a3==b3==c3=="X") or(a1==a2==a3=="X")or (b1==b2==b3=="X") or (c1==c2==c3=="X") or (a1==b2==c3=="X") or (a3==b2==c1=="X"):            
         print("PLAYER 2 WINS")
         exit()
else:
     pass         
#move8
row8=int(input("player 2: move 4: enter row (1,2,3)="))
column8=int(input("player 2: move 4: enter column(1,2,3)="))
if(row8==1)and(column8==1)   : 
    a1="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row8==1)and(column8==2):
    a2="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row8==1)and(column8==3):
    a3="x"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row8==2)and(column8==1):
    b1="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
elif(row8==2)and(column8==2):
    b2="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row8==2)and(column8==3):
    b3="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row8==3)and(column8==1):
    c1="X"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row8==3)and(column8==2):
    c2="X" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row8==3)and(column8==3):
    c3="X"   
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
else:
     pass    


if((a1=='O')and(a2=="O")and(a3=="O") ) or ((b1=="O")and(b2=="O")and(b3=="O"))or((c1=="O")and(c2=="O")and(c3=="O"))or((a1=="O")and(b2=="O")and(c3=="O"))or((a3=="O")and (b2=="O")and(c1=="O")) or (a1==b1==c1=="O") or (a2==b2==c2=="O") or (a3==b3==c3=="O"):

                  print("PLAYER 1 WINS")
                  exit()
elif((a1=='X')and(a2=="X")and(a3=="X") ) or ((b1=="X")and(b2=="X")and(b3=="X"))or((c1=="X")and(c2=="X")and(c3=="X"))or((a1=="X")and(b2=="X")and(c3=="X"))or((a3=="X")and (b2=="X")and(c1=="X")) or (a1==b1==c1=="X") or (a2==b2==c2=="X") or (a3==b3==c3=="X"):
         print("PLAYER 2 WINS")
         exit()  
else:
     pass            
#move 9
row9=int(input("Player 1:move 5: enter row (1,2,3)="))         
column9=int(input("Player 1:move 5: enter column (1,2,3)=")) 
if(row9==1)and(column9==1)   : 
    a1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row9==1)and(column9==2):
    a2="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row9==1)and(column9==3):
    a3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row9==2)and(column9==1):
    b1="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
elif(row9==2)and(column9==2):
    b2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row9==2)and(column9==3):
    b3="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row9==3)and(column9==1):
    c1="O"
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row9==3)and(column9==2):
    c2="O" 
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3)
elif(row9==3)and(column9==3):
    c3="O"   
    print(a1,"|",a2,"|",a3)
    print("--+---+--")
    print(b1,"|",b2,"|",b3)
    print("--+---+--")
    print(c1,"|",c2,"|",c3) 
else:
     pass    
if((a1=='O')and(a2=="O")and(a3=="O") ) or ((b1=="O")and(b2=="O")and(b3=="O"))or((c1=="O")and(c2=="O")and(c3=="O"))or((a1=="O")and(b2=="O")and(c3=="O"))or((a3=="O")and (b2=="O")and(c1=="O")) or (a1==b1==c1=="O")or (a2==b2==c2=="O") or (a3==b3==c3=="O"):

                  print("PLAYER 1 WINS")
                  exit()
elif((a1=='X')and(a2=="X")and(a3=="X") ) or ((b1=="X")and(b2=="X")and(b3=="X"))or((c1=="X")and(c2=="X")and(c3=="X"))or((a1=="X")and(b2=="X")and(c3=="X"))or((a3=="X")and (b2=="X")and(c1=="X")) or (a1==b1==c1=="X ")or (a2==b2==c2=="X ") or (a3==b3==c3=="X "):
         print("PLAYER 2 WINS") 
         exit()
else:
     print("GAME DRAW")         