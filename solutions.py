import collections

class Solution:
    def strStr(self,source,target):
        if source is None or target is None:
            return -1
        for i in range(len(source)-len(target)+1):
            for j in range(len(target)):
                if source[i+j]!=target[j]:
                    break
            else:
                return i
        return -1

    def anagram(self,s,t):
        return collections.Counter(s)==collections.Counter(t)

    def anagram2(self,s,t):
        if s is None or t is None:
            return False
        if len(s)!=len(t):
            return False
        l=[]
        for i in range(len(s)):
            l.append(s[i])
        for i in range(len(t)):
            if t[i] not in l:
                return False
            else:
                l.remove(t[i])
        if len(l)==0:
            return True
        else:
            return False

    def anagram3(self,s,t):
        return sorted(s)==sorted(t)

    def compare_strings(self,A,B):
        if A is None or B is None:
            return False
        if len(A)<len(B):
            return False

        letters=collections.defaultdict(int)
        for a in A:
            letters[a]+=1
        for b in B:
            if b not in letters:
                return False
            elif letters[b]<=0:
                return False
            else:
                letters[b]-=1
        return True
    
        


if __name__=='__main__': 
    s=Solution()
    r=s.compare_strings('ABCD','AC')
    print(r)
