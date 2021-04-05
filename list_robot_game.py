#!/usr/bin/env Python3

##########################

from os import system
from random import randint

###########################
# GAME MAP 10 x 10

#LEGEND:
# 0 - ENPTY
# 1 - ROBOT
rx = randint( 0, 9 )
ry = randint( 0, 9 )

# 2 -BOMB
bx = 5
by = 5

#3 -HP
hpx = randint( 0, 9 )
hpy = randint( 0, 9 )



# #### GAME MAP ##########

gm = [
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], #trailing comma

]

gm[ry][rx]   = 1 #initial robot coord setup
gm[bx][by]   = 2
gm[hpx][hpy] = 3

def draw_map():

 system( "clear" )

 print( "#" * 38 )
 for y in range( 10 ):
  for x in range( 10 ):
  
   if( gm[y][x] == 1 ):
    print( " R ", end = " " )
  
   elif( gm[y][x] == 2 ):
    print( " B ", end = " " )
  
   elif(gm[y][x] == 3 ):
    print( " H ", end = " " )

   else:
    print( " . ", end = " " )
   
  print( )
  print( )
 print( "#" * 38 )


while True:
 
 step = 1
 draw_map()
 
 if( ry == by and rx == bx ):
     print( "BOOOM! GAME OVER!" )
     break
# code doesn't work. I see it later
# if( ry == hpy and rx == hpx ):
#    print( "GREAT!!!" )
#     input( "hit ENTER to continue" )



 direction = input( ">>>>> " )
  
 gm[ry][rx] = 0 
 
 if( direction == "d" ): #>>>>
  if( rx < 9 ):
   rx += 1
  else:
   print( "You cant't move here" )
   input(" hit ENTER to continue" )
 
 elif( direction == "a" ): #<<<<
  if( rx > 0 ):
   rx -= step
  else:
   print( "You cant't move here" )
   input(" hit ENTER to continue" )
 
 elif( direction == "s" ): #down
  if( ry < 9 ):
   ry += step
  else:
   print( "You cant't move here" )
   input(" hit ENTER to continue" )
 
 elif( direction == "w" ): #up
  if( ry > 0):
   ry -= step
  else:
   print( "You cant't move here" )
   input(" hit ENTER to continue" )
 
 gm[ry][rx] = 1
 
 if( direction == "x" ):
  system( "clear")
  print("Thank you for playing!")
  break
# ######################### 

