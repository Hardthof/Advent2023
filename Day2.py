import re

bag = {'red':12, 'green':13, 'blue':14}

def search(s):
    for item in s:
            for key in bag.keys():
                if key in item:
                    if(int(re.findall(r'\d+', item)[0]) > bag[key]):
                         return False
    return True

def calcpower(s):
    red = 0
    blue = 0
    green = 0

    for item in s:
        if 'red' in item: red = max(red, int(re.findall(r'\d+', item)[0]))
        elif 'blue' in item: blue = max(blue, int(re.findall(r'\d+', item)[0]))
        elif 'green' in item: green = max(green, int(re.findall(r'\d+', item)[0]))

    return red* blue* green

if __name__ == '__main__':

    f = open('Day2.txt', mode='r')
    seq = [line.split(':')[1].strip() for line in f]
    
    result = 0
    setpower = 0
    for i,s in enumerate(seq):
        ss = s.split(';')
        sss = []
        for k in ([f.split(',') for f in ss]):
            for j in k:
                sss.append(j)
        
        if search(sss): result = result + i + 1
        setpower += calcpower(sss)

    print(result, setpower)