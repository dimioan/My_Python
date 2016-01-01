

scores = []
scores.append([12, 16, 11, 12])
scores.append([9])
scores.append([6, 9, 11, 14, 17, 15, 14, 20])

print '-'*10
print '\n',scores,'\n'
print '-'*10

for p in range(len(scores)):
    for g in range(len(scores[p])):
        score = scores[p][g]
        print '%4d' % score
    print
    
