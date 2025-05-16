from typing import List

def hamming_distance(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b))

class Solution0:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        wrd_len_dict = {}
        # This dict keeps subsequences for different wrd_lens with different humming sequences
        # this will be of stucture {wrd_len_of_content: [[[lst_idx_0, lst_idx_1], [wrd0, wrd1]], [[lst_idx_2, lst_idx_3], [wrd2, wrd3]]]}
        # eg. {2: [[[0,1], ["as", "ss"]], [[2], ["kk"]]]} 
        # Now "kk" is kept in a different list becuase it has more humming space from "ss", but upcoming subseq might continue "kk"
        address = [] # this will be [key, idx]
        max_seq_len = 0
        for i, word in enumerate(words):
            # print(word)
            wrd_len = len(word)
            # check if wrd_len as a key exist
            if wrd_len not in wrd_len_dict:
                wrd_len_dict[wrd_len] = [[[i], [word]]]
                if max_seq_len == 0:
                    address = [wrd_len, 0]
                    max_seq_len = 1
            else:
                # Search in thelist correponding to its entry
                been_added = False
                for entry_idx, entry in enumerate(wrd_len_dict[wrd_len]):
                    index_list = entry[0]
                    seq = entry[1]
                    seq_len = len(seq)
                    new_entries = []
                    # First check all prior member of that seqence as well 
                    for k in range(seq_len-2,-1,-1): # Traverse from seq_len-2 to 0
                        j = index_list[k]
                        if groups[i]!=groups[j] and hamming_distance(seq[k], word)==1:
                            been_added = True
                            new_seq = seq[0:k+1]+[word]
                            new_idx_lst = index_list[0:k+1]+[i]
                            print(new_idx_lst,new_seq)
                            new_entries.append([new_idx_lst, new_seq])
                    wrd_len_dict[wrd_len].extend(new_entries)

                    # check for alternating group condition
                    print(index_list)
                    j = index_list[-1]
                    if groups[i]!=groups[j] and hamming_distance(seq[-1], word)==1:
                        entry[0].append(i)
                        entry[1].append(word)
                        been_added = True 
                        if max_seq_len < len(entry[1]):
                            address = [wrd_len, entry_idx]
                            max_seq_len += 1 
                    

                            # This will be atmost be equal to max_seq_len but not more than that

                # Now it can be added to as many subseq as many it fits into
                # But if it has no been added then it should added as a new seq
                if not been_added:
                    wrd_len_dict[wrd_len].append([[i], [word]])
        print(wrd_len_dict)
        # finally return the sequence at the address, which has the max seq length
        key, idx = address
        return wrd_len_dict[key][idx][1]

# DP bottom up solution
class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        n = len(groups)
        dp = [1] * n
        prev_ = [-1] * n
        max_index = 0

        for i in range(1, n):
            for j in range(i):
                if (
                    self.check_hamming(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev_[i] = j
            if dp[i] > dp[max_index]:
                max_index = i

        ans = []
        i = max_index
        while i >= 0:
            ans.append(words[i])
            i = prev_[i]
        ans.reverse()
        return ans

    def check_hamming(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

if __name__ == "__main__":
    # Test case 1: Basic test with alternating groups and valid Hamming distances

    words1 = ["bab","daba","cab","baba","bada"]
    groups1 = [1,2,2,1,2]
    
    # Test case 2: Words of different lengths
    words2 = ["a","b","c","d"]
    groups2 = [1,2,1,2]
    
    # Test case 3: All same groups (should return single word)
    words3 = ["aaa","bbb","ccc"]
    groups3 = [1,1,1]
    

    
    solution = Solution()
    print(solution.getWordsInLongestSubsequence(words1, groups1))
    print(solution.getWordsInLongestSubsequence(words2, groups2))
    print(solution.getWordsInLongestSubsequence(words3, groups3))

