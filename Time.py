import time

minutes = int(input("Enter the number of minutes to focus: "))
seconds = minutes * 60

while seconds:
    mins, secs = divmod(seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up!")
sdsad
dasl;,sdasdadad
sadasdasd
sd
s

s
s
s
sdad
sa
dasd
as
d
ad
a
d
ad
ad
