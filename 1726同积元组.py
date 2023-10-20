"""
给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。其中 a、b、c 和 d 都是 nums 中的元素，且 a != b != c != d 。

 

示例 1：

输入：nums = [2,3,4,6]
输出：8
解释：存在 8 个满足题意的元组：
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
示例 2：

输入：nums = [1,2,4,5,10]
输出：16
解释：存在 16 个满足题意的元组：
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums 中的所有元素 互不相同
"""
from collections import Counter

def tupleSameProduct(self, nums: list[int]) -> int:
    n = len(nums)
    if n < 4:
        return 0
    
    # 1.hash存储乘积
    # 计算列表中所有元素两两乘积的组合数量 hashDict
    # 每有一个元组(a,b,c,d)则有8个不同顺序组合
    # hashDict[a*b] = cnt(a*b) 表示乘积a*b组合数量， 
    # 每两个组成一个符合条件的元组，即有：cnt(a*b) * (cnt(a*b) - 1) /2 * 8个元组组合
    # 构建以乘积为键，组合s数为值的hash
    # {12: [(2,6),(3,4)]}
    hashDict = {}

    # for i in range(n):
    #     for j in range(i+1, n):
    #         hashDict[nums[i] * nums[j]] = hashDict.get(nums[i] * nums[j],0) + 1

    hashDict = Counter([nums[i] * nums[j] for i in range(n) for j in range(i+1,n)])
    r = 0
    for _,v in hashDict.items():
        r += v * (v-1) *4
    return r