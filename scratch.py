with open('data/poe_validset.txt', 'r') as set:
    count = 0
    for line in set:
        count += len(line.split())
    print(count)


