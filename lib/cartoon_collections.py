def roll_call_dwarves(dwarves):
    index= 1
    for name in dwarves:
        print(f"{index}. {name}")
        index +=1

def summon_captain_planet(calls):
    return [i.title()+"!" for i in calls]


def long_planeteer_calls(calls):
    for i in calls:
        if len(i) > 4:
            return True
    return False

def find_the_cheese(foods):
    for i in foods:
        if i == 'gouda' or i=='cheddar' or i=='camembert':
            return i
    return None
