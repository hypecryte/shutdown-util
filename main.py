import os, re, time


def cancel_shutdown():
    print("Shutdown is canceled")
    os.system("shutdown -a")
    time.sleep(5)


# if __name__ == "__main__":
#     main()
