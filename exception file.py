try:
    f=open("demo.txt")
    try:
        f.write("Manjusha")
    except:
        print("something went wrong")
    finally:
        f.close()
except:
    print("somthing went wrong when open the file")