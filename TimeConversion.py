import sys


time = raw_input().split(':')
if 'PM' in time[2]:
    if time[0]=='12': print time[0]+':'+time[1]+':'+time[2][0:2]
    else: print str(int(time[0])+12)+':'+time[1]+':'+time[2][0:2]
elif 'AM' in time[2]:
    if time[0]=='12': print '00:'+time[1]+':'+time[2][0:2]
    else:print time[0]+':'+time[1]+':'+time[2][0:2]
