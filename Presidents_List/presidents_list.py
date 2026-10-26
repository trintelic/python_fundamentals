print("List of 10 Presidents Following George Washington's Presidency")
print(
    "List of presidencies between 1797-1849, including first name, "
    "last name, and term."
)
print(
    "Asterisks are next to presidents that have a last name starting with "
    "an A when program is ran."
)

presidents = [
    ["John Adams", "1797-1801"],
    ["Thomas Jefferson", "1801-1809"],
    ["James Madison", "1809-1817"],
    ["James Monroe", "1817-1825"],
    ["John Quincy Adams", "1825-1829"],
    ["Andrew Jackson", "1829-1837"],
    ["Martin Van Buren", "1837-1841"],
    ["William Henry Harrison", "1841-1841"],
    ["John Tyler", "1841-1845"],
    ["James K. Polk", "1845-1849"],
]

print("Name and Term using a For loop")
print("********************************************")
for president in presidents:
    name = president[0]
    term = president[1]
    last_name = name.split()[-1]

    if last_name.startswith("A"):
        print(name + "* - " + term)
    else:
        print(name + " - " + term)

print("U.S. Presidents - While Loop")
print("********************************************")
index = 0

while index < 10:
    name = presidents[index][0]
    term = presidents[index][1]
    last_name = name.split()[-1]

    if last_name.startswith("A"):
        print(name + "* - " + term)
    else:
        print(name + " - " + term)

    index = index + 1
