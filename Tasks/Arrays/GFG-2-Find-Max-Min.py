# Finding the max and min element in an array

class solution:
    def __init__(self,array):
        self.array = array

    def displayMax(self):
        setMax = self.array[0]
        for i in self.array:
            if setMax < i:
                setMax = i
        return setMax
    
    def displayMin(self):
        setMin = self.array[0]
        for i in self.array:
            if i < setMin:
                setMin = i
        return setMin
    
# main 

if __name__ == "__main__":
    arr = [22,14,8,17,35,3]
    sol = solution(arr)
    print("Maximum is ",sol.displayMax())
    print("Minimum is ",sol.displayMin())
