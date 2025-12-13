n = 50
was_zero = False
count = 0
done = False
with open('data.txt') as f:
    for line in f.readlines():
        assert not done
        if not line:
            done = True
            continue
        
        # print(line[:-1])
        letter = line[0]
        number = line[1:]
        assert letter == 'R' or letter == 'L'
        R = 1 if (letter == 'R') else -1
        assert number.isdigit

        num = int(number)

        n += (num * R)
        while n < 0:
            n += 100
            if not was_zero:
                count += 1
            else:
                was_zero = False
            # print('\tping')
        while n > 99:
            if n == 100:
                n = 0
                break
            n -= 100
            count += 1
            # print('\tpong')
        
        if n == 0:
            was_zero = True
            count += 1
            # print('\tbong')
        else:
            was_zero = False


        # print(n)
        # if not n:
        #     count += 1

print(count)



