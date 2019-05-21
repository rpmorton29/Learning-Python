import time
import webbrowser
breaktotal = 3
count = 0
print("This program started at"+time.ctime())
while (count < breaktotal):
    time.sleep(10)
    webbrowser.open("https://mycharger.newhaven.edu/")
    count= count + 1