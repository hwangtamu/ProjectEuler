__author__ = 'Han Wang'
nums  = [2]
for i in range(100000):
    nums.append(2*i+3)
l = 1
while nums[l]<500:
    tmp = nums[:l+1]
    for i in range(l+1,len(nums)):
        if nums[i]%nums[l]!=0:
            tmp.append(nums[i])
    nums = tmp
    l += 1
print nums[10000]

