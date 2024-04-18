class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        freq = Counter(arr)
        sorted_items = sorted(freq.items(), key=lambda item: item[1])
        
        for key, value in sorted_items:
            if k <= 0:
                break
            if k >= value:
                k -= value
                freq[key] = 0
            else:
                freq[key] -= k
                k = 0
        
        counter = 0
        for value in freq.values():
            if value > 0:
                counter += 1

        return counter
