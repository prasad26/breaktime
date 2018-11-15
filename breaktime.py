import time
import webbrowser

total_breaks = 3
break_count = 0

print("The program starts on"+time.ctime())
while (break_count < total_breaks):
    time.sleep(15)
    webbrowser.open("https://www.youtube.com/watch?v=VQ_I7ikMusc")
    break_count = break_count + 1
    
    
