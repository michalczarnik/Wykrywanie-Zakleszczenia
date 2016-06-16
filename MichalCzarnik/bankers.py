def allocate(allocated, maxi, res):
    if len(allocated)==1:
        safe=1
        for i in range(len(res)):
            if(res[i]<(maxi[0][i]-allocated[0][i])):
                safe=0
        if safe:
            return 1
        else:
            return 0
    ###LENGTH is not 1. So you should try all permutations.
    for p in range(len(allocated)):
        safe = 1
        for i in range(len(allocated[p])):
            if res[i]<(maxi[p][i]-allocated[p][i]):
                safe=0
        if safe:
            new_allocated=allocated[:p]+allocated[p+1:]
            new_maxi=maxi[:p]+maxi[p+1:]
            new_res = res[:]
            new_res=[res[i]+allocated[p][i] for i in range(len(res))]
            if allocate(new_allocated, new_maxi, new_res):
                print ('maximum: \n%s'%('\n'.join([' '.join([str(item) for item in row]) for row in maxi])))
                print ('allocated: \n%s'%('\n'.join([' '.join([str(item) for item in row]) for row in allocated])))
                print ('resources in hand: %s'%(res))
                print ('Allocated %s to %s'%([maxi[p][i]-allocated[p][i] for i in range(len(maxi[p]))], p))
                print ('----------------------------------------------')
                print ('----------------------------------------------')
                return 1
            else:
                return 0
        else:
            continue
    return 0