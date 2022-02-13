import time
def countdown (t):
    while  t>0:
        print (t)
        t = t - 1
        time.sleep(1)
        RED = '\033[31m'
        BLUE = '\033[44m'
        STYLE = '\033[1m'
    print ( RED + BLUE + STYLE + "HAPPY TERMUX LIFE!Save The virtual!")

print ("How Many Seconds To Count Down? Please, Enter An Integer")
seconds = input ()
while not seconds.isdigit ():
    print ("That Wasn't An Integer Number! Please,Enter An Integer")
    seconds = input ()
seconds = int (seconds)
countdown (seconds)
