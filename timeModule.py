import time 

timestamp = int(time.strftime("%H"))

if timestamp >= 5 and timestamp <= 12:
    print("Good Morning\n")

elif timestamp >= 12 and timestamp <= 16:
    print("Good Afternoon\n")

elif timestamp >= 16 and timestamp <= 20:
    print("Good Evening\n")   

else:
    print("Good Night\n")


timestamp = time.strftime("%H:%M:%S")
print(timestamp)


