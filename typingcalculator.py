from time import *
import random as r

def mistake(paragraphtest,usertest):
    error=0
    for i in range(len(paragraphtest)):
        try:
            if paragraphtest != usertest:
             error=error+1
        except:
            error=error+1
    return error

def speed_time(time_start,time_end,userinput):
    time_delay = time_end - time_start
    time_Round =round(time_delay,2)
    speed = len(userinput)/ time_Round
    return round(speed)



test=["Welcome to Github .This is my first minor project.",
      "Nature is made of everything we see around us trees, flowers,etc"]
test1=r.choice(test)
print("      *******Typing speed*******")
print(test1)

print()
print()

time_1=time()
testinput=input("Enter:")
time_2=time()

print('speed: ',speed_time(time_1,time_2,testinput),"w/sec")
print("Error:",mistake(test1,testinput))
