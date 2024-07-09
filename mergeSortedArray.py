from typing import List

class Solution:
    def merge(self, nums1: [int], m: int, nums2: List[int], n: int) -> None:
        for i in nums2:
            nums1.append(i) #adicionando os elementos da L2 para L1

        L = []
        for j in range(len(nums1)):
            #adicionando os elementos diferentes de 0 a L
            if nums1[j] != 0:
                L.append(nums1[j])
        nums1 = L
        
        for k in range(len(L) - 1):
            if nums1[k] > nums1[k+1]: #ordenando 
                nums1[k], nums1[k+1] = nums1[k+1], nums1[k]          
    
        return nums1
    
a = Solution()
resultado = a.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(resultado)
