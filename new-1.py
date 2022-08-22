
import os
def currentdir():
    print("Current:"+os.getcwd())

def getos():
    print("Operating System:  "+os.uname()[0])
    print("Version:  "+os.uname()[3])
    print("User:  "+os.uname()[1])
    print("Release:  "+os.uname()[2])
    print("Machine Type:  "+os.uname()[4])

def ls():
    a=os.listdir()
    b=len(os.listdir())
    if(b==0):
        print("Empty Directory")
    else:
        print("Press Given Number to MOve Forward in Directory:")
    
    
    for i in range(0,b):
        print("{i}. {d}".format(i=i+1,d=a[i]))
        # print()

def changedir(a):
    try:
        os.chdir(os.listdir()[int(a)-1])
    except NotADirectoryError or ValueError:
        print("Its a File")


def main():
    while(True):
        getos()
        ls()
        a=input("Enter Corresponding Number or q to quit:")
        if(a=='q'):
            os._exit(0)
        changedir(a)
    


if __name__=='__main__':
    main()
