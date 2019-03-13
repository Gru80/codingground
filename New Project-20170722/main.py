# Importing things are done here
import sys
import time

# Define the function
def progbar(wid):
  #for i in range(wid):
    wid += 1
    sys.stdout.write('\r')
    sys.stdout.write('[')
    for _ in range (wid):
        sys.stdout.write('#')

    c =100-wid
    for _ in range (c):
        sys.stdout.write(' ')

    sys.stdout.write('] ' + str(wid) + '%')
    # flush it all out
    sys.stdout.flush()

# Make the progbar count to 100
for prog in range(100):
    progbar(prog)
    time.sleep(0.05)

# We just print an empty line here
print("")

# End of file
# Really - nothing else is comming up next
