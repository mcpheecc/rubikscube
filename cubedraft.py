import sys
colorlist = 'yrbwog'
faces = {0:'F',1:'U',2:'R',3:'B',4:'D',5:'L'}
def rotatecw(x): #rotates a list 90 degrees clockwise
  return list(map(list,zip(*x[::-1])))
def rotateccw(x): #rotates a list 90 degrees counterclockwise
  return list(map(list,zip(*x)[::-1]))
def getOppositeFace(x): #given a face, returns the opposite face
  x = x+3
  return x%6

def getEdge(x,y,z): #grabs the adjacent sticker of an edge piece given an edge sticker
  m = x%3 #determines which facepair (front/back left/right) etc
  if m==0:
    c=1
    if y==0:
      a=1+x
    elif y==2:
      a=4-x
    elif z==0:
      a=5
    else:
      a=2
    x = x/3
    b = 2-(2*x)
    return [a,b,c]
  if m==1:
    i=x-1
    if y==0:
      a=3
    elif y==2:
      a=0
    elif z==0:
      a=5-i
    else:
      a=2+i
    if i==0:
      if y==1:
        b=1
      elif y==0:
        b=2
      else:
        b=0
    else:
      b=y
    if z==1:
      c=1
    elif z==0:
      c=2
    else:
      c=0
    return [a,b,c]
  if m==2:
    i=x-2
    if y==0:
      a=3
    elif y==2:
      a=0
    elif z==0:
      a=1+i
    else:
      a=4-i
    b=1
    i=i/3
    if i==0:
      if z==2:
        c=0
      else:
        c=2
    else:
      if z==0:
        c=2
      else:
        c=0
    return [a,b,c]
  print('error getting',x,y,z)
  sys.exit()

def getCorner(x,y,z): #gets the next corner sticker in a clockwise orientation
  if x%3==0:
    if y==z:
      if y==2:
        a = 2
      else:
        a = 5
    else:
      if y==0:
        a = 1+x
      else:
        a = 4-x
    x = x/3
    x = 2*x
    b = 2-x
    c = 2-x
    return [a,b,c]
  if x%3==1:
    i = x-1
    if y==z:
      if y==2:
        a = 2+i
      else:
        a = 5-i
    else:
      if y==0:
        a = 3
      else:
        a = 0
    if i==0:
      b = z
      if y==0:
        c = 2
      else:
        c = 0
    else:
      b = y
      if z==0:
        c = 2
      else:
        c = 0
    return [a,b,c]
  if x%3==2:
    i = x-2
    if y==z:
      if y==2:
        a = 4-i
      else:
        a = 1+i
    else:
      if y==0:
        a = 3
      else:
        a = 0
    if i==0:
      if y==z==2:
        b = 2
        c = 0
      else:
        b = 0
        c = 2
    else:
      if y==z==0:
        b = 0
        c = 2
      else:
        b = 2
        c = 0
    return [a,b,c]
  print('could not find piece',x,y,z)
  sys.exit()

class cube():
  def __init__(self,content=[[[i for x in range(3)] for y in range(3)] for i in colorlist]):
    self.content = content
  
  def getEdgePiece(self,a,b): #given two colors returns the coordinates of those pieces such that returnlist[0-2] contains the first color coordinates and returnlist[3-5] contain the second color coordinates
    for i in range(6):
      tryPiece = getEdge(i,0,1)
      if self.content[i][0][1]==a:
        if self.content[tryPiece[0]][tryPiece[1]][tryPiece[2]]==b:
          return [i,0,1]+tryPiece
      if self.content[i][0][1]==b:
        if self.content[tryPiece[0]][tryPiece[1]][tryPiece[2]]==a:
          return tryPiece+[i,0,1]
      tryPiece = getEdge(i,1,0)
      if self.content[i][1][0]==a:
        if self.content[tryPiece[0]][tryPiece[1]][tryPiece[2]]==b:
          return [i,1,0]+tryPiece
      if self.content[i][1][0]==b:
        if self.content[tryPiece[0]][tryPiece[1]][tryPiece[2]]==a:
          return tryPiece+[i,1,0]
      tryPiece = getEdge(i,1,2)
      if self.content[i][1][2]==a:
        if self.content[tryPiece[0]][tryPiece[1]][tryPiece[2]]==b:
          return [i,1,2]+tryPiece
      if self.content[i][1][2]==b:
        if self.content[tryPiece[0]][tryPiece[1]][tryPiece[2]]==a:
          return tryPiece+[i,1,2]
      tryPiece = getEdge(i,2,1)
      if self.content[i][2][1]==a:
        if self.content[tryPiece[0]][tryPiece[1]][tryPiece[2]]==b:
          return [i,2,1]+tryPiece
      if self.content[i][2][1]==b:
        if self.content[tryPiece[0]][tryPiece[1]][tryPiece[2]]==a:
          return tryPiece+[i,2,1]
    return ['error']
  
  def getCornerPiece(self,a,b,c): #given three colors, returns a list of coordinates of that corner piece such that returnlist[0-2] give the first colors coordinates etc  
    for i in range(6):
      for j in (0,2):
        for k in (0,2):
          if self.content[i][j][k]==a:
            i2,j2,k2 = getCorner(i,j,k)
            if self.content[i2][j2][k2]==b:
              i3,j3,k3 = getCorner(i2,j2,k2)
              if self.content[i3][j3][k3]==c:
                return [i,j,k,i2,j2,k2,i3,j3,k3]
            elif self.content[i2][j2][k2]==c:
              i3,j3,k3 = getCorner(i2,j2,k2)
              if self.content[i3][j3][k3]==b:
                return [i,j,k,i3,j3,k3,i2,j2,k2]
          elif self.content[i][j][k]==b:
            i2,j2,k2 = getCorner(i,j,k)
            if self.content[i2][j2][k2]==a:
              i3,j3,k3 = getCorner(i2,j2,k2)
              if self.content[i3][j3][k3]==c:
                return [i2,j2,k2,i,j,k,i3,j3,k3]
            elif self.content[i2][j2][k2]==c:
              i3,j3,k3 = getCorner(i2,j2,k2)
              if self.content[i3][j3][k3]==a:
                return [i3,j3,k3,i,j,k,i2,j2,k2]
          elif self.content[i][j][k]==c:
            i2,j2,k2 = getCorner(i,j,k)
            if self.content[i2][j2][k2]==b:
              i3,j3,k3 = getCorner(i2,j2,k2)
              if self.content[i3][j3][k3]==a:
                return [i3,j3,k3,i2,j2,k2,i,j,k]
            elif self.content[i2][j2][k2]==a:
              i3,j3,k3 = getCorner(i2,j2,k2)
              if self.content[i3][j3][k3]==b:
                return [i2,j2,k2,i3,j3,k3,i,j,k]
    return ['error']
  
  def printCube(self):
    print('Front',self.content[0])
    print('Up',self.content[1])
    print('Right',self.content[2])
    print('Back',self.content[3])
    print('Down',self.content[4])
    print('Left',self.content[5])
  
  def rotateFront(self):
    self.content[0] = rotatecw(self.content[0])
    self.content[1][2], self.content[2][2], self.content[4][2], self.content[5][2] = self.content[5][2], self.content[1][2], self.content[2][2], self.content[4][2]
    print('Rotating front')
  
  def rotateUp(self):
    self.content[1] = rotatecw(self.content[1])
    self.content[5] = rotateccw(self.content[5])
    self.content[3] = rotatecw(rotatecw(self.content[3]))
    self.content[2] = rotatecw(self.content[2])
    self.content[0][0], self.content[5][0], self.content[3][0], self.content[2][0] = self.content[2][0], self.content[0][0], self.content[5][0], self.content[3][0] 
    self.content[5] = rotatecw(self.content[5])
    self.content[3] = rotatecw(rotatecw(self.content[3]))
    self.content[2] = rotateccw(self.content[2])
    print('Rotating up')
  
  def rotateRight(self):
    self.content[2] = rotatecw(self.content[2])
    self.content[0] = rotateccw(self.content[0])
    self.content[1] = rotateccw(self.content[1])
    self.content[3] = rotateccw(self.content[3])
    self.content[4] = rotatecw(self.content[4])
    self.content[0][0], self.content[1][0], self.content[3][0], self.content[4][0] = self.content[4][0], self.content[0][0], self.content[1][0], self.content[3][0]
    self.content[0] = rotatecw(self.content[0])
    self.content[1] = rotatecw(self.content[1])
    self.content[3] = rotatecw(self.content[3])
    self.content[4] = rotateccw(self.content[4])
    print('Rotating right')
  
  def rotateBack(self):
    self.content[3] = rotatecw(self.content[3])
    self.content[4][0], self.content[2][0], self.content[1][0], self.content[5][0] = self.content[5][0], self.content[4][0], self.content[2][0], self.content[1][0]
    print('Rotating back')
  
  def rotateDown(self):
    self.content[4] = rotatecw(self.content[4])
    self.content[5] = rotateccw(self.content[5])
    self.content[2] = rotatecw(self.content[2])
    self.content[3] = rotatecw(rotatecw(self.content[3]))
    self.content[5][2], self.content[0][2], self.content[2][2], self.content[3][2] = self.content[3][2], self.content[5][2], self.content[0][2], self.content[2][2]
    self.content[5] = rotatecw(self.content[5])
    self.content[2] = rotateccw(self.content[2])
    self.content[3] = rotatecw(rotatecw(self.content[3]))
    print('Rotating down')
  
  def rotateLeft(self):
    self.content[5] = rotatecw(self.content[5])
    self.content[3] = rotateccw(self.content[3])
    self.content[1] = rotateccw(self.content[1])
    self.content[0] = rotateccw(self.content[0])
    self.content[4] = rotatecw(self.content[4])
    self.content[3][2], self.content[1][2], self.content[0][2], self.content[4][2] = self.content[4][2], self.content[3][2], self.content[1][2], self.content[0][2]
    self.content[3] = rotatecw(self.content[3])
    self.content[1] = rotatecw(self.content[1])
    self.content[0] = rotatecw(self.content[0])
    self.content[4] = rotateccw(self.content[4])
    print('Rotating left')
  
  def runAlgorithm(self,s):
    for i in s:
      if i=='F':
        self.rotateFront()
      if i=='U':
        self.rotateUp()
      if i=='R':
        self.rotateRight()
      if i=='B':
        self.rotateBack()
      if i=='D':
        self.rotateDown()
      if i=='L':
        self.rotateLeft()
  
  def solve(self):
    #Step 1, solving the edgepieces in the bottom layer
    print('bottom cross')
    colors = {'y':0,'b':2,'w':3,'g':5}
    for i in colors:
      if debug:
        print('solving for o',i)
        self.checkCube()
      nextPiece = self.getEdgePiece('o',i)
      if nextPiece[0]==4: #case1-4 piece is in bottom layer and twisted correctly
        if nextPiece[3]==colors[i]: #case 1 piece is solved
          if debug:
            print('case1')
        else: #case2-4 piece is in the bottom layer but needs to be moved to the right position
          x = faces[nextPiece[3]]
          y = faces[colors[i]]
          self.runAlgorithm(x+x)
          nextPiece = self.getEdgePiece('o',i)
          count = 0
          while nextPiece[3]!=colors[i]:
            self.rotateUp()
            nextPiece = self.getEdgePiece('o',i)
            count = count + 1
            if(count==5):
              sys.exit()
          self.runAlgorithm(y+y)
          if debug:
            print('case3-4')
      elif nextPiece[3]==4: #case5-8 piece is in bottom layer and twisted wrong
        if nextPiece[0]==colors[i]:
          self.runAlgorithm(faces[colors[i]])
          nextPiece = self.getEdgePiece('o',i)
          x = faces[nextPiece[3]]
          y = faces[colors[i]]
          stack = x + x + x + 'UUU' + x + y + y
          self.runAlgorithm(stack)
          if debug:
            print('case5') #case5 piece is in the right position but oriented wrong
        else:
          self.runAlgorithm(faces[nextPiece[0]])
          nextPiece = self.getEdgePiece('o',i)
          x = faces[nextPiece[3]]
          stack = x + x + x + 'U' + x
          self.runAlgorithm(stack)
          nextPiece = self.getEdgePiece('o',i)
          count = 0 
          while (nextPiece[3]!=colors[i]):
            self.rotateUp()
            nextPiece = self.getEdgePiece('o',i)
            count = count + 1
            if(count==5): #debugging
              print('case6-8 broken')
              sys.exit()
          x = faces[colors[i]]
          self.runAlgorithm(x+x)
          if debug:
            print('case6-8')
      elif nextPiece[3]==colors[i]: #case 9-11 piece is in edgeface twisted correctly
        count = 0 
        while(nextPiece[0]!=4):
          self.runAlgorithm(faces[colors[i]])
          nextPiece = self.getEdgePiece('o',i)
          count = count + 1
          if(count==5):
            print('case9-11 broken')
            sys.exit()
        if debug:
          print('case9-11')
      elif nextPiece[0]==colors[i]: #case 12-14 piece is in edgeface and twisted wrong
        if nextPiece[3]!=1: #this forces case 13 and 14 into case 12
          count = 0
          while(nextPiece[3]!=1):
            self.runAlgorithm(faces[colors[i]])
            nextPiece = self.getEdgePiece('o',i)
            count = count + 1
            if(count==5):
              print('case12-14 broken')
              sys.exit()
        self.rotateUp()
        nextPiece = self.getEdgePiece('o',i)
        x = faces[nextPiece[0]]
        y = faces[colors[i]]
        stack = x + y + x + x + x + y + y
        self.runAlgorithm(stack)
        if debug:
          print('case12-14')
      elif nextPiece[0]==getOppositeFace(colors[i]): #case 15-17 piece is opposite of edgeface with cross color touching center piece
        if nextPiece[3]!=1:
          count = 0
          while(nextPiece[3]!=1):#this forces case 16 and and 17 into case 15
            self.runAlgorithm(faces[getOppositeFace(colors[i])])
            nextPiece = self.getEdgePiece('o',i)
            count = count + 1
            if(count==5):
              print('case15-17 broken')
              sys.exit()
          x = faces[getOppositeFace(colors[i])]
          if count==1:
            self.runAlgorithm('U'+x+x+x)
          else:
            self.runAlgorithm('U'+x)
        else:
          self.rotateUp()
        nextPiece = self.getEdgePiece('o',i)
        x = faces[nextPiece[0]]
        y = faces[colors[i]]
        stack = x + x + x + y + x
        self.runAlgorithm(stack)
        if debug:
          print('case15-17')
      elif nextPiece[3]==getOppositeFace(colors[i]): #case 18-20 piece is in opposite of edgeface with edgecolor touching centerpiece
        if nextPiece[0]!=1:
          count = 0
          while(nextPiece[0]!=1):
            self.runAlgorithm(faces[getOppositeFace(colors[i])])
            nextPiece = self.getEdgePiece('o',i)
            count = count + 1
            if(count==5):
              print('case18-20 broken')
              sys.exit()
          x = faces[getOppositeFace(colors[i])]
          if count==1:
            stack = 'U' + x + x + x
          else:
            stack = 'U' + x
          self.runAlgorithm(stack)
        else:
          self.rotateUp()
        self.rotateUp()
        self.runAlgorithm(faces[colors[i]]+faces[colors[i]])
        if debug:
          print('case18-20')
      elif nextPiece[0]==1: #case 21-22 piece is in top layer twisted correctly
        count = 0
        while(nextPiece[3]!=colors[i]):
          self.rotateUp()
          nextPiece = self.getEdgePiece('o',i)
          count = count + 1
          if(count==5):
            print('case21-22 broken')
            sys.exit()
        self.runAlgorithm(faces[colors[i]]+faces[colors[i]])
        if debug:
          print('case21-22')
      elif nextPiece[3]==1: #case23-24 is in top layer twisted incorrectly
        count = 0
        while(nextPiece[0]!=colors[i]):
          self.rotateUp()
          nextPiece = self.getEdgePiece('o',i)
          count = count + 1
          if(count==5):
            print('case23-24 broken')
            sys.exit()
        self.rotateUp()
        nextPiece = self.getEdgePiece('o',i)
        x = faces[nextPiece[0]]
        y = faces[colors[i]]
        stack = x + y + y + y + x + x + x
        self.runAlgorithm(stack)
        if debug:
          print('case23-24')
      if debug:
        self.checkCube()
        
    #Step 2 solving the corner pieces in the bottom layer    
    print('bottom corners')
    cornerpair = [('y','b'),('g','y'),('w','g'),('b','w')]
    for k in range(4):
      i,j = cornerpair[k]
      if debug:
        print('solving for o',i,j,nextPiece)
        self.checkCube()
      nextPiece = self.getCornerPiece('o',i,j)
      if nextPiece[0]==4: #case1-4 corner is in the bottom layer and twisted correctly
        if nextPiece[3]==colors[i] and nextPiece[6]==colors[j]:
          if debug:
            print('case1') #corner is in the right place
        else: #corner is in an adjacent corner position
          x = faces[nextPiece[6]]
          self.runAlgorithm(x + 'U' + x + x + x)
          nextPiece = self.getCornerPiece('o',i,j)
          count = 0
          while(nextPiece[0]!=colors[i]):
            self.rotateUp()
            nextPiece = self.getCornerPiece('o',i,j)
            count = count + 1
            if(count==5):
              print('case2-3 broken')
              sys.exit()
          nextPiece = self.getCornerPiece('o',i,j)
          x = faces[nextPiece[0]]
          stack = x + x + x +'UUU' + x
          self.runAlgorithm(stack)
          if debug:
            print('case2-3')
      elif nextPiece[6]==4: #case5-8 corner is on the bottom layer but twisted cw
        x = faces[nextPiece[0]]
        self.runAlgorithm(x + x + x + 'UUU' + x)
        nextPiece = self.getCornerPiece('o',i,j)
        count = 0
        while(nextPiece[6]!=colors[j]):
          self.rotateUp()
          nextPiece = self.getCornerPiece('o',i,j)
          count = count + 1
          if(count==5):
            print('case5-8 broken')
            sys.exit()
        nextPiece = self.getCornerPiece('o',i,j)
        x = faces[nextPiece[0]]
        self.runAlgorithm(x + x + x +'UUU' + x)
        if debug:
          print('case5-8')
      elif nextPiece[3]==4: #case9-12 corner is on the bottom layer but twisted ccw
        x = faces[nextPiece[0]]
        self.runAlgorithm(x + 'U' + x + x + x)
        nextPiece = self.getCornerPiece('o',i,j)
        count = 0
        while(nextPiece[3]!=colors[i]):
          self.rotateUp()
          nextPiece = self.getCornerPiece('o',i,j)
          count = count + 1
          if(count==5):
            print('case9-12 broken')
            sys.exit()
        nextPiece = self.getCornerPiece('o',i,j)
        x = faces[nextPiece[0]]
        self.runAlgorithm(x + 'U' + x + x +x)
        if debug:
          print('case9-12')
      elif nextPiece[0]==1: #case13-16 corner is in top layer with crosscolor facing up
        count = 0
        while(nextPiece[3]!=colors[j]):
          self.rotateUp()
          nextPiece = self.getCornerPiece('o',i,j)
          count = count + 1
          if(count==5):
            print('case13-16 broken')
            sys.exit()
        nextPiece = self.getCornerPiece('o',i,j)
        x = faces[nextPiece[3]]
        self.runAlgorithm(x + 'UU' + x + x + x + 'UUU' + x + 'U' + x + x + x)
        if debug:
          print('case13-16')
      elif nextPiece[3]==1: #case17-20: corner is in the top layer twisted cw
        count = 0
        while(nextPiece[0]!=colors[i]):
          self.rotateUp()
          nextPiece = self.getCornerPiece('o',i,j)
          count = count + 1
          if(count==5):
            print('case17-20 is broken')
            sys.exit()
        nextPiece = self.getCornerPiece('o',i,j)
        x = faces[nextPiece[0]]
        self.runAlgorithm(x + x + x + 'UUU' + x)
        if debug:
          print('case17-20')
      elif nextPiece[6]==1: #case21-24 corner is in the top layer twisted ccw
        count = 0
        print(nextPiece)
        while(nextPiece[0]!=colors[j]):
          self.rotateUp()
          nextPiece = self.getCornerPiece('o',i,j)
          count = count + 1
          if(count==5):
            print('case21-24 is broken')
            sys.exit()
        nextPiece = self.getCornerPiece('o',i,j)
        print(nextPiece)
        x = faces[nextPiece[0]]
        self.runAlgorithm(x + 'U' + x + x +x)
        if debug:
          print('case21-24')
      if debug:
        self.checkCube()
        
    #Step 3 solving the edge pieces in the middle layer
    print('middle layer')
    color1 = {'y':0,'w':3}
    color2 = {'b':2,'g':5}
    for i in color1:
      for j in color2:
        nextPiece = self.getEdgePiece(i,j)
        if debug:
          self.checkCube()
          print('solving for',i,colors[i],j,colors[j],'piece',nextPiece)
        if nextPiece[0]==colors[i] and nextPiece[3]==colors[j]:
          if debug:
            print('case1') #edge piece is already solved
        else:
          if not(nextPiece[0]==1 or nextPiece[3]==1): 
            #edgepiece is in the wrong spot or twisted
            x = faces[nextPiece[0]]
            count  = 0
            while(nextPiece[3]!=1):
              self.runAlgorithm(x)
              nextPiece = self.getEdgePiece(i,j)
              count = count + 1
              if(count==5):
                print('pop out algorithm 1 broken')
                sys.exit()
            for num in range(count):
              self.rotateUp()
            for num in range(4-count):
              self.runAlgorithm(x)
            nextPiece = self.getEdgePiece(i,j)
            x = faces[nextPiece[0]]
            for num in range(4-count):
              self.rotateUp()
            for num in range(4-count):
              self.runAlgorithm(x)
            for num in range(4-count):
              self.rotateUp()
            for num in range(count):
              self.runAlgorithm(x)
          nextPiece = self.getEdgePiece(i,j) #now edgepiece is in the top layer (if it wasn't already) and can be placed in using a similar algorithm  
          if nextPiece[0]==1:
            a,b = i,j
          else:
            a,b = j,i
          nextPiece = self.getEdgePiece(a,b) #guarentees that color1 is in top layer
          count = 0
          while(nextPiece[3]!=colors[b]):
            self.rotateUp()
            nextPiece = self.getEdgePiece(a,b)
            count = count + 1
            if(count==5):
              print('pop in algorithm broken')
              sys.exit()
          count = 0
          while(nextPiece[3]!=getOppositeFace(colors[a])):
            self.rotateUp()
            nextPiece = self.getEdgePiece(a,b)
            count = count + 1
            if(count==5):
              print('pop in algorithm broken')
              sys.exit()
          x = faces[colors[a]]
          y = faces[colors[b]]
          for num in range(count):
            self.runAlgorithm(x)
          for num in range(4-count):
            self.rotateUp()
          for num in range(4-count):
            self.runAlgorithm(x)
          for num in range(4-count):
            self.rotateUp()
          for num in range(4-count):
            self.runAlgorithm(y)
          for num in range(count):
            self.rotateUp()
          for num in range(count):
            self.runAlgorithm(y)
        if debug:
          self.checkCube()
          
    #Step 4 orienting the edge pieces in the top layer      
    print('orient top cross')
    count = 0
    for i in colors:
      nextPiece = self.getEdgePiece('r',i)
      if(nextPiece[0]==1):
        count = count + 1
    if debug:
      self.checkCube()
      self.printCube()
    if count==0:
      self.runAlgorithm('FRURRRUUUFFFUUFURUUURRRFFF')
      if debug:
        print('case1')
    elif count==2:
      count = 0
      while(self.content[1][1][2]!='r'):
        self.rotateUp()
        count =  count + 1
        if(count==5):
          print('topcross1 broken')
          sys.exit()
      if self.content[1][1][0]=='r':
        self.runAlgorithm('FRURRRUUUFFF')
        if debug:
          print('case2')
      else:
        if self.content[1][2][1]=='r':
          self.rotateUp()
          self.rotateUp()
        else:
          self.rotateUp()
          self.rotateUp()
          self.rotateUp()
        self.runAlgorithm('FURUUURRRFFF')
        if debug:
          print('case3')
    else:
      if debug:
        print('case4') #cross is already solved
    count = 0
    for i in colors:
      nextPiece = self.getEdgePiece('r',i)
      if(nextPiece[0]==1):
        count = count + 1
    if debug:
      self.checkCube()
      
    #Step 5 orienting the corner pieces in the top layer
    print('orient top corners')
    count = 0
    for i in (0,2):
      for j in (0,2):
        if self.content[1][i][j]=='r':
          count = count + 1
    if debug:
      self.checkCube()
    if count==4:
      if debug:
        print('case1')
    elif count==0:
      if debug:
        print('case2-3')
      count = 0
      while(self.content[0][0][0]!='r'):
        self.rotateUp()
        count = count + 1
        if(count==5):
          sys.exit()
      if self.content[0][0][2]=='r':
        if self.content[3][2][0]=='r':  
          self.runAlgorithm('RUURRRUUURURRRUUURUUURRR')
        else:
          self.runAlgorithm('URUURRUUURRUUURRUUR')
      else:
        self.runAlgorithm('UURUURRUUURRUUURRUUR')
    elif count==1:
      if debug:
        print('case4-5')
      count = 0
      while(self.content[1][2][0]!='r'):
        self.rotateUp()
        count = count + 1
        if(count==5):
          sys.exit()
      if self.content[0][0][2]=='r':
        self.runAlgorithm('RURRRURUURRR')
      else:
        self.runAlgorithm('UUULLLUUULUUULLLUUL')
    else:
      count = 0 
      while(self.content[1][0][0]!='r'):
        self.rotateUp()
        count = count + 1
        if(count==5):
          sys.exit()
      if self.content[1][2][2]=='r':
        if self.content[0][0][0]!='r':
          self.rotateUp()
          self.rotateUp()
        self.runAlgorithm('RRRFRBBBRRRFFFRB')
        if debug:
          print('case6')
      else:
        if self.content[1][0][2]!='r':
          self.rotateUp()
        if self.content[0][0][0]=='r':
          self.runAlgorithm('RRDRRRUURDDDRRRUURRR')
        else:
          self.runAlgorithm('RURRRURUURRRUURUURRUUURRUUURRUUR')
        if debug:
          print('case7-8')
    if debug:
      self.checkCube()
      
    #Step 6 permuting the corner pieces in the top layer
    print('permute corners')
    count = 0
    while((self.content[0][0][0]!=self.content[0][0][2])&(count<4)):
      self.rotateUp()
      count = count + 1
      if count==5:
        print('permute corners broken')
        sys.exit()
    if debug:
      self.checkCube()
      test.printCube()
      print(count)
    if count<4:
      if self.content[3][2][0]==self.content[3][2][2]:
        if debug:
          print('case1')
      else:
        self.runAlgorithm('UUURUUULLLURRRUULUUULLLUUL')
        if debug:
          print('case2')
    else:
      self.runAlgorithm('RUUULLLURRRUULUUULLLUULUURUUULLLURRRUULUUULLLUUL')
    if debug:
      self.checkCube()
      
    #Step 7 permuting the edge pieces in the top layer
    print('permute edges')
    if debug:
      self.checkCube()
      self.printCube()
    nextPiece = self.getCornerPiece('y','g','r')
    count = 0
    while(nextPiece[0]!=0):
      self.rotateUp()
      nextPiece = self.getCornerPiece('y','g','r')
      count = count + 1
      if(count==5):
        sys.exit()
    count = 0
    for i in colors:
      nextPiece = self.getEdgePiece('r',i)
      if nextPiece[3]==colors[i]:
        count = count + 1
    if count==4:
      if debug:
        print('case1')
    elif count==1:
      count2 = 0
      while(self.content[0][0][0]!=self.content[0][0][1]):
        self.rotateUp()
        count2 = count2 + 1
        if(count2==5):
          sys.exit()
      if self.content[3][2][1]==self.content[2][0][0]:
        self.runAlgorithm('UURRURURRRUUURRRUUURRRURRR')
      else:
        self.runAlgorithm('UURUUURURURUUURRRUUURR')
      if debug:
        print('case2-3')
    else:
      if self.content[0][0][1]=='w':
        self.runAlgorithm('RRURURRRUUURRRUUURRRURRRUUURRURURRRUUURRRUUURRRURRR')
        if debug:
          print('case3')
      elif self.content[0][0][1]=='b':
        self.runAlgorithm('RUUURURURUUURRRUUURRUUURUUURURURUUURRRUUURR')
        if debug:
          print('case4')
      else:
        self.runAlgorithm('RRURURRRUUURRRUUURRRURRRURRURURRRUUURRRUUURRRURRR')
        if debug:
          print('case5')
    count = 0
    while(self.content[0][0][0]!='y'):
      self.rotateUp()
      count = count + 1
      if(count==5):
        sys.exit()
    self.checkCube()
    
  def checkCube(self): #checks the progress of the cube, stopping at the first incomplete step
    count = 0
    color1 = {'y':0,'w':3}
    color2 = {'b':2,'g':5}
    colors = {'y':0,'b':2,'w':3,'g':5}
    for i in colors:
      nextPiece = self.getEdgePiece('o',i)
      if nextPiece[0]==4:
        if nextPiece[3]==colors[i]:
          count = count + 1
    if count!=4:
      print('bottom cross',count,'pieces correct')
      return
    count = 0
    for i in color1:
      for j in color2:
        nextPiece = self.getCornerPiece('o',i,j)
        if nextPiece[0]==4:
          if nextPiece[3]==color1[i]:
            if nextPiece[6]==color2[j]:
              count = count + 1
    if count!=4:
      print('bottom corners',count,'pieces correct')
      return
    count = 0
    for i in color1:
      for j in color2:
        nextPiece = self.getEdgePiece(i,j)
        if nextPiece[0]==color1[i] and nextPiece[3]==color2[j]:
          count = count + 1
    if count!=4:
      print('middle layer',count,'pieces done')
      return
    count = 0
    for i in [(0,1),(1,0),(1,2),(2,1)]:
      if self.content[1][i[0]][i[1]]=='r':
        count = count + 1
    if count!=4:
      print('top cross',count,'pieces done')
      return
    count = 0
    for i in (0,2):
      for j in (0,2):
        if self.content[1][i][j]=='r':
          count = count + 1
    if count!=4:
      print('top corners',count,'pieces done')
      return
    if not(self.content[0][0][0]==self.content[0][0][2] and self.content[2][0][0]==self.content[2][2][0]):
      print('top corners not permuted')
      return
    if not(self.content[0][0][0]==self.content[0][0][1] and self.content[2][0][0]==self.content[2][1][0]):
      print('top edges not permuted')
      return
    if self.content[0][0][0]=='y':
      print('cube solved')
      return
    print('error cube should be solved')
scramble = 'RFFFRDDDFLLRRUBDDDUUBDDDRRUUDDLLLUUBBBFFRRRLFFDDDFFF'
debug = False
#debug = True
test = cube()
test.runAlgorithm(scramble)
test.solve()
test.printCube()