from euler import *
##l = open('p098_words.txt')
##l = l.read()
##l = l.replace('"','').replace(',', ' ').split()
##ags = set()
##ind = 1
##for i in l:
##    if not ind%100:print(ind)
##    for j in l:
##        if anagrams(i,j) and not i == j:
##            ags.update([i,j])
##    ind+=1
ags = ['SING', 'EAST', 'GARDEN', 'TONE', 'SHOUT',
       'FILE', 'REDUCTION', 'NAME', 'TIME', 'CREDIT',
       'SHUT', 'PHASE', 'COURSE', 'TEA', 'EXCEPT', 'REGION',
       'MEAN', 'MEAL', 'THING', 'DOG', 'ACT', 'RATE', 'MALE',
       'IGNORE', 'OWN', 'WORTH', 'FROM', 'SURE', 'THESE', 'EAT',
       'NOW', 'LEAD', 'QUIET', 'CENTRE', 'USER', 'POST', 'CARE',
       'SIGN', 'DIRECT', 'GOD', 'ITS', 'ON', 'THUS', 'RAISE', 'SIT',
       'STEAL', 'SOURCE', 'LIFE', 'BROAD', 'HOW', 'NOTE', 'LEAST',
       'ITEM', 'RECENT', 'TEAR', 'ARISE', 'SOUTH', 'INTRODUCE',
       'CREATION', 'HEART', 'HATE', 'STOP', 'NO', 'FORMER', 'HEAT',
       'DANGER', 'SEAT', 'CAT', 'SHAPE', 'WHO', 'FORM', 'QUITE',
       'EARN', 'REFORM', 'REACTION', 'SHEET', 'BOARD', 'NIGHT', 'NEAR',
       'EARTH', 'RACE', 'THROW', 'SPOT', 'DEAL', 'EXPECT']
m=0
for i in ags:
    a = int(''.join([str(digitsum(ord(j)-64)) for j in i]))
    if issquare(a) and a>m:
        m=a
print(m)
