#1
count = int(input("please enter qunatuty number of how many numbers do you want: "))


number = []


for i in range(count):


     num = int(input("lease enter number" + str(i+1) + ":"))

number.append(num)
print(number)

print(len(number))



#2
start = int(input("Enter start number: "))
end = int("Enter end number: ")

numbers = []

for i in range(start, end):
       numbers.append(i)

print(numbers)


print(max(numbers))
print(min(numbers))
print(sum(numbers))

#3
numbers = []

for i in range(1, 10):
     numbers.append(i)
print(numbers)
print(len(numbers))














































