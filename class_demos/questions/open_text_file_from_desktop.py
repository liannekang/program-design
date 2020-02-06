f = open("/Users/benkiel/Desktop/poe.txt", "r", encoding="utf8",)

count = 0
for line in f:
    words = line.split()
    for word in words:
        if word == "the":
            count += 1
print(count)



