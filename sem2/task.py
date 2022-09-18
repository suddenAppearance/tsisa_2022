from sqlalchemy import select, func, text

from main import session, Product, CompanyRequirement, UserSelect

i = 2

selected_str = session.execute(
    select(UserSelect.selected_company).filter(UserSelect.name == "Кузоватов")
).one_or_none()[0]

print(selected_str)
selected = list(map(lambda s: int(s), selected_str.split(", ")))
print(selected)

matrix = session.execute(text(f"select * from make_balance_table(ARRAY[{selected_str}])")).all()[1:]

x = {int(i[0].split(";")[0]): list(map(lambda s: {int(s)}, i[0].split(";")[1:])) for i in matrix}

print("-----------BALANCE TABLE:--------------")
print(f"   |{' '.join(f'{i:<7}' for i in x.keys())}")
print("_" * (4 + len(x.keys()) * 7))
for key, value in x.items():
    print(f"{key:<2} |{' '.join(f'{i:<7}' for i in value)}")

a = {[0] * len(x.keys())}
for i, value in x.keys():
    for j in value:
        a[i][j] = x[i][j] / sum(x[j])


print("-----------BALANCE TABLE:--------------")
print(f"   |{' '.join(f'{i:<7}' for i in x.keys())}")
print("_" * (4 + len(x.keys()) * 7))
for key, value in x.items():
    print(f"{key:<2} |{' '.join(f'{i:<7}' for i in value)}")

session.close()
