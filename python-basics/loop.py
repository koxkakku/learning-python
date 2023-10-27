for i in range(1, 1000):
    if i % 10 == 7:
        print(i)

number = 0
result = 0
while number < 100:
    result += number
    number += 1

print(result)

names = ['raju', 'sujit', 'sourav', ' ', 'mahesh']
new_names = []
i = 0
while i < len(names):
    if names[i] != ' ':
        new_names.append(names[i])
    i += 1
print(new_names)
