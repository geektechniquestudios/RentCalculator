INSURANCE = 21.73
INTERNET = 100
RENT = 1520
WATER = 28.76


def calc_rent():
    rent_with_utils = float(input("Enter total rent with utils: "))
    power_cost = float(input("Enter the power bill: "))
    utils = rent_with_utils - RENT
    shared_costs = (power_cost + utils + INTERNET + INSURANCE + WATER) / 3
    trell_percent = 520 / 1490
    kirstie_percent = (1.0 - trell_percent) / 2
    kirstie_cost = kirstie_percent * RENT + shared_costs
    trell_cost = trell_percent * RENT + shared_costs
    print(f"Kirstie's share => {kirstie_cost}\n")
    print(f"Trell's share => {trell_cost}")


if __name__ == '__main__':
    calc_rent()
