from time import gmtime, strftime
from time import sleep


def main():
    print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
    
    for i in range (10,0, -1):
        print(i)
        sleep(1)
    print('HORA DO EVENTO')

if __name__ == '__main__':
    main()