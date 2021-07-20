items = [('avacado',2.2,170),('pamelo',8,1500),('durian',22,1500),('cucamelon,',0.26,15),('lychee',0.4,20)]

def greedy_fruit(items,capacity):
    items = sorted(items,key=lambda item:item[1],reverse=True)
    chosen_fruits = {}
    profit = 0
    for i in range(len(items)):
        name,value,weight = items[i]
        num_of_fruits = (capacity - capacity % weight)/weight
        chosen_fruits[name] = num_of_fruits
        capacity = capacity%weight
        profit += num_of_fruits*value
    return round(profit,2),chosen_fruits


def greedy_fruit_dantzig(items,capacity):
    items = sorted(items,key=lambda item:item[1]/item[2],reverse=True)
    chosen_fruits = {}
    profit = 0
    for i in range(len(items)):
        name,value,weight = items[i]
        num_of_fruits = (capacity - capacity % weight)/weight
        chosen_fruits[name] = num_of_fruits
        capacity = capacity%weight
        profit += num_of_fruits*value
    return round(profit,2),chosen_fruits
    #     print()
print(greedy_fruit(items,2000))
print(greedy_fruit_dantzig(items,2000))
