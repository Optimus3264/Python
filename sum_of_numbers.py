s='asb10is2m4d'
total=0
current=''

for char in s:
    if char.isdigit():
        current +=char
    else:
        if current:
            total +=int(current)
            current=""

if current:
    total +=int(current)

print(total)