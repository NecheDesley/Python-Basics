# total = 0
# count = 0
# while True:
#     number = input('please enter a number: ')
#     if number == 'done':
#         value = float(number)
#         total = total + value
#         count = count + 1
# average = total / count
# print('Average:', average)



# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names :
#     counts[name] = counts.get(name, 0) + 1
# print(counts)


#for split

# counts =dict()
# print('Enter a line of text:')
# line = input('')
# words = line.split()
# print('Words:', words)
# print('counting...')
# for word in words:
#     counts[word] = counts.get(word,0) +1
# print('counts', counts)


# to check time

# from datetime import datetime

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(current_time)


# def my_print(firstname, surname): 
#     print(firstname, surname)

# my_print("desley", "Neche")

def my_print(my_argument):
    print(my_argument)
def multi(num1, num2):
    return num1 * num2

my_print(multi(3, 7))

