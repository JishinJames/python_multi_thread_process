import multiprocessing
import time as t

#print(multiprocessing.cpu_count())

def calc_square(number):
    print(number*number)

def quad(number):
    print(number*number*number*number)

if __name__ == "__main__":
    number=7
    print(multiprocessing.cpu_count())

    start = t.time()
    process1 = multiprocessing.Process(target=calc_square,args=(number,))
    process2 = multiprocessing.Process(target=quad,args=(number,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    end = t.time()

    print(f"Time : {end - start}")
