def enqueue(queue,item):
    queue.append(item)
    print(item,"added to queue")


def display(queue):
    print("QEUEUE IS->")
    print(queue)

def dequeue(queue):
    print(queue.pop(0),"item deleted from queue")



def main():
    queue=[]
    while True:
        print("Enter 1 for enqueue")
        print("Enter 2 for Dequeue")
        print("Enter 3 for display")
        print("Enter 4 for exit")
        choice=int(input("Enter your choice"))

        if choice==1:
            item=int(input("Enter the item to be added"))
            enqueue(queue,item)

        if choice==2:
            dequeue(queue)

        if choice==3:
            display(queue)




if __name__=="__main__":
    main()
