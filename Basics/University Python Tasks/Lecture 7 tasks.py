from random import randint
import time
import math

print("First Task")
time.sleep(0.5)


def recursion(number, sum):
    if number > 0:
        sum += number
        number -= 1
        recursion(number, sum)
    else:
        return list_of_sums.append(sum)


input_number = int(input("Enter a number which you want to find the sum of the factorials of: "))
time.sleep(1.5)
list_of_sums = []
list_of_the_numbers = []
while input_number > 0:
    recursion(input_number, 0)
    list_of_the_numbers.append(input_number)
    input_number -= 1
result_dictionary = dict(zip(list_of_the_numbers, list_of_sums))
for key, value in result_dictionary.items():
    print(f'Number: {key}, Factorial: {value}.')
    time.sleep(0.2)
time.sleep(1)
print("___________________________")
print(f'The sum of all factorials is: {sum(list_of_sums)}.')
print("___________________________")

time.sleep(3)
print("Second task")


def sum_of_list_elements(current_index_of_the_list, sum, list_of_elements):
    if current_index_of_the_list > -1:
        current_number = list_of_elements[current_index_of_the_list]
        sum += current_number
        current_index_of_the_list -= 1
        sum_of_list_elements(current_index_of_the_list, sum, list_of_elements)
    else:
        result.append(sum)

result = []
list_of_elements = []
number_of_list_elements = randint(5, 10)
for i in range(0, number_of_list_elements):
    current_generated_number = randint(1, 100)
    list_of_elements.append(current_generated_number)

sum_of_list_elements((number_of_list_elements - 1), 0, list_of_elements)
list_of_elements = [str(number) for number in list_of_elements]

print(f'The program generated these numbers: {" ".join(list_of_elements)}')
time.sleep(1.5)
print(f'The average value, calculated using a recursion is: {result[0] / number_of_list_elements:.2f}.')
print("___________________________")

time.sleep(3)
print("Third task")

coordinates_file = open("coordinates.txt", "w")
coordinates_file.write("Sofia: 42.69751;23.32415;|Eindhoven: 37.774929;-122.419416\n")
coordinates_file.write("Santorini: 36.393154;25.461510;|Valencia: 39.466667;-0.375000\n")
coordinates_file.write("Palermo: 38.116669;13.366667;|Rio de Janeiro: -22.908333;-43.196388")

coordinates_file = open("coordinates.txt", "r")
coordinates_file = coordinates_file.readlines()
r = 6371  # radius of the Earth in kilometers
for line in coordinates_file:
    line = line.split("|")
    first_half = line[0].split(": ")
    second_half = line[1].split(": ")

    location1 = first_half[0]
    first_half = first_half[1].split(";")
    lat1 = float(first_half[0])  # latitude of point 1 in degrees
    lon1 = float(first_half[1])  # longitude of point 1 in degrees

    location2 = second_half[0]
    second_half = second_half[1].split(";")
    lat2 = float(second_half[0])  # latitude of point 2 in degrees
    lon2 = float(second_half[1])  # longitude of point 2 in degrees

    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    lon1_rad = math.radians(lon1)
    lon2_rad = math.radians(lon2)

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c
    time.sleep(0.8)
    print(f'First location: {location1}; Latitude: {lat1}; Longitude: {lon1}')
    time.sleep(0.8)
    print(f'Second location: {location2}; Latitude: {lat2}; Longitude: {lon2}')
    time.sleep(0.8)
    print(f'The distance between {location1} and {location2} is: {d}')
    time.sleep(0.4)
    print("___________________________")
