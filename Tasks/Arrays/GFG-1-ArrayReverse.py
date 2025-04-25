arr = [1,2,8,9,4,2,1]

class solution:
    def  __init__(self,array):
        self.array = array
    def reverseArray(self):
        arr = []
        length = len(self.array)
        for i in range(1,length+1):        
            arr.append(self.array[-i])

        return arr

if __name__ == "__main__":
    sol = solution(arr)
    print(sol.reverseArray())

    # using inbuilt functions
    arr.reverse()
    print(arr)

 # Here Time complexity is O(length) or  O(n), Space complexity: input space = n, auxilary space = n so O(n+n) = O(2n) ~ O(n)