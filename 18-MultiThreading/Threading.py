# Implementing multithreading using Threading Module

# class Example:
#     def run(self):
#         for i in range(5):
#             print("Hello from Example")

# class ExampleTwo:
#     def run(self):
#         for i in range(5):
#             print("Hello from ExampleTwo")

# eg = Example()
# eg2 = ExampleTwo()
# eg.run()
# eg2.run()

####################################################################################

# from threading import*

# class Example(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hello from Example ")

# class ExampleTwo(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hello from ExampleTwo ")

# eg = Example()
# eg2 = ExampleTwo()
# eg.start()
# eg2.start()

############################################################################################

# using time 
# from threading import*
# from time import sleep

# class ExampleOne(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello from Example One ")
#             sleep(1)

# class ExampleTwo(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello from Example Two ")
#             sleep(1)

# eg = ExampleOne()
# eg2 = ExampleTwo()
# eg.start()
# sleep(0.1)
# eg2.start()

####################################################################################

#using join() method
# from threading import*
# from time import sleep

# class ExampleOne(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello from Example One ")
#             sleep(1)

# class ExampleTwo(Thread):
#     def run(self):
#         for i in range(5):
#             print("Hello from Example Two ")
#             sleep(1)

# eg = ExampleOne()
# eg2 = ExampleTwo()
# eg.start()
# sleep(0.1)
# eg2.start()
# eg.join()
# eg2.join()
# print("End of the program")

#################################################################################

# synchronization - using lock object
from threading import*
import threading
from time import sleep

lock = threading.Lock()
class ExampleOne(Thread):
    def run(self):
        for i in range(5):
            lock.acquire()
            print("lock acquired")
            print("Hello from Example One ")
            sleep(1)
            lock.release()

class ExampleTwo(Thread):
    def run(self):
        for i in range(5):
            lock.acquire()
            print("lock acquired")
            print("Hello from Example Two ")
            sleep(1)
            lock.release()

eg = ExampleOne()
eg2 = ExampleTwo()
eg.start()
sleep(0.1)
eg2.start()