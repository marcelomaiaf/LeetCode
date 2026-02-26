class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = {}
        for l in magazine:
            store[l] = store.get(l,0) + 1
        
        for i in ransomNote:
            if not i in store or store[i]  <=0 :
                    return False
            else:
                store[i] -= 1
        return True