# double = [i*i for i in range(10)]
# print(double)

# იგივეა რაც:

# double = []
# for i in range(10):
#     double.append(i * i)

# print(double)


# def my_gen():
#     n = 1
#     print('This is printed first')
#     yield n
#     n += 1
#     print('This is printed second')
#     yield n

#     n += 1
#     print('This is printed at last')
#     yield n
# a=my_gen()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

#1. შექმენით სია, რომლის ელემენტებია 1-დან 100-მდე არსებული 5-ის ჯერადი რიცხვების კუბები. გამოიყენეთ for ციკლის მოკლე ჩაწერის ფორმა. შესაბამისი ფუნქციის გამოყენებით იპოვეთ სიის მაქსიმალური ელემენტი.
# cubed_multiples_of_5 = [x**3 for x in range(5, 101, 5)]
# print(cubed_multiples_of_5)

#2. წინა მაგალითში არსებული სიისთვის შექმენით იტერატორი და StopIteration შეცდომის გამოსროლამდე
# დაბეჭდეთ სათითაოდ იტერატორის ელემენტები next() ფუნქციის გამოყენებით.
# cubed_multiples_of_5 = []

# for x in range(5, 101, 5):
#     cubed_multiples_of_5.append(x**3)

# print(cubed_multiples_of_5)

# იგივეა რაც

# cubed_multiples_of_5 = [x**3 for x in range(5, 101, 5)]
# iterator = iter(cubed_multiples_of_5)

# while True:
#     try:
#         cube = next(iterator)
#         print(cube)
#     except StopIteration:
#         break

#3. შექმენით სიმრავლე, რომლის ელემენტებია 1-დან 100-მდე არსებული 5-ის ჯერადი რიცხვების კუბები. გამოიყენეთfor ციკლის მოკლე ჩაწერის ფორმა. შესაბამისი ფუნქციების გამოყენებით იპოვეთ სიმრავლის ელემენტების საშუალო არითმეტიკული

# cubed_multiples_of_5 = {x**3 for x in range(5, 101, 5)}

# average = sum(cubed_multiples_of_5) / len(cubed_multiples_of_5)

# print("The set of cubes of multiples of 5:", cubed_multiples_of_5)
# print("The average of the elements (arithmetic mean) is:", average)

#4. წინა მაგალითში არსებული სიმრავლისთვის შექმენით იტერატორი და StopIteration შეცდომის გამოსროლამდე
# დაბეჭდეთ სათითაოდ იტერატორის ელემენტები next() ფუნქციის გამოყენებით.

# cubed_multiples_of_5 = {x**3 for x in range(5, 101, 5)}
# iterator = iter(cubed_multiples_of_5)

# while True:
#     try:
#         cube = next(iterator)
#         print(cube)
#     except StopIteration:
#         break

#5. შექმენით tuple ტიპის ობიექტი, რომლის ელემენტებია 1-დან 100-მდე არსებული 5-ის ჯერადი რიცხვების კუბები. გამოიყენეთ for ციკლის მოკლე ჩაწერის ფორმა. შესაბამისი ფუნქციის გამოყენებით იპოვეთ tuple-ის სიგრძე (ელემენტების რაოდენობა)
# cubed_multiples_of_5 = tuple(x**3 for x in range(5, 101, 5))

# length = len(cubed_multiples_of_5)

# print("The tuple of cubes of numbers from 1 to 100 that are multiples of 5:", cubed_multiples_of_5)
# print("The length of the tuple is:", length)


# 6. წინა მაგალითში არსებული tuple ტიპის ობიექტისთვის შექმენით იტერატორი და StopIteration შეცდომის  გამოსროლამდე დაბეჭდეთ სათითაოდ იტერატორის ელემენტები next() ფუნქციის გამოყენებით.
# cubed_multiples_of_5 = tuple(x**3 for x in range(5, 101, 5))
# iterator = iter(cubed_multiples_of_5)

# try:
#     while True:
#         cube = next(iterator)
#         print(cube)
# except StopIteration:
#     pass

# 7. შექმენით გენერატორი, რომელიც სათითაოდ დააბურნებს რიცხვებს 1-დან 5-მდე. შექმენით შესაბამისი იტერატორი და სათითაოდ გამოიძახეთ 1-დან 5-მდე მდე რიცხვები.

# def number_generator():
#     for i in range(1, 6):
#         yield i

# iterator = number_generator()

# for num in iterator:
#     print(num)
