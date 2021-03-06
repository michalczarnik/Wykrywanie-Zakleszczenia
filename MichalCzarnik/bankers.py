def allocate(allocated, maxi, res):
    """Funkcja odpowiedzialna za alokacje zasobow, dzialajaca zgodnie z algorytmem bankiera

    Argumenty:
    allocated - Macierz zasobow posiadanych przez wszystkie watki
    maxi - Macierz zasobow jakie sa potrzebne wszystkim watkom
    res - Wektor zasobow serwera

    Zmienne wyjsciowe:
    0 - Zwracane gdy nie udala sie alokacja srodko (wykryto zakleszczenie)
    1- Zwracane gdy udala sie alokacja srodkow (nie ma zakleszczenia)
    """
    if len(allocated)==1:
        safe=1
        for i in range(len(res)):
            if(res[i]<(maxi[0][i]-allocated[0][i])):
                safe=0
        if safe:
            return 1
        else:
            return 0
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
                print ('Posiadane zasoby: %s'%(res))
                print ('----------\t-------------\t---------------')
                return 1
            else:
                return 0
        else:
            continue
    return 0
