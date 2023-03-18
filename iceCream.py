"""You have four bowls of ice cream.
Each bowl can only have one scoop.
There are three repeatable flavors: chocolate, vanilla, strawberry.
These flavors can be in any amount of the four bowls.
BUT
There are two unique flavors: cookie dough and blueberry.
If any bowl has either one of these flavors, no other bowls can have that
flavor.
For instance, there can be an arrangement with one bowl of blueberry and three
bowls of vanilla, but not two bowls of blueberry in combination with any other
flavors.

How many possible combinations can be made?"""

# define flavors via set
repFlav = {"chocolate", "vanilla", "strawberry"}

uniqueFlav = {"blueberry", "cookie dough"}

# create dictionary for bowls, where bowl number is key and the value is empty
# the value will be set to a flavor

bowls = {
        "bowlOne": "",
        "bowlTwo": "",
        "bowlThree": "",
        "bowlFour": ""
        }

print(repFlav)
print(uniqueFlav)
x = bowls.keys()
y = bowls.values()
print(x)
print(y)
