try:
    print(10/0)
    try:
        print(len(None))
    except Exception as ex:
        print(ex)
except Exception as ex:
    print(ex)

