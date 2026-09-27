"""Interactive finance tracker built while learning Python."""


def calculate_net_profit(revenue, expense):
    return revenue - expense


again = "ha"

while again == "ha":
    number_of_days = int(input("Necha kunlik ma'lumot kiritasiz: "))
    total_profit = 0

    for day in range(1, number_of_days + 1):
        revenue = float(input(f"{day}-kun daromadini kiriting: "))
        expense = float(input(f"{day}-kun xarajatini kiriting: "))

        daily_profit = calculate_net_profit(revenue, expense)
        total_profit = total_profit + daily_profit

        print(f"{day}-kun sof foydasi:", round(daily_profit), "so'm")

    print("Jami sof foyda:", round(total_profit), "so'm")
    again = input("Yana hisoblashni xohlaysizmi? ha/yo'q: ")

print("Dastur tugadi.")
