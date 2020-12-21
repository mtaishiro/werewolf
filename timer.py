from time import sleep

#definition of time countdown
def timer(max, sectime):

    #maximum time
    max_time = max

    #every second
    sec = sectime

    for i in range (max_time):
        sleep(sec)
##        print("{}seconds passed".format(max_time - i))

print("start discussing")

#5minutes
timer(300, 1)

print("time's up!")



##when you show how many times are left

##5 minutes countdown
##timer(120, 1)
##print("three minutes left")
##timer(120, 1)
##print("one minutes left")
##timer(60, 1)
##print("time's up")
