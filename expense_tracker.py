from expense import Expense


def main():
    file_expense = "expense.csv"

    ex = get_expense_details()
    print(ex)

    save_expense_file(ex, file_expense)

    summarize_expense(file_expense)

    specific_category(file_expense)


def get_expense_details():
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    print(f"Your expense amount is: Rs.{expense_amount:.2f}")

    expense_category = ["Food", "Home", "Work", "Fun"]

    while True:
        print("Expense Categories:")

        for i, category_name in enumerate(expense_category):
            print(f"{i + 1}. {category_name}")

        selected = int(input("Select Category: "))

        if selected in range(1, 5):
            cat = expense_category[selected - 1]

            new_expense = Expense(
                name=expense_name,
                category=cat,
                amount=expense_amount
            )

            return new_expense

        else:
            print("Your input is invalid!!!")


def save_expense_file(ex, file_expense):
    with open(file_expense, "a") as f:
        f.write(f"{ex.name},{ex.category},{ex.amount}\n")


def summarize_expense(file_expense):
    expense = []

    with open(file_expense, "r") as f:
        lines = f.readlines()

    for line in lines:
        strip_line = line.strip()

        if strip_line == "":
            continue

        names, category1, amount1 = strip_line.split(",")

        line_expense = Expense(
            name=names,
            category=category1,
            amount=float(amount1)
        )

        expense.append(line_expense)

    amount = {}

    for ex in expense:
        key = ex.category

        if key in amount:
            amount[key] += ex.amount
        else:
            amount[key] = ex.amount

    print("\nTotal Expenses:")

    for key, am in amount.items():
        print(f"    {key} - Rs.{am:.2f}")


def specific_category(file_expense):
    command = input(
        "\nDo you want to see expenses in category (Y/N): "
    )

    if command.upper() == "Y":

        expense_category = ["Food", "Home", "Work", "Fun"]

        print("\nExpense Categories:")

        for i, category in enumerate(expense_category):
            print(f"{i + 1}. {category}")

        num = int(input("Enter the category number: "))

        if num in range(1, 5):
            selected_category = expense_category[num - 1]

            print(f"\nExpenses under {selected_category}:")

            total = 0
            found = False

            with open(file_expense, "r") as f:
                lines = f.readlines()

            for line in lines:
                if line.strip() == "":
                    continue

                name, category, amount = line.strip().split(",")

                if category == selected_category:
                    print(
                        f"{name} - Rs.{float(amount):.2f}"
                    )

                    total += float(amount)
                    found = True

            if found:
                print(
                    f"Total {selected_category} expense: "
                    f"Rs.{total:.2f}"
                )
            else:
                print(
                    f"No expenses found under {selected_category}."
                )

        else:
            print("Invalid category number.")

    elif command.upper() == "N":
        print("Okay!")

    else:
        print("Invalid input.")


if __name__ == "__main__":
    main()

