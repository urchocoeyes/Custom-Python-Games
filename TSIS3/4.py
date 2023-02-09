def filter_prime(nums):
    for i in range(len(nums)):
        print("i :", i)
        isPrime = True
        for j in range(2, nums[i]):
            print("j :", j)
            print('nums[i] :', num[i])
            if nums[i] % j == 0:
                isPrime = False
        if isPrime:
            print("isPrimed :" , nums[i])


nums = input()
num = nums.split(' ')
print(num)
n = [int(x) for x in num]
print(n)
print("filtered n : ")
filter_prime(n)


        
        