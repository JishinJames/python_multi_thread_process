import threading
import time as t

def calc_square( number):
    print(number*number)

def quad(number):
    print(number*number*number*number)

if __name__ == "__main__":
    number =7
    print()

start = t.time()
thread1 = threading.Thread(target=calc_square,args=(number,))
thread2 = threading.Thread(target=quad,args=(number,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = t.time()

print(f"Time : {end - start}")

#print(thread2)
