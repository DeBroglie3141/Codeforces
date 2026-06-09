y = int(input())
a = True
new_y = y

while a:
    new_y += 1
    l = len(str(new_y))
    nb_c_diff = len(set(str(new_y)))
    if l == nb_c_diff:
        a = False
        print(new_y)
