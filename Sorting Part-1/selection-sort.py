class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            hold_small=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[hold_small]:
                    hold_small=j
            arr[i],arr[hold_small]=arr[hold_small],arr[i]
        return arr
