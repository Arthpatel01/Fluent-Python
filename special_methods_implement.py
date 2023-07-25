import collections
import math
import random

# Named tuple representing a playing card with 'rank' and 'suit' fields
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # List of ranks and suits for a standard deck of cards
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # Create a list of Card instances for the entire deck using a list comprehension
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        # Returns the number of cards in the deck
        return len(self._cards)

    def __getitem__(self, position):
        # Allows accessing cards in the deck using indexing (e.g., deck[0], deck[1])
        return self._cards[position]


class Vector:
    def __init__(self, x=0, y=0):
        # Initialize the 2D vector with x and y components
        self.x = x
        self.y = y

    def __repr__(self):
        # Return a string representation of the vector in the format "Vector(x, y)"
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        # Calculate and return the magnitude (length) of the vector using the Pythagorean theorem
        return math.hypot(self.x, self.y)

    def __bool__(self):
        # Return True if the vector is non-zero (has a magnitude greater than 0), False otherwise
        return bool(abs(self))

    def __add__(self, other):
        # Add two vectors together and return the resulting vector
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        # Multiply the vector by a scalar (a number) and return the resulting vector
        return Vector(self.x * other, self.y * other)


if __name__ == '__main__':
    # Testing the FrenchDeck class
    deck = FrenchDeck()
    print(len(deck))  # Output: 52
    print(deck[3:5])  # Output: [Card(rank='5', suit='spades'), Card(rank='6', suit='spades')]

    # Printing all cards in reverse from the deck object
    for card in reversed(deck):
        print(card)

    # Testing the Vector class
    v = Vector(5, 3)
    print(v)  # Output: Vector(5, 3)
    print(abs(v))  # Output: 5.830951894845301 (magnitude of the vector)
    print(bool(v))  # Output: True (the vector is non-zero)

    v1 = Vector(4, 2)
    v2 = Vector(3, 1)
    print(v1 + v2)  # Output: Vector(7, 3) (sum of the two vectors)
    print(v * 3)  # Output: Vector(15, 9) (vector multiplied by scalar 3)
