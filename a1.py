""" 
Question 1:  (2 points) Write a function mh2kh(s) that given the speed, s, expressed in miles/hour returns
the same speed expressed in kilometres/hour. """
###################################################################
# Question 1
###################################################################
def mh2kh(s : float) -> float:
    """
    Convert a speed given in miles per hour (mph) to kilometers per hour (km/h).
    :param s: Speed in miles per hour.
    :returns: Equivalent speed in kilometers per hour.
    """
    return s * 1.60934
###################################################################
# Question 2
###################################################################
""" 2. (2 points) Two numbers a and b are called pythagorean pair if both a and b are integers and there
exists an integer c such that a^2 + b^2 = c^2. Write a function pythagorean_pair(a,b) that takes two
integers a and b as input and returns True if a and b are pythagorean pair and False otherwise. """
def pythagorean_pair(a, b) -> bool:
    """
    Check if two integers form a Pythagorean pair. A Pythagorean pair (a, b) satisfies the equation 
    a^2 + b^2 = c^2 for some integer c.
    
    :param a: First integer.
    :param b: Second integer.
    :returns: True if a and b form a Pythagorean pair, False otherwise.
    """

    return (a**2 + b**2)**0.5 % 1 == 0
###################################################################
# Question 3
###################################################################
""" 3. (2 points) Write a function in_out(xs,ys,side) that takes three numbers as input, where side is
non-negative. Here xs and ys represent the x and y coordinates of the bottom left corner of a
square; and side represents the length of the side of the square. (Notice that xs, ys, and side
completely define a square and its position in the plane). Your function should first prompt the
user to enter two numbers that represent the x and y coordinates of some query point. Your
function should print True if the given query point is inside of the given square, otherwise it
should print False. A point on the boundary of a square is considered to be inside the square. """
#side >= 0
def in_out(xs,ys,side) -> bool:
    """
    Check if a given query point is inside or on the boundary of a square defined by 
    its bottom-left corner and side length.
    
    :param xs: x-coordinate of the bottom-left corner of the square.
    :param ys: y-coordinate of the bottom-left corner of the square.
    :param side: Length of the square's side (non-negative).
    :returns: True if the query point is inside or on the boundary of the square, False otherwise.
    """
    ux = float(input("Entrez la valuer de x : ")) 
    uy = float(input("Entrez la valuer de y : ")) 
    print(xs <= ux <= xs + side and ys <= uy <= ys + side)
###################################################################
# Question 4
###################################################################

""""
4. (2 points) Write a function safe(n) that takes a non-negative integer n as input where n has at
most 2 digits. The function determines if n is a safe number. A number is not safe if it contains
a 9 as a digit, or if it can be divided by 9. The function should test if n is safe and return True if
n is safe and False otherwise.""" 

def safe(n) :
    """
    Determine if a number is "safe". A number is not safe if it contains a 9 as a digit or if it is divisible by 9.
    
    :param n: A non-negative integer with at most two digits.
    :returns: True if the number is safe, False otherwise.
    """
    return not( n//10 == 9 or n%9 == 0 or n % 10 == 9)
"""
5. (2 points) Write a function quote_maker(quote, name, year) that returns a sentence, i.e. a
string of the following form: In year, a person called name said: “quote” See the next
Section 2 below for some examples of how your function must behave."""
###################################################################
# Question 5
###################################################################
def quote_maker(quote, name, year) :
    """
    Creates a sentence using a quote, the name of the person who said it, and the year it was said.
    
    :param quote: The quote.
    :param name: The name of the person who said the quote.
    :param year: The year the quote was said.
    :returns: A sentence of the form "In [year], a person called [name] said: '[quote]'".
    """
    return f"In {year}, a person called {name} said: \"{quote}\""
"""
6. (2 points) Write a function quote_displayer() that prompts the user for a quote, name, and year.
The function should then print a sentence using the same format as specified in the previous
question. (To do that, your solution must make a call to quote_maker function from the previous
question to obtain a string that you then print)."""
###################################################################
# Question 6
###################################################################
def quote_displayer():
    """
    Prompt the user for a quote, name, and year, and display the formatted sentence using the quote_maker function.
    """
    quote = input("Il a dit quoi? : ")
    person = input(" Qui l'a dit? : ")
    year = input("En quelle annee? : ")
    print(quote_maker(quote, person, year))

"""
7. (2 points) In this question you will write a function that determines and prints the result of a
rock, paper, scissors game given choices of player 1 and player 2. In particular, write a function
rps_winner() that prompts the user for choice of player 1 and then choice of player 2, and then
it displays the result for player 1 as indicated in the examples given in Section 2. You may assume
that the user will only enter words: rock, paper or scissors in lower case. Recall that paper beats
rock, rock beats scissors and scissors beat paper. If both players make the same choice, we have
a draw."""
###################################################################
# Question 7
###################################################################
def rps_winners():
    """
    Simulate a Rock, Paper, Scissors game between two players and determines the winner.
    
    :returns: A string indicating whether Player 1 wins, Player 2 wins, or if it's a draw.
    """
    player1 = input("PLayer 1 : ##########################\nRock paper or scissors? : ")
    player2 = input("PLayer 2 : ##########################\nRock paper or scissors? : ")
    p1_score = (player1 == "paper")*1 + (player1 == "scissors")*2
    p2_score = (player2 == "paper")*1 + (player2 == "scissors")*2
    score = (3+p1_score - p2_score)%3
    return (score == 1)*"Player 1 wins!" + (score == 2)*"Player 2 wins!" + (score == 0)*"It's a draw!"    


"""
8. (2 points) Write a function fun(x) that takes as input a positive number x and solves the following
equation for y and returns y. The equation is 104y=x+3."""
###################################################################
# Question 8
###################################################################
def fun(x) :
    """
    Solve the equation 104y = x + 3 for y and return the value of y.
    
    :param x: The value of x in the equation.
    :returns: The value of y that solves the equation.
    """
    return (x+3)/104


"""
9. (2 points) Write a function ascii_name_plaque(name) that takes as input a string representing a
person’s name and draws (using print function)
a name plaque as shown in the examples given
in Section 2 below. Recall that you may not use
loops nor if/branching statements."""
###################################################################
# Question 9
###################################################################
def ascii_name_plaque(name) :
    """
    Create an ASCII name plaque for a given name.
    
    :param name: The name to be displayed on the plaque.
    :returns: A string representing the name plaque in ASCII art.
    """
    return "*"*(len(name)+4)+"\n*"+ " "*round((len(name)/2))+"*" +f"\n* {name} *" +"\n*"+ " "*round((len(name)/2))+"*" +"\n"+ "*"*(len(name)+4)

"""
****************************************
* *
* __Captain Kara 'Starbuck' Thrace__ *
* *
****************************************
"""
"""
10. (2 points) Write a function draw_court() that
draws with Turtle graphics a basketball court
as in this image. You do not have to use these
same colours, but you must use at least 2
distinct colours to fill some regions of the
court. Your figure does not have to be identical 
to mine, but it should be close enough."""

###################################################################
# Question 10
###################################################################
import turtle


def draw_court():
    """
    Draw a basketball court using Turtle graphics. The court should have at least two distinct colors.
    """

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=1080, height=720)
    t = turtle.Turtle()
    t.speed(-10)

    # Helper functions
    def draw_rectangle(t, width, height, color):
        t.fillcolor(color)
        t.begin_fill()
    
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
        t.end_fill()

    def draw_circle(t, radius, color):
        t.fillcolor(color)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()
        
    def draw_half_circle(t, radius, line_color, direction : int):
        t.pendown()
        initial_color = t.pencolor()
        t.pencolor(line_color)
        t.circle(radius, extent= direction * 180)
        t.pencolor(initial_color)
        

    t.penup()
    t.goto(-515, -275)  
    t.pendown()
    draw_rectangle(t, 1030, 550, "lightgray")  
    t.penup()
    t.goto(-470, -250)  
    t.pendown()
    draw_rectangle(t, 940, 500, "lightgray") 
    t.penup()
    


    t.penup()
    t.goto(-470, -100)  
    t.pendown()
    draw_rectangle(t, 160, 200, "orange")  
    t.penup()
    t.goto(-470, -120)  
    t.pendown()
    draw_rectangle(t, 160, 240, "") 
    
    t.penup()
    t.goto(-310,-100)
    t.pendown()
    draw_circle(t, 100, "") 
    
    t.penup()
    t.goto(310, -100)  
    t.pendown()
    draw_rectangle(t, 160, 200, "orange")  
    t.penup()
    t.goto(310, -120)  
    t.pendown()
    draw_rectangle(t, 160, 240, "")
    t.penup()
    t.goto(0, 250)  
    t.pendown()
    t.goto(0, -250) 
    t.penup()
    
    t.penup()
    t.goto(310,-100) 
    t.pendown()
    draw_circle(t, 100, "")  
    t.penup()
    
    t.goto(0, -50)
    t.pendown()
    draw_circle(t, 50, "orange")  
    t.penup()
    
    t.goto(-470, -250)
    draw_half_circle(t, 250, "white", 1) 
    t.penup()
    
    t.goto(470, 250)
    draw_half_circle(t, 250, "white", 1) 
    
    t.penup()
    t.goto(-450, -60)
    t.pendown()
    t.goto(-450, 60)
    t.goto(-450, 0)
    t.goto(-440, 0)
    t.penup()
    t.goto(-440, -5)
    draw_circle(t, 5, "white")

    t.penup()
    t.goto(450, -60)
    t.pendown()
    t.goto(450, 60)
    t.goto(450, 0)
    t.goto(440, 0)
    t.penup()
    t.goto(440, -5)
    draw_circle(t, 5, "white")
    





"""
11. (2 points) Write a function alogical(n) , that
takes as input a number, n, where n is bigger
or equal to 1, and returns the minimum number of times that n needs to be divided by 2 in order
to get a number equal or smaller than 1. For example 5.4/2=2.7. Since 2.7 is bigger than 1,
dividing 5.4 once by 2 is not enough, so we continue. 2.7/2=1.35 thus dividing 5.4 twice by 2 is
not enough since 1.35 is bigger than 1. So we continue. 1.35/2=0.675. Since 0.675 is less than
1, the answer is 3. In particular, these calculations determine that 5.4 needs to be divided by 2
three times minimum in order to get a number that is less than or equal to 1. See Section 2 for
more examples. Recall that you may not use loops nor if/branching statements."""
###################################################################
# Question 11
###################################################################
import math

def alogical(n) -> int:
    """
    :n: is the input number where n is bigger or equal to 1.
    :returns: It returns the amount of times we can divide n by 2 to get a number less than or equal to 1.
    """
    return math.ceil(math.log2(n)) 


"""12. (2 points) Write a function cad_cashier(price,payment) that takes two real non-negative numbers
with two decimal places as input, where payment>=price and where the second decimal in
payment is 0 or 5. They represent a price and payment in Canadian dollars. The function should
return a real number with 2 decimal places representing the change the customer should get in
Canadian dollars. Recall that in Canada, while the prices are expressed in pennies, the change is
based on rounding to the closest 5 cents. See the examples in Section 2 for clarification and
examples on how your function must behave."""
###################################################################
# Question 12
###################################################################

def cad_cashier(price, payment) -> float:
    """
    :price: It is the price of the item
    :payment: this is payed by the customer, it should be non-negative and bigger than or equal to price. It should end with 0 or 5 cents.
    :returns: It returns the amount of change in Canadian dollars rounded to the nearest 5 cents.
    """
    return round((payment - price)*20)/20



"""13. (5 points) Suppose that a cashier in Canada owes a customer some change and that the cashier
only has coins ie. toonies, loonies, quarters, dimes, and nickels. Write a function that determines
the minimum number of coins that the cashier can return. In particular, write
a function min_CAD_coins(price,payment) that returns five numbers (t,l,q,d,n) that represent
the smallest number of coins (toonies, loonies, quarters, dimes, and nickels) that add up to
the amount owed to the customer (here price and payment are defined as in the previous
question). You program must first call cad_cashier function, from question 13, to determine the
amount of change that needs to be returned. Then before doing anything else, you may want to
convert this amount entirely to cents (that should be of type int). Once you have the total
number of cents here are some hints on how to find the minimum number of coins.
Hints for your solution (algorithm) for question 14:
To find the minimum number of coins the, so called, greedy strategy (i.e. greedy algorithm) works for
this problem. The greedy strategy tries the maximum possible number of the biggest-valued coins first,
and then the 2nd biggest and so on. For example, if price is $14.22 and payment $20, the customer is
owed $5.80 (after rounding to closest 5 cents), thus 580 cents, the greedy strategy will first figure the
maximum number of toonies it can give to the customer. In this case, it would be 2 toonies. It cannot be
3 toonies as that equals $6 and the cashier would return too much money. Once the cashier returns 2
toonies, he/she still needs to return 180 cents. The next biggest coin after toonie is a loonie. So the
greedy strategy would try loonies next. Only 1 loonie can fit in 180 cents, so the cashier should next
return 1 loonie. Then there is 80 cents left. The next biggest coin to consider is a quarter … and so on …
ending with nickels. (For this example the function should return (2,1,3,0,1) ). Thus for this question,
you are asked to implement this strategy to find the optimal solution. See section 2 for more examples.
Side note: in the Canada (and most other) coin systems, the greedy algorithm of picking the largest
denomination of coin which is not greater than the remaining amount to be made will always produce
the optimal result (i.e. give the smallest number of coins). This is not automatically the case, though: if
the coin denominations were 1, 3 and 4 cents then to make 6 cents, the greedy algorithm would choose
three coins: one 4-cent coin and two 1-cent coins whereas the optimal solution is two 3-cent coins.
def """
###################################################################
# Question 13
###################################################################
def min_cad_coin(price, payment) -> tuple[int, int, int, int, int]:
    """
    :price: It is the price of the item
    :payment: this is payed by the customer, it should be non-negative and bigger than or equal to price. It should end with 0 or 5 cents.
    :returns: It returns a tuple of five integers (t,l,q,d,n) that represent the smallest number of coins (toonies, loonies, quarters, dimes, nickels) that add up to the amount owed to the customer.
    """
    change_cents = cad_cashier(price, payment) *100
    return change_cents//200, (change_cents % 200)//100, (change_cents%100)//25, (change_cents%25)//10, (change_cents%25%10)//5
