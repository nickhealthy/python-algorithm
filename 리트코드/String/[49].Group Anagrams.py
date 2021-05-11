import collections

class Solution:
    def groupAnagrams(self, strs):
        my_dict = collections.defaultdict(list)
        for key in strs:
            my_dict[''.join(sorted(key))].append(key)
        
        return my_dict.values()
        