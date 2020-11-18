import time
if __name__=="__main__":
    while True:
        char=input("char to repeat:\n")
        try:
            while True:
                print(char)
                time.sleep(2)
        except KeyboardInterrupt:
            print("You pressed CTRL+C")
            continue
