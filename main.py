def merge(*lists):
    lists2 = []

    for i in range(len(lists)):
        lists2 += lists[i]
    
    lists2.sort()
    return lists2
