from os import listdir


base_url='/data/images'

def test():
    listOfData = listdir('./images')   
    for data in listOfData:
        formatFile = data.split('.')[-1]
        if formatFile == 'jpg':
            with open('train.txt', 'a') as f:
                f.write(base_url + data + '\n')
                

if __name__ == '__main__':
    test()
