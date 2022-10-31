def openFile():
    try:
        f1 = open('data.txt', 'r')
        while True:
            data = f1.readlines()
            print(data)
            if data[0] != '':
                return data
            elif data[0] != '':
                break
        f1.close()
    except IOError:
        print(IOError.with_traceback())

def dateMonth():
    data2 = openFile()
    size = len(data2)
    data1 = ['31', '12', '1900']
    for i in range(0, size,1):
        n = data2[i].split('-')[0]
        print(n)
        if int(n) < int(data1[0]):
            data1[0] = n
        n = data2[i].split('-')[1]
        if int(n) < int(data1[1]):
            data1[1] = n
    print(data1[0], "-", data1[1])


dateMonth()