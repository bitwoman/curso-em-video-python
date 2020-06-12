# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
list_numbers = []

for x in range(0,3):
  numbers = int(input('Enter three numbers: '))
  list_numbers.append(numbers)

#bigger
if list_numbers[0] > list_numbers[1] and list_numbers[0] > list_numbers[2]:
  bigger = list_numbers[0]
elif list_numbers[1] > list_numbers[0] and list_numbers[1] > list_numbers[2]:
  bigger = list_numbers[1]
elif list_numbers[2] > list_numbers[0] and list_numbers[2] > list_numbers[1]:
  bigger = list_numbers[2]

#small
if list_numbers[0] < list_numbers[1] and list_numbers[0] < list_numbers[2]:
  smaller = list_numbers[0]
elif list_numbers[1] < list_numbers[0] and list_numbers[1] < list_numbers[2]:
  smaller = list_numbers[1]
elif list_numbers[2] < list_numbers[0] and list_numbers[2] < list_numbers[1]:
  smaller = list_numbers[2]

# or short way:
# bigger = max(list_numbers)
# small = min(list_numbers)

print(bigger, smaller)
