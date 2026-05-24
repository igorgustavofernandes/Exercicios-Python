nums = []
nums_vistos = {}
target = 0

for c in range(4):
    nums.append(int(input('Enter a number: ')))
target = int(input('Enter the target sum: '))       

for i, num in enumerate(nums):
    complemento = target - num
    if complemento in nums_vistos:
        print(f'Complement Index: {nums_vistos[complemento]} Actual Index: {i}')
        break
    else:
        nums_vistos[num] =  i
    