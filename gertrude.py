import printimg

while True:
    try:
        code = int(input())
        printimg.printimg(code)
    except Exception:
        pass   
