def count(data):
    numb = 0
    try:
        while data[0].count('#') == 0:
            data.pop(0)
        while data[-1].count('#') == 0:
            data.pop()
    except:
        return 0
    for i in data:
        numb +=1
    return numb

def house(plan):
    if '#' not in plan: return 0
    newlist = plan.splitlines()
    newlist = list(filter(None, newlist))
    rotated = list(zip(*newlist[::-1]))

    return (count(newlist)*count(rotated))