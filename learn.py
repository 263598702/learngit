import time
import cProfile

def computeChicken():
    x,y=1,1
    start=time.clock()
    while x<=20:
        while y<=33:
            z=100-x-y
            if z%3==0 and (x*5+y*3+z//3)==100:
                print(' %d %d %d' %(x,y,z))
            y+=1
        y=1
        x+=1
    end=time.clock()

    print(end-start)

def computeChicken2(): 
    start=time.clock()
    for x in range(0,21,4): 
        for y in range(25,3,-7):
            z=100-x-y
            if z%3==0 and (x*5+y*3+z//3)==100 and x>0:
                print(' %d %d %d' %(x,y,z))
            y+=1
        
        y=1
        x+=1
    end=time.clock()
    print(end-start)
            

        
if __name__=='__main__':
    computeChicken2()


