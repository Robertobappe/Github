nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
nums1 = [1,2,3,0,0,0]
m=3
n=3

for j in range(n):
    for i in range(n+m):
        if nums1[i] > nums2[j] and nums1[i] != 0:
            continue
        else:
            nums1[i]=nums2[j]

print(nums1)