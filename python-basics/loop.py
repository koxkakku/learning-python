# vegetable and quantity provided sequentially in input.
# store vegetable and its total quantity as a dict.
vegetable = input()
veg_price_dict = {}
while vegetable != 'stop':
    quantity = int(input())
    if vegetable in veg_price_dict.keys():
        veg_price_dict[vegetable] += quantity
    else:
        veg_price_dict[vegetable] = quantity
    vegetable = input()
for key, value in veg_price_dict.items():
    print(f'{key}->{value}')

# count of characters except space in string
test_string = 'Sharad Kumar Dutta'
char_dict = {}
for ch in test_string:
    if ch == " ":
        continue
    elif ch in char_dict.keys():
        char_dict[ch] += 1
    else:
        char_dict[ch] = 1
for key, value in char_dict.items():
    print(f'{key} -> {value}')

# print a table of given factor and count
factor = int(input())
count = int(input())
table = []
for i in range(1, count+1):
    table.append(i*factor)
print(table)

# print sum of numbers upto 100
sum = 0
for num in range(1, 101):
    sum += num
print(sum)

# print a pyramid of numbers for a given input number
n = int(input())
current = 1
for row in range(1, n+1):
    for col in range(1, row+1):
        if current > n:
            break
        print(str(current) + " ", end=" ")
        current += 1
    print()
    if current > n:
        break

# create a list of string from an existing list with all the empty entries being skipped
names = ["India", "China", "", "Afghanistan", "", "Sri Lanka"]
new_list = []
for name in names:
    if name != "":
        new_list.append(name)
print(new_list)

# print all the numbers ending with 7 upto 1000
for num in range(1,1001):
    if num % 10 == 7:
        print(num)
