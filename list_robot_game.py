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
bx = randint( 0, 9 )
by = randint( 0, 9 )

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


 direction = input( ">>>>> " )
 gm[ry][rx] = 0 
 if( direction == "d" ): #>>>>
  rx += 1
 elif( direction == "a" ): #<<<<
  rx -= step
 elif( direction == "s" ): #down
  ry += step
 elif( direction == "w" ): #up
  ry -= step
 gm[ry][rx] = 1

# HW2: optimize movement
# HW3: check for bomb
# ######################### 

