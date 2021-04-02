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

# 2 - BOMB

# #### GAME MAP ##########

gm = [
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 2, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], #trailing comma

]

gm[ry][rx] = 1 #initial robot coord setup

while True:
# #### DRAW THE MAP ########


 system( "clear" )

 print( "#" * 38 )
 for y in range( 10 ):
  for x in range( 10 ):
  
   if( gm[y][x] == 1 ):
    print( " R ", end = " " )
  
   elif( gm[y][x] == 2 ):
    print( " B ", end = " " )
  
   else:
    print( " . ", end = " " )
   
  print( )
  print( )
 print( "#" * 38 )


# ##########################

# #### MOVE ROBOT ##########


 option = input( ">>>> " )
# HW2: optimize movement
# HW3: check for bomb

 if( option == "d" ): #>>>>
  gm[ry][rx] = 0
  rx += 1
  gm[ry][rx] = 1

 elif( option == "a" ): #<<<<
  gm[ry][rx] = 0
  rx -= 1
  gm[ry][rx] = 1

 elif( option == "s" ): # down
  gm[ry][rx] = 0
  ry += 1
  gm[ry][rx] = 1

 elif( option == "w" ): # up
  gm[ry][rx] = 0
  ry -= 1
  gm[ry][rx] = 1

# ######################### 


















