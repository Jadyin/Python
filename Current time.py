#Code tells the current date and time
#By Jakob Delaney

import datetime

now = datetime.datetime.now
print("The current date is ")
print(now.strftime("%m/%d/%Y, %H:%M:%S"))
