text="Mary had a little lamb, Its fleece was white as snow (or black as coal)."
count=0
count1=0
for char in text:
    if char.isupper():
        count=count+1
    count1=count1+1
print(count,count1)