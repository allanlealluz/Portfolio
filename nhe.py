class RomanNumerals:
    def to_roman(val):
        romans = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        c = 0
        t = []
        maxt = sorted(romans.values())
        maxt2 = sorted(romans.values(),reverse=True)
        roman =  ['I','IV','V','IX','X','L','XC','C','CD','D','CM','M']
        roman2 = ['M','CM','D','CD','C','XC','L','X','IX','V','IV','I']
        count = len(maxt) -1
        while c != val:
            if val >= 1000:
                if maxt2[count] == val:
                    print(roman2[count])
                    break
                elif maxt2[count] < val - c:
                    c += maxt2[count]
                    t.append(roman2[count])
                else:
                    count -= 1
            else:
                if maxt[count] == val:
                    print(roman[count])
                    break
                elif maxt[count] < val - c:
                    c += maxt[count]
                    t.append(roman[count])
                else:
                    count -= 1
        print(t)
RomanNumerals.to_roman(1000)
RomanNumerals.to_roman(1990)
RomanNumerals.to_roman(6)
RomanNumerals.to_roman(4)
RomanNumerals.to_roman(1)