######################  SIMPLE TIC TAC TOE #########################

import random
q=0

# whole program in loop to exit whenever player is no more interested

while q==0:
  
  # STEP 1: choice of X or O
  
  print(".............HI BUDDY LETS SEE WHO WINS.................")
  print("..................U wanna chose X or O....................")
  letter=input()
  if letter=='x' or letter=='X':
    opponent = "O" 
    letter='X'
  elif letter=='o' or letter=='O':
    opponent='X'
    letter='O'
  else:
    print('Type only X or O')
    print('Do u wanna play again if yes press 1 or else press 0')
    try:
        choice = int(input())
    except ValueError:
        print('Invalid input! Assuming you do not want to play again.')
        choice = 0
    if choice == 1:
        continue
    else:
        break

  # STEP 2: defining the matrix
  
  grid=['0',' ',' ',' ',' ',' ',' ',' ',' ',' ']
  def grids():
    print('                       %c | %c | %c ' %(grid[1],grid[2],grid[3]))
    print('                      ___|___|___')
    print('                       %c | %c | %c ' %(grid[4],grid[5],grid[6]))
    print('                      ___|___|___')
    print('                       %c | %c | %c ' %(grid[7],grid[8],grid[9]))
    print('                      ___|___|___')
    
  # STEP 3: defining all possible winning conditions
  
  def win():
    if ((grid[1]==letter and grid[2]==letter and grid[3]==letter) or (grid[4]==letter and grid[5]==letter and grid[6]==letter) or (grid[7]==letter and grid[8]==letter and grid[9]==letter) or 
  (grid[1]==letter and grid[4]==letter and grid[7]==letter) or (grid[2]==letter and grid[5]==letter and grid[8]==letter) or (grid[3]==letter and grid[6]==letter and grid[9]==letter) or (grid[1]==letter and grid[5]==letter and grid[9]==letter) or (grid[3]==letter and grid[5]==letter and grid[7]==letter)):
      return(1)
    elif ((grid[1]==opponent and grid[2]==opponent and grid[3]==opponent) or (grid[4]==opponent and grid[5]==opponent and grid[6]==opponent) or (grid[7]==opponent and grid[8]==opponent and grid[9]==opponent) or 
  (grid[1]==opponent and grid[4]==opponent and grid[7]==opponent) or (grid[2]==opponent and grid[5]==opponent and grid[8]==opponent) or (grid[3]==opponent and grid[6]==opponent and grid[9]==opponent) or (grid[1]==opponent and grid[5]==opponent and grid[9]==opponent) or (grid[3]==opponent and grid[5]==opponent and grid[7]==opponent)):
      return(2)
    else:
      return(0)

  # STEP 4: Algo to oppose the player by unsatisifying the winning conditions
  
  def opp():
    if len(unoccupied)==8:
      return random.choice(unoccupied)
    a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=0
    flag=0
    s=[]

    # Checking if computer can win in next move
    if ((1 in opposite and 2 in opposite) or (2 in opposite and 3 in opposite) or (1 in opposite and 3 in opposite)):
       a=set([1,2,3]).difference(opposite)
       if len(a)==1:
        s.append(a) 
    if ((4 in opposite and 5 in opposite) or (5 in opposite and 6 in opposite) or (4 in opposite and 6 in opposite)):
       b=set([4,5,6]).difference(opposite) 
       if len(b)==1:
         s.append(b)
    if ((7 in opposite and 8 in opposite) or (8 in opposite and 9 in opposite) or (7 in opposite and 9 in opposite)):
       c=set([7,8,9]).difference(opposite)
       if len(c)==1:
         s.append(c)
    if ((1 in opposite and 4 in opposite) or (4 in opposite and 7 in opposite) or (1 in opposite and 7 in opposite)):
       d=set([1,4,7]).difference(opposite)
       if len(d)==1:
         s.append(d)
    if ((2 in opposite and 5 in opposite) or (5 in opposite and 8 in opposite) or (2 in opposite and 8 in opposite)):
       e=set([2,5,8]).difference(opposite)
       if len(e)==1:
         s.append(e)
    if ((3 in opposite and 6 in opposite) or (6 in opposite and 9 in opposite) or (3 in opposite and 9 in opposite)):
       f=set([3,6,9]).difference(opposite)
       if len(f)==1:
         s.append(f)
    if ((1 in opposite and 5 in opposite) or (5 in opposite and 9 in opposite) or (1 in opposite and 9 in opposite)):
       g=set([1,5,9]).difference(opposite)
       if len(g)==1:
         s.append(g)
    if ((3 in opposite and 5 in opposite) or (5 in opposite and 7 in opposite) or (3 in opposite and 7 in opposite)):
       h=set([3,5,7]).difference(opposite) 
       if len(h)==1:
         s.append(h)

    # Checking if player is about to win and block them
    if ((1 in occupied and 2 in occupied) or (2 in occupied and 3 in occupied) or (1 in occupied and 3 in occupied)):
       i=set([1,2,3]).difference(occupied)
       if len(i)==1:
        s.append(i) 
    if ((4 in occupied and 5 in occupied) or (5 in occupied and 6 in occupied) or (4 in occupied and 6 in occupied)):
       j=set([4,5,6]).difference(occupied) 
       if len(j)==1:
         s.append(j)
    if ((7 in occupied and 8 in occupied) or (8 in occupied and 9 in occupied) or (7 in occupied and 9 in occupied)):
       k=set([7,8,9]).difference(occupied)
       if len(k)==1:
         s.append(k)
    if ((1 in occupied and 4 in occupied) or (4 in occupied and 7 in occupied) or (1 in occupied and 7 in occupied)):
       l=set([1,4,7]).difference(occupied)
       if len(l)==1:
         s.append(l)
    if ((2 in occupied and 5 in occupied) or (5 in occupied and 8 in occupied) or (2 in occupied and 8 in occupied)):
       m=set([2,5,8]).difference(occupied)
       if len(m)==1:
          s.append(m)
    if ((3 in occupied and 6 in occupied) or (6 in occupied and 9 in occupied) or (3 in occupied and 9 in occupied)):
       n=set([3,6,9]).difference(occupied)
       if len(n)==1:
         s.append(n)
    if ((1 in occupied and 5 in occupied) or (5 in occupied and 9 in occupied) or (1 in occupied and 9 in occupied)):
       o=set([1,5,9]).difference(occupied)
       if len(o)==1:
         s.append(o)
    if ((3 in occupied and 5 in occupied) or (5 in occupied and 7 in occupied) or (3 in occupied and 7 in occupied)):
       p=set([3,5,7]).difference(occupied) 
       if len(p)==1:
         s.append(p)
  
    for i in s:
       if list(i)[0] not in opposite and list(i)[0] in unoccupied:
           return list(i)[0]
       
    return random.choice(unoccupied) 
   
    
  place_no=0
  unoccupied=[1,2,3,4,5,6,7,8,9]
  occupied=[]
  opposite=[]
  
  # STEP 5: all together
  
  while(win() !=3):

    if (win() == 1):
        grids()
        print('..................YOU WON :) ..............................')
        print('Do u wanna play again? Press 1 for Yes, 0 for No:')
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input! Assuming you do not want to play again.")
            choice = 0
        if choice == 1:
            break
        else:
            q = 1
        break

    if (win() == 2):
        grids()
        print('................YOU LOST :( ..............................')
        print('Do u wanna play again? Press 1 for Yes, 0 for No:')
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input! Assuming you do not want to play again.")
            choice = 0
        if choice == 1:
            break
        else:
            q = 1
        break

    grids()
    print('enter the position you wanna place your %c (1-9): ' % (letter))
    try:
        place_no = int(input())
    except ValueError:
        print("Please enter a valid number between 1 and 9")
        continue  # ask again

    if place_no < 1 or place_no > 9:
        print("Invalid position! Enter number between 1 and 9.")
        continue

    if place_no in occupied or place_no in opposite:
        print('U cant occupy an occupied place')
        print('Do u wanna play again? Press 1 for Yes, 0 for No:')
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input! Assuming you do not want to play again.")
            choice = 0
        if choice == 1:
            break
        else:
            q = 1
        break

    occupied.append(place_no)
    occupied.sort()
    grid[place_no] = letter

    if len(unoccupied) == 1:
        win()
        if (win() == 1):
            grids()
            print('................YOU WON :) ..............................')
            print('Do u wanna play again? Press 1 for Yes, 0 for No:')
            try:
                choice = int(input())
            except ValueError:
                print("Invalid input! Assuming you do not want to play again.")
                choice = 0
            if choice == 1:
                break
            else:
                q = 1
            break
        if (win() == 2):
            grids()
            print('................YOU LOST :( ..............................')
            print('Do u wanna play again? Press 1 for Yes, 0 for No:')
            try:
                choice = int(input())
            except ValueError:
                print("Invalid input! Assuming you do not want to play again.")
                choice = 0
            if choice == 1:
                break
            else:
                q = 1
            break

    unoccupied.remove(place_no)

    if len(unoccupied) == 0:
        grids()
        print("....................ITS A DRAW :| ...........................")
        print('Do u wanna play again? Press 1 for Yes, 0 for No:')
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input! Assuming you do not want to play again.")
            choice = 0
        if choice == 1:
            break
        else:
            q = 1
        break

    r = opp()
    grid[r] = opponent
    unoccupied.remove(r)
    opposite.append(r)

