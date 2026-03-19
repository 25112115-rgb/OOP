import time
Now = time.time ()
Days = Now // (24 * 3600)
Remaining = Now % (24 * 3600)
Hours = Remaining // 3600
Remaining = Remaining & 3600
Minutes = Remaining // 60
Seconds = Remaining % 60
print ("Days since epoch:", int(Days))
print ("Now is: ", f"{int(Hours):02d}:{int(Minutes):02d}:{int(Seconds):02d}" )
