from time import sleep

from Process import Process

if __name__ == '__main__':
    
    p1 = Process("0")
    p2 = Process("1")
    p3 = Process("2")

    sleep(60)

    p1.stop()
    p2.stop()
    p3.stop()
