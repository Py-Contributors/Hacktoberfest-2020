def converttime(time):
    if(time[-2:]=='PM'):
        if(time[0:2]!='12'):
            time = str(int(time[0:2])+12)+time[2:8]
        elif(time[0:2]=='12'):
             time = "12"+time[2:8]
    elif(time[-2:]=='AM'):
        if(time[0:2]=='12'):
            time = "00"+time[2:8]
        else:
            time = time[0:8]
    else:
        time = time[0:8]
            
    print(time)
def main():
    s = ["06:40:03AM","10:13:14PM","12:13:14PM","04:13:14AM","09:13:14PM"]
    for time in s:
        converttime(time)
main()
