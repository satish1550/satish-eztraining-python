import time
def countdown(t):
    while t:
        mins,secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer)
        time.sleep(1)
        t-=1
    print("Finished")
t = int(input("Enter the time in seconds :"))
countdown(int(t))