def two_sum(numbers, target):
    end = ''
    for t,tes in enumerate(numbers):
        for c,num in enumerate(numbers):
            if tes + num == target and t != c:
                    print((t,c))
                    end = 'true'
                    break
        if end == 'true':
            break
two_sum([1,2,3], 4)
two_sum([1234,5678,9012], 14690)
two_sum([2,2,3], 4)
