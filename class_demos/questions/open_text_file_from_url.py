import urllib.request 

url = "http://www.gutenberg.org/files/2147/2147-0.txt"
count = 0
for line in urllib.request.urlopen(url):
    line = line.decode('utf-8')
    words = line.split()
    for word in words:
        if word == "the":
            count += 1
print(count)



