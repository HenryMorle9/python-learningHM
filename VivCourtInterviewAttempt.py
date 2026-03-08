class MovingTotal:
# my attempt. Failed misinterpreted the problem to be 2sum hashmap 
# when it was sliding window. lol. cringe.

    #big O is equal to O(1) because hashmap get is constant time
    #check if total is equal to 

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
    for num in numbers:
        numbers.append[num]

def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        exists = {}
        for count, num in total:
            need = total-num
            if exists[need]==total:
                return True
            exists[num, count]
        return False
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    
    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    
    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))