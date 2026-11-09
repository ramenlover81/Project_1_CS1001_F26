"""CSC 1001 - Programming Assignment 1.

Student starter file. Implement the eight required functions below.
The provided data types live in data.py; do not edit data.py.

For EVERY function, replace the TODO documentation with a short comment
explaining its purpose, input(s), and output. You may write helper functions.
"""

import data


# Part 1: vowel_count
def vowel_count(text: str) -> int:
    # TODO: Purpose: this counts the number of vowels in a string
    # TODO: Input(s): The text looks at a string of text to see how many vowels it has
    # TODO: Output: The function returns the amount of vowels in a string if it contains a vowel and adds all of them up to a final integer value (a,e,i,o,u)
    count = 0
    for letter in text:
        if letter.lower() in "aeiou":
            count += 1
    
    return count
    raise NotImplementedError("Part 1: implement vowel_count")


# Part 2: short_lists
def short_lists(items: list[list[int]]) -> list[list[int]]:
    # TODO: Purpose: the function looks at a nested list so it has a list inside another list so we are checking if the length of the list inside the bigger list's length is equal to 2 if so we are able to only filter to the lists that have a length of 2 or greater allowing for easy filtering with this function. 
    # TODO: Input(s): this function contains a list inside a bigger list of integer values 
    # TODO: Output: the function returns a list of the list of the intergers that has a length of greater than or equal to 2. 
     result = []
    
       for item in items:
            if len(item) == 2:
            result.append(item)
        
        return result
    raise NotImplementedError("Part 2: implement short_lists")


# Part 3: ascending_pairs
def ascending_pairs(items: list[list[int]]) -> list[list[int]]:
    # Purpose: Return a new nested list where each two-item list is in
    # non-descending order; nested lists of other lengths remain unchanged.
    # Input: items, a list of lists of integers.
    # Output: A new list of lists of integers.
    
    result = []
    for item in items:
        if len(item) == 2:
            if item[0] > item[1]:
                result.append([item[1], item[0]])
            else:
                result.append([item[0], item[1]])
        else:
            result.append(item)

    return result
   


# Part 4: add_prices
def add_prices(first: data.Price, second: data.Price) -> data.Price:
    # TODO: Purpose: This function adds two prices together and returns the total price as a new Price object.  
    # TODO: Input(s): The first price parameter is the dollar value price and then the second one is the cents price value.
    # TODO: Output: This function returns a new Price object that adds the two prices together and returns the total price as a new Price object.
    # TODO: count = 0 
    total_dollars = first.dollars + second.dollars + (first.cents + second.cents) // 100
    total_cents = (first.cents + second.cents) % 100
    return data.Price(total_dollars, total_cents)



    


# Part 5: rectangle_area
def rectangle_area(rectangle: data.Rectangle) -> float:
    # TODO: Purpose: This function computes the area of a rectangle given its width and height.
    # TODO: Input(s): this function takes in the parameter rectangle which is a data type that contains the width and height of the rectangle.
    # TODO: Output:this function returns area of a rectangle as a float, doing this by multiplying the width and height of the rectangle.
            width = rectangle.bottom_right.x - rectangle.top_left.x
            height = rectangle_top_left.y - rectangle.top_left.y
            area = width * height
        return area 
    
    raise NotImplementedError("Part 5: implement rectangle_area")


# Part 6: books_by_author
def books_by_author(author: str, books: list[data.Book]) -> list[data.Book]:
    # TODO: Purpose: This function returns a specific author by a specific book in a list of strings so it could coontain multiple authors. 
    # TODO: Input(s): This function takes in an authort in the form of a string and the books in a list form. 
    # TODO: Output: This function returns a list of books written by the specified author.
    # TODO: result = []
    result = []
    for book in books:
        if book.author == author:
            result.append(book)
    return result

    raise NotImplementedError("Part 6: implement books_by_author")


# Part 7: circle_bound
def circle_bound(rectangle: data.Rectangle) -> data.Circle:
    # TODO: Purpose: This function computes a circle that bounds the given rectangle.
    # TODO: Input(s): This function takes in a rectangle as a parameter.
    # TODO: Output: This function returns a circle that bounds the given rectangle.
    # TODO: 
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    radius = ((rectangle.bottom_right.x - rectangle.top_left.x) ** 2 + (rectangle.bottom_right.y - rectangle.top_left.y) ** 2) ** 0.5 / 2
    return data.Circle(center_x, center_y, radius)
    raise NotImplementedError("Part 7: implement circle_bound")


# Part 8: below_pay_average
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    # TODO: Purpose: This function computes the list of employees whose pay is below the average pay.
    # TODO: Input(s): This function takes in a list of employees as a parameter.
    # TODO: Output: This function returns a list of names of employees whose pay is below the average pay.
    # TODO: 
    if not employees:
        return []
    total_pay = sum(employee.pay for employee in employees)
    average_pay = total_pay / len(employees)
    below_average = []
    for employee in employees:
        if employee.pay < average_pay:
            below_average.append(employee.name)
    return below_average
    raise NotImplementedError("Part 8: implement below_pay_average")
