import time

print("\nSleep Function")
class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")
student = Student()
student.take_nap(1)

print("\nTimestamp operations")
timestamp = 1572879180
print(time.ctime(timestamp))
print(time.gmtime(timestamp))
print(time.localtime(timestamp))
st = time.gmtime(timestamp)
print(time.asctime(st)) # Mon Nov  4 14:53:00 2019
print(time.mktime((2021, 5, 23, 20, 53, 0, 0, 308, 0))) # 1621821180.0