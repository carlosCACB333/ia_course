def print_twice(string, callback):
    print(string)
    print(string)
    callback()


def callback_function():
    print("Callback function called")


if __name__ == '__main__':
    print_twice("Hello", callback_function)
