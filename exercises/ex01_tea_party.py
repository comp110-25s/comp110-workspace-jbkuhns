"""The goal of this program is to have multiple inputs through functions calculating how many people can attend the tea party"""

__author__: str = "730745570"


def main_planner(guests: int) -> None:
    """This function combines the tea_bags, treats
    and cost functions together into one main function"""
    print("A Cozy Tea Party for 2 People!")
    tea_count = tea_bags(people=guests)
    print(f"Tea Bags: {tea_count}")
    treat_count = treats(people=guests)
    print(f"Treats needed: {treat_count}")
    total_cost = cost(tea_count=tea_count, treat_count=treat_count)
    print(f"Total cost: ${total_cost:.2f}")
    return None


def tea_bags(people: int) -> int:
    """You input the amount of people and it returns your value as an integer"""
    return people * 2


def treats(people: int) -> int:
    """The amount of tea bags you need will be multiplied by 1.5
    and that's the amount of treats each person gets"""
    teas = tea_bags(people=people)
    return int(teas * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """The total cost for all the tea bags and treats"""
    tea_cost = tea_count * 0.50
    treat_cost = treat_count * 0.75
    return tea_cost + treat_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
