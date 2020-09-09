#https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:
        '''
        #1.construct BST's F(i,n)=G(i-1)G(n-i)
        G = [0]*(n+1)
        G[0] ,G[1]= 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1]*G[i-j]
                
        return G[-1]
        '''
        #2.卡塔兰数
        #C_n+1 =2(2n+1)*C_n/(n+2) C0 = 1
        c = 1
        for i in range(0, n):
            c = 2*(2*i+1)*c/(i+2)
        
        return int(c)
