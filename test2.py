
vowels = ["a", "e", "i", "o", "u"]

word = "Hello World!"
count = 0
for i in word:
    for v in vowels:
        if v == i:
            count += 1
print(count)
        