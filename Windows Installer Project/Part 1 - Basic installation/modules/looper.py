def looper(func, fail_msg):
    while True:
        flag = func()
        if flag == True:
            break
        
        else:
            print(fail_msg)
        