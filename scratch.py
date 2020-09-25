with open('data/poe_eval.txt', 'r', encoding='utf8') as set:
    count = 0
    for line in set:
        count += len(line.split())
    print(count)


