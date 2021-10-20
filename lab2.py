#Câu 1
kingdoms = ['Bacteria', 'Protozoa', 'Chromista',
'Plantaee', 'Fungi','Animaliaa']
print("kingdoms: ", kingdoms)
#1a
print("kingdoms[0] : ", kingdoms[0])
#1b
print("kingdoms[5] : ", kingdoms[5])
#1c
print("kingdoms[:3]: ", kingdoms[:3])
#1d
print("kingdoms[2:5]: ", kingdoms[2:5])
#1e 
print("kingdoms[4:]: ", kingdoms[4:])
#1f
print("kingdoms[1:0]: ", kingdoms[1:0])
# Câu 2
#2a
print("kingdoms[-6]: ", kingdoms[-6])
#2b
print("kingdoms[-1]: ", kingdoms[-1])
#2c
print("kingdoms[-6:-3]: ", kingdoms[-6:-3])
#2d
print("kingdoms[-4:-1]: ", kingdoms[-4:-1])
#2e
print("kingdoms[-2:]: ", kingdoms[-2:])
#2f
print("kingdoms[-1:-2]: ", kingdoms[-1:-2])
print("--------/////--------")
# Câu 3 
#3 Create list of appointments:
appointments = ['9:20', '10:30', '14:00', '15:00', 
'15:30']
print(appointments)
#3a Add them 16:20 to the end of the list
appointments.append('16:30')
print(appointments)
#3b Use the + operator to add '16:30' 
appointments += ['16:30']
print(appointments)
#3c The approach in (a) modifies the list. 
#3c The one in (b) creates a new list.
print("--------/////--------")
# Câu 4 
#4 Create list of ids:
ids = [4353, 2314, 2956, 3382, 9362, 3900]
print(ids)
#4a Remove 3382 from the list. I use remove()
ids.remove(3382)
print(ids)
#4b  Get the index of 9362. I use index()
index_9362 = ids.index(9362)
print('index of 9362: ',index_9362)
#4c Insert 4499 in the list after 9362
ids.insert(index_9362 + 1, 4499)
print('Add 4499 after 9362: ',ids)
#4d Extend the list by adding [5566, 1830] 
ids.extend([5566, 1830])
print('Add 5566, 1830: ',ids)
#4e  Reverse the list.
ids.reverse()
print('Reversed List:', ids)
#4f  Sort the list.
ids.sort()
print('Sorted list: ', ids)
print("--------/////--------")
# Câu 5
#5a a list contains the atomic numbers of the six alkaline earth metals
alkaline_earth_metals = [4, 12, 20, 38, 56, 88]
print('alkaline_earth_metals: ',alkaline_earth_metals)
#5b index contains radium’s atomic number. 2 ways 
positive_index = alkaline_earth_metals[5]
print('index contains radium’s atomic number: ', positive_index)
negative_index = alkaline_earth_metals[-1]
print('index contains radium’s atomic number: ', negative_index)
#5c  how many items there are in alkaline_earth_metals?
print('length of alkaline_earth_metals: ', len(alkaline_earth_metals))
#5d the highest atomic number in alkaline_earth_metals
print('the highest atomic number: ', max(alkaline_earth_metals))
print("--------/////--------")
# Câu 6 
#6a a list of temperatures
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
print('temps: ', temps)
#6b sort temps in ascending order
temps.sort()
print('Sorted temps: ', temps)
#6c Using slicing
cool_temps = temps[0:2]
warm_temps = temps[2:]
print('cool_temps: ',cool_temps)
print('warm_temps: ', warm_temps)
#6d Using list arithmetic
temps_in_celsius = cool_temps + warm_temps
print('temps_in_celsius: ', temps_in_celsius)
print("--------/////--------")
# Câu 7
#7 Return True if and only if first item of the list is the same as the last
def same_first_last(L) :
    return L[0] == L[-1]
print(same_first_last([3, 4, 2, 8, 3]))
print(same_first_last(['apple', 'banana', 'pear']))
print(same_first_last([4.0, 4.5]))
print(same_first_last(['Duong', 'Binh', 'Cuong', 'Duong']))
print("--------/////--------")
# Câu 8 
#8 Return True if and only if the length of L1 is longer than the length of L2
def is_longer(L1, L2):
    return len(L1) > len(L2)
print(is_longer([1, 2, 3], [4, 5]))
print(is_longer(['abcdef'], ['ab', 'cd', 'ef']))
print(is_longer(['a', 'b', 'c'], [1, 2, 3]))
print(is_longer(['Tran Cong Tu'],['Tran','Cong','Tu']))
print("--------/////--------")
# Câu 9 
#9  values = [0,[0,[0,values,2],2],2]
values = [0,1,2]
values[1] = values
print(values)
print("--------/////--------")
# Câu 10 
units =  [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]
print(units)
#10a the first inner list]
print('the first inner list: ', units[0])
#10b the last inner list
print('the last inner list', units[-1])
#10c The string 'km'
print('units[0][0]: ', units[0][0])
#10d The string 'kg'
print('units[1][0]: ',  units[1][0])
#10e The list ['miles', 'league']
print('units[0][1:]: ', units[0][1:])
#10f The list ['kg', 'pound']
print('units[1][0:2]: ', units[1][0:2])
print("--------/////--------")
# Câu 11
#11 Repeat the previous exercise using negative indices.
#11a the first inner list]
print('the first inner list: ', units[-2])
#11b the last inner list
print('the last inner list', units[-1])
#11c The string 'km'
print('units[-2][-3]: ', units[-2][-3])
#11d The string 'kg'
print('units[-1][-3]: ',  units[-1][-3])
#11e The list ['miles', 'league']
print('units[-2][-2:]: ', units[-2][-2:])
#11f The list ['kg', 'pound']
print('units[-1][:-1]: ', units[-1][0:-1])
print("--------/////--------")
# Chương 9
# Câu 1
#1 for loop to print all the values
celegans_phenotypes =  ['Emb','Him', 'Unc', 'Lon', 'Dpy', 'Sma']
print(celegans_phenotypes)
for phenotype in celegans_phenotypes:
    print(phenotype)
print("--------/////--------")
# Câu 2
#2 print all on a single line
half_lives = [87.74, 24110.0, 6537.0, 14.4, 376000.0]
for value in half_lives:
    print(value, end=' ')
print("--------/////--------")
# Câu 3
#3 add values + 1  of whales to more_whales
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
print('whales: ', whales)
more_whales = []
for count in whales:
    more_whales.append(count + 1)
print('more_whales: ', more_whales)
print("--------/////--------")
# Câu 4
#4a Create a nested list 
alkaline_earth_metals = [[4, 9.012], [12, 24.305],
[20, 40.078], [38, 87.62],[56, 137.327], [88, 226]]
print(alkaline_earth_metals)
#4b for loop to print all the values
for element in alkaline_earth_metals:
    print('atomic number: ', element[0])
    print('atomic weight: ', element[1])
    print('')
#4c  not nested
number_and_weight = []
for element in alkaline_earth_metals:
    number_and_weight.append(element[0])
    number_and_weight.append(element[1])
print('number_and_weight: ', number_and_weight)
print("--------/////--------")
# Câu 5
#5  add  a docstring, type annotations, or comments
def mystery_function(values):
    """ Trả về một bản sao có các danh sách con.
    Phần từ trong danh sách con được đảo ngược
    >>> mystery_function([[1,2,3], [4,5,6]])
    [[3,2,1],[4,5,6]
     """
    result = []
    for sublist in values:
        result.append([sublist[0]]) # result = [[1]] 
        for i in sublist[1:]: # lan 1: i = 2,3  / lan 2: i = 5,6  
            result[-1].insert(0, i) 
            # them i vao truoc.
            # Lan 1. result[-1] = [1]
            # Lan 2. result[-1] = [4]
    return result
print( mystery_function([[1, 2, 3], [4, 5, 6]]))
print("--------/////--------")
# Câu 6
#6 type quit (any capitalization) to exit
text = ""
while text.lower() != "quit":
    text = input("Please type quit (any capitalization) to exit: ")
    if text.lower() == "quit":
        print("Exited program")
print("--------/////--------")
# Câu 7 
#7 add the population of the current country to total
country_populations = [1295, 23, 7, 3, 47, 21]
total = 0
for population in country_populations:
    total += population
print('total population = ', total)
print("--------/////--------")
# Câu 8 
#8
rat_1 = [2,1,3,4,7,6,2,3,5,8]
rat_2 = [1,3,2,2,6,8,4,2,2,9]
#8a
if rat_1[0] > rat_2[0]:
    print("Rat 1 weighed more than rat 2 on day 1.")
else:
    print("Rat 1 weighed less than rat 2 on day 1.")
#8b
if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
    print("Rat 1 remained heavier than Rat 2.")
else:
    print("Rat 2 became heavier than Rat 1.")
#8c
if rat_1[0] > rat_2[0]:
    if rat_1[-1] > rat_2[-1]:
        print("Rat 1 remained heavier than Rat 2.")
    else:
        print("Rat 2 became heavier than Rat 1.")
else:
    print("Rat 1 weighed less than rat 2 on day 1.")
print("--------/////--------")
# Câu 9
#9  Print the numbers in the range 33 to 49 (inclusive)
for number in range(33, 50):
    print(number)
print("--------/////--------")
# Câu 10 
#10 Print the numbers from 1 to 10 (inclusive) in descending order, all on one line.
for number in range(10):
    print(10 - number, end=' ')
print('')
print("--------/////--------")
# Câu 11
#11
sum = 0
count = 0
for number in range(2,23):
    sum += number
    count += 1
average = sum / count
print('sum = ', sum)
print('count = ', count)
print('average = ', average)
print("--------/////--------")
# Câu 12
#12 Rewrite the code 
def remove_neg(num_list):
    index = 0
    while index < len(num_list):
        if num_list[index] < 0:
            num_list.remove(num_list[index])
        else:
            index += 1
num_list = [1, 2, 3, -3, 6, -1, -3, 1]
remove_neg(num_list)
print(num_list)


print("--------/////--------")
# Câu 13
#13 a right triangle
for width in range(1, 8):
    print('T' * width)
print("--------/////--------")
# Câu 14
#14 a right triangle with s hypotenuse on the left side
for width in range(1, 8):
    print(' '*(7 - width), 'T'* width) 
    print(' '*(7 - width), 'T'* width)

print("--------/////--------")
# Câu 15
#15 Redo the previous two exercises using while loops instead of for loops.
width1 = 1
while width1 < 8:
    print('T' * width1)
    width1 += 1

width2 = 1
while width2 < 8:
    print(' '*(7 - width2), 'T'*width2)
    width2 += 1

print("--------/////--------")
# Câu 16
rat_1_weight = [2,1,1,4,5,7,2,3,5,8];
rat_2_weight = [2,1,1,4,6,6,4,2,2,9];
#16a how many weeks the weight of the first rat to become 25 percent heavier 
week = 0
while rat_1_weight[week] / rat_1_weight[0] - 1 < .25:
    week += 1
print(week)
#16b  how many weeks it would take for rat 1 to be 10 percent heavier than rat 2
week = 0
while rat_1_weight[week] / rat_2_weight[week] - 1 < .10:
    week += 1
print(week) 
print("--------/////--------")