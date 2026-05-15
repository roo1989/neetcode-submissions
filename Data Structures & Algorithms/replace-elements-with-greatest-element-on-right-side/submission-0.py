class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # arr[0] = max(arr[1:])
        # arr[1] = max(arr[2:])
        # arr[2] = max(arr[3:])
        # arr[3] = max(arr[4:])
        # arr[4] = max(arr[5:])
        # arr[5] = -1

        last_max = -1
        
        for i in range(len(arr) -1, -1, -1):
            new_max = max(arr[i], last_max)
            arr[i] = last_max
            last_max = new_max

        return arr
