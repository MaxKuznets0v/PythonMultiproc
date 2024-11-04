from settings import TERMINATE_CMD

if __name__ == '__main__':
    while True:
        message = input().strip()
        if message != TERMINATE_CMD:
            print(message)
        else:
            break
