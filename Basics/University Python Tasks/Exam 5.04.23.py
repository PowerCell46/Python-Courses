#First task
L = [24,3,5,15,2,2,14,1]
M = L[:]
M.sort(reverse=True)
M = [str(number) for number in M]
print(f'This is the second list - the exact same at the previous, but in order: {" ".join(M)}')
M_odd = [int(number) for ind, number in enumerate(M) if ind % 2 != 0]
print(f'The sum of the numbers in the odd positions in the second list is: {sum(M_odd)}')

#Second task
Lat_degrees = (0, 10, 23.43, 30, 23.43, 66.57, 70, 66.57, 90,90)
Lat_pole = ("S", "S", "N", "N", "S", "S", "N", "N", "N", "S")
s_values = []
n_values = []
for index in range(0, len(Lat_pole)):
    if Lat_pole[index] == "S":
        s_values.append(Lat_degrees[index])
    elif Lat_pole[index] == "N":
        n_values.append(Lat_degrees[index])
Lat_dictionary = {"S": s_values, "N": n_values}
print(Lat_dictionary)
