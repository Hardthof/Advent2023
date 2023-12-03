digits = {'one': '1',
          'two': '2',
          'three': '3',
          'four': '4',
          'five': '5',
          'six': '6',
          'seven': '7',
          'eight': '8',
          'nine': '9',
          }

def getNumber(s):
    a = '0'
    b = '0'
    for i in range(len(s)):
        if s[i].isdigit():
            a = s[i]
        else:
            for key in digits.keys():
                if s[i:].startswith(key):
                    a = digits[key]
                    break
        if a != '0': break
    
    s = ''.join(reversed(s))
    for i in range(len(s)):
        if s[i].isdigit():
            b = s[i]
        else:
            for key in digits.keys():
                if s[i:].startswith(''.join(reversed(key))):
                    b = digits[key]
                    break
        if b != '0': break

    print(a, b)

    return int(a + b)


if __name__ == '__main__':

    f = open('Day1.txt', mode='r')
    seq = [line.strip() for line in f]
    print(sum([getNumber(s) for s in seq]))