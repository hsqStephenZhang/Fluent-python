def func():
    print("this is function")

    with open("test.txt",'r') as fp:
        # return 1
        print(fp.read())
func()