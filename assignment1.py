# Name: Chester Corpuz
# OSU Email: corpuzc@oregonstate.edu 
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: 04/25/2023
# Description: Assignment that consists of multiple problems to help with Big O notation 


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int,int):
    """
    TODO: Write this implementation
    This method utilizes a pointer to iterate through the code. The minimum and maximum are set to the first 
    value of the array and are changed if there is a larger (maximum) or lower (minimum) number. 
    """
    pointer = 0 
    minimum = arr.get(0)
    maximum = arr.get(0)
    while pointer < arr.length(): 
        if arr[pointer] > maximum: 
            maximum = arr[pointer]

        if arr[pointer] < minimum:
            minimum = arr[pointer]
        pointer += 1 
    
    return (minimum,maximum)

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    The method utilizes a pointer to traverse the arr object. The new object is made to the same length as the arr object. The conditionals
    are made depending on the module of 3 or 5. If the module of 3 or 5 are both 0, the new arr would input fizzbuzz into the index of that number. If the number is 
    divisible only by 3 and not 5, the new array would add fizz to that index. When the number is only fullly divisible by 5, then the array will add buzz to the new_arr
    in the index that that number was found. When the number cannot be fully divisible by 3 or 5, 
    then the new_arr will replace the set index value to the previous arr number. 
    """
    pointer = 0 
    new_arr = StaticArray(arr.length())
    while pointer < arr.length(): 
        if arr.get(pointer) % 3 == 0 and arr.get(pointer) % 5 == 0: 
            new_arr.set(pointer, 'fizzbuzz')
        elif arr.get(pointer) % 3 == 0 and arr.get(pointer) % 5 != 0: 
            new_arr.set(pointer, 'fizz')
        elif arr.get(pointer) % 3 != 0 and arr.get(pointer) % 5 == 0: 
            new_arr.set(pointer, 'buzz')
        else: 
            new_arr.set(pointer, arr.get(pointer))
        
        pointer += 1
    return new_arr 



# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    TODO: Write this implementation
    This method utilizes a two pointer approach. The left pointer points to the left most index while the right points to the right most index. 
    The values for the indexes are placed into two different temporary variables, and are used to switch the values of the left and right poitners. 
    The function will traverse the array until the left pointer exceeds the right pointer since the values in those indexes had been switched. 
    """
    left = 0 
    right = arr.length() - 1

    while left < right:
        temp_left = arr.get(left) 
        temp_right = arr.get(right)
        arr.set(left, temp_right)
        arr.set(right, temp_left)

        left += 1 
        right -=1 

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    TODO: Write this implementation
    This function utilizes a pointer to iterate through the indexes of the StaticArray. When the number of steps are greater than the array length 
    the program reduces it until it is a factor that is less than the array length. The program then places the elements into the new array's index based off of 
    the number of steps, current index of the Static Array, and if the steps are negative. 
    """
    pointer = 0 
    new_arr = StaticArray(arr.length()) 
    neg = False
    if steps < 0: 
        neg = True 

    #this allows for the uptake of steps greater than the array length  
    #loops until the the module of the steps is less than the array length, so that it does not exceed the bounds of the array
    while abs(steps) > arr.length(): 
        steps %= arr.length()

    if neg == True: 
        stpes = -steps 
    
    #Rotate (move the position of) the elements from the StaticArray into the new array based on the calculated steps 
    while pointer < arr.length(): 
        if pointer + steps < 0: 
            new_arr.set(arr.length() + pointer + steps, arr.get(pointer))
        elif pointer + steps >= arr.length():
            new_arr.set(pointer + steps - arr.length(), arr.get(pointer)) 
        else: 
            new_arr.set(pointer + steps, arr.get(pointer))

        pointer += 1 
    return new_arr

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    TODO: Write this implementation
    This function creates a new StaticArray object with an array that is dependent on the end and start input. 
    A pointer is used to iterate through the made StaticArray object and a conditional statement checks if 
    the range is counting in increasing or decreasing numbers. 
    """
    pointer = 0 
    new_arr = StaticArray(abs(end - start) + 1)
    while pointer != new_arr.length():
        new_arr.set(pointer, start)
        if end - start < 0: 
            start -=1 
        else: 
            start += 1
        pointer += 1
    
    return new_arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Write this implementation
    This funciton uses two pointers. The left pointer lags behind the right pointer by one step. When the difference between the right pointer 
    and the left pointer is negative then the array is checked as decreasing and continues to check the next indexes. When the difference between the right 
    and left pointer is not negative, then it is checked as increasing and continues to iterate over the next indexes. If both conditions of increasing or 
    decreasing are checked, then the function returns 0. If only the decreasing mark is checked a -1 is returned. If only the increasing mark is checked a 1 
    is returned.  
    """
    left = 0 
    right = 1 
    incr = False
    decr = False
    
    while right != arr.length(): 
        if type(arr.get(right)) == str:
            #utilizes the ord function to obtain ASCII values of the strings
            if ord(arr.get(right)) - ord(arr.get(left)) < 0: 
                decr = True 
            elif ord(arr.get(right)) - ord(arr.get(left)) > 0:
                incr = True 

        elif arr.get(right) - arr.get(left) < 0: 
            decr = True 
        elif arr.get(right) - arr.get(left) > 0:
            incr = True

        if decr == incr: 
            return 0 

        right += 1
        left += 1
    
    if incr == True:
        return 1 
    else:
        return -1 


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    Utilizes a fast and slow pointer. The fast pointer iterates through the array, while the slow pointer is changed to the 
    index of the fast pointer if the values for the fast and slow indexes are not the same. The count increases if the fast and slow indexes
    have the same element and is not in the 0th index. The count resets when the fast and slow indexes have different values. 
    """
    slow = 0
    fast = 0 
    max_mode = 1
    indx = slow 
    count = 1

    while fast != arr.length(): 
        if arr.get(fast) == arr.get(slow) and fast != 0: 
            count += 1
        
        if arr.get(fast) != arr.get(slow): 
            slow = fast 
            count = 1

        if count > max_mode: 
            max_mode = count 
            indx = slow 
        
        fast += 1 
    
    return arr.get(indx), max_mode

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------
def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    Removes the duplicates in a StaticArray by making a new array based off of the count of non-duplicates in the StaticArray.
    The function iterates in another loop, to input values into the new array based off of the non-duplicate values in the StaticArray. 
    """
    fast = 0 
    slow = 0 
    count = 1 
    #This loop determines the length of the Static Array Object. 
    while fast != arr.length(): 
        if arr.get(fast) != arr.get(slow): 
            count += 1
            slow = fast 
        fast += 1 
    
    val_arr = StaticArray(count) 
    #Resets the pointers for the StaticArray and sets a new pointer for the new Array 
    pointer = 0
    fast = 0 
    slow = 0 
    
    #This places the value from the 'fast' index into the new array at the index of 'pointer' if the value does not repeat.
    while pointer != val_arr.length(): 
        if pointer == 0: 
            val_arr.set(pointer, arr.get(fast))
            pointer += 1
        if arr.get(fast) != arr.get(slow): 
            val_arr.set(pointer, arr.get(fast))
            slow = fast 
            pointer += 1

        fast += 1 
        
    return val_arr 


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    Takes a StaticArray in any order, and returns a new StaticArray object in descending order
    """
    i = 0
    max_val = 0
    min_val = 0 

    #find the range of values in the arr 
    for i in range(arr.length()): 
        if arr.get(i) > max_val: 
            max_val = arr.get(i)
        
        if arr.get(i) < min_val: 
            min_val = arr.get(i)
            
    #set up count_array to be the length of the range of values
    count_arr = StaticArray((max_val - min_val) + 1)

    #Iterate through arr to determine the amount each value has.
    for i in range(arr.length()):
        if not count_arr.get(arr.get(i)-min_val):
            count_arr.set(arr.get(i) - min_val, 0)
        count_arr.set(arr.get(i) - min_val, count_arr.get(arr.get(i) - min_val) + 1)
     
    ord_arr = StaticArray(arr.length())

    i = count_arr.length() - 1 
    count = 0
    val = 0 
    while i >= 0: 
        if count_arr.get(i): 
            if count_arr.get(i) > 1: 
                ord_arr.set(val, i + min_val)
                val += 1 
                count += 1 
                if count != count_arr.get(i):
                    continue 
                else: 
                    i -= 1 
                    count = 0
            elif count_arr.get(i) == 1: 
                ord_arr.set(val, i + min_val)
                val += 1
                i -= 1 
        else: 
            i -= 1

    return ord_arr

# ------------------- PROBLEM 10 - TRANSFORM_STRING ---------------------------

def transform_string(source: str, s1: str, s2: str) -> str:
    """
    TODO: Write this implementation
    Takes the sources tring and replaces the values with other elements depending on which value it iterates on. 
    uses a for loop to iterate through the first array. The second loop is to iterate through the nested list.  
    """
    new_str =''
    for i in source: 
        for y in i:  
            if y in s1: 
                new_str += y.replace(y, s2[s1.index(y)]) 
            else: 
                if y.isupper() == True: 
                    new_str += y.replace(y, ' ')
                elif y.islower() == True: 
                    new_str+= y.replace(y, '#')
                elif y.isdigit() == True: 
                    new_str+= y.replace(y,'!')     
                else: 
                    new_str += y.replace(y,'=')
    return new_str


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# transform_string example 1\n')
    original = (
        '#     #  =====  !      =====  =====  #     #  =====',
        '#  #  #  !      !      !      !   !  ##   ##  !    ',
        '# # # #  !===   !      !      !   !  # # # #  !=== ',
        '##   ##  !      !      !      !   !  #  #  #  !    ',
        '#     #  =====  =====  =====  =====  #     #  =====',
        '                                                   ',
        '         TTTTT OOOOO      22222   66666    1       ',
        '           T   O   O          2   6       11       ',
        '           T   O   O       222    66666    1       ',
        '           T   O   O      2       6   6    1       ',
        '           T   OOOOO      22222   66666   111      ',
    )
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')

    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
