letter = str(input("Enter a letter:"))
find_letter = (input("What letter are you looking for?"))

count = 0
for ch in letter:
    if ch == find_letter:
        count = count + 1
        #print(count)
print ("There is", count, find_letter, "in letter.")
    
