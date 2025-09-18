nums = [1,2,3,4]

prefix = [1] # chapdan boshlab sonlar ko'paytmasi uchun
suffix = [1] # o'ngdan o'sha elementgacha bo'lgan kopaytma uchun

# birinchi o'rinda prefixni to'ldirishimiz kerak 
# yigindilarni 0 dan boshlasak kopaytmalarni bir dan boshlaymiz

product = 1
for num in nums:
    product *= num
    prefix.append(product)

# endi suffixni to'ldirishimiz kerak bo'ladi
product = 1
for num in reversed(nums):
    product *= num
    suffix.append(product)

suffix.reverse()

result = []
for i in range(len(nums)):
    left, right = 1, 1
    left = prefix[i]
    right = suffix[i+1]
    prod = left * right
    result.append(prod)
print(result)