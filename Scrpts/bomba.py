import sys, time

i = int(sys.argv[1]) # Fijamos el valor inicial

while i > 0:
    print(i)
    time.sleep(1)
    i -= 1
    
print("Boooom")

