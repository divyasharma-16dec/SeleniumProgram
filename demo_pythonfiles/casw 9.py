# while loop: Use for retrieve mechanism.
# Retrieve =  Click login button > check weather home page appear or not. > Loop should stop.
# if home page is not appeared = we need to again continue to while loop.

a=0
while a<10:
    print(a)  # if below condition is not there, loop wil infinite.
    a=a+1  # We need to add one condition to stop the execution. (Here It will stop the execution.)

for x in range(1,20):
    if x == 5:
        continue
    else:
        print(x)