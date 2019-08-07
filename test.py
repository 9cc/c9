# account = 'chen'
# password = '123456'

# print('please input account:', end='')
# user_account = input()
# print('please input password:', end='')
# user_password = input()

# if user_account == account and user_password == password:
#     print('success!')
# else:
#     print('fail')


# class Student():
#     name = ''
#     age = 0


#     def __init__(self, name, age):
#         self.name = name
#         self.aeg = age
#         print(name)
#         print(age)

# student1 = Student('cc', 18)
# print(Student.__dict__)


for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print('%d * %d = %d' % (i, j, i*j), end=' ')
    print('')

    # 123
