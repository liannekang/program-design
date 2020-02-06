a = "weeord"

count = {}

for letter in a:
    if letter not in count.keys():
        count[letter] = 1
    else:
        count[letter] += 1
        
print(count)