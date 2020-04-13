import threading

def working():
    print("Um thread working")
    return

thread = []
for i in range(10):
    t = threading.thread