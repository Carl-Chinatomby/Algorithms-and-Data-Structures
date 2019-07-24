"""Given a Menu with Items and Item Prices
(can use whichever data structure you want) & a totalCost - Find all combinations that add up to a certain price"""

MENU = [
    ('chicken', 7.50),
    ('beef', 12.00),
    ('pork', 13.50),
]


def get_combinations(menu, total_price):
    #Create a matrix
    combinations = [ [0] * (total_price+1) ] * (len(menu+1))
    solutions = []


    for i in range(len(menu)):
        combinations[i][0] = 1

def main():
    get_combinations(MENU, 21.00)



if __name__ == "__main__":
    pass
