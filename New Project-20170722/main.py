import sys
import time

// Define the function
def progbar(wid):
  #for i in range(wid):
    wid += 1
    sys.stdout.write('\r')
    sys.stdout.write('[')
    for a in range (wid):
        sys.stdout.write('#')

    c =100-wid
    for b in range (c):
        sys.stdout.write(' ')

    sys.stdout.write('] ' + str(wid) + '%')
    sys.stdout.flush()
    
// Make the progbar count to 100
for prog in range(100):
    progbar(prog)
    time.sleep(0.05)

print("")
