import random


class Card:
    def __init__(self, rank: int, suite: str):
        self.rank = rank  # 1-13
        self.suite = suite  # Hearts, Diamonds, Spades, Clubs

    def __str__(self):
        """ Make a string from the card's rank and suite. E.g. 5 of Clubs will be '5C'"""
        r = self.rank
        str_r = None

        if r == 1:
            str_r = 'A'
        elif r == 11:
            str_r = 'J'
        elif r == 12:
            str_r = 'Q'
        elif r == 13:
            str_r = 'K'
        elif r == 14:
            str_r = ' '
        else:
            str_r = str(r)

        return f'{str_r}{self.suite[0].upper()}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        """ Compare if this card and 'other' card has the same rank """
        if not isinstance(other, Card):
            return False
        return self.rank == other.rank

    def __lt__(self, other):
        """ Compare if the rank of this card is lower than 'other' """
        if not isinstance(other, Card):
            return False
        return self.rank < other.rank

    def __gt__(self, other):
        """ Compare if the rank of this card is higher than 'other' """
        return other.rank < self.rank  # Just invert the check


class Deck:
    def __init__(self):
        """ Create a deck of 52 cards """

        self.cards = []

        for suite in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
            for rank in range(1, 14):
                self.cards.append(Card(rank, suite))
        for _ in range(0, 3):
            self.cards.append(Card(14, 'Joker'))

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    @staticmethod
    def insert(card_list, card):
        """ Inserts a 'card' in the correct spot in the deck 'card_list' """

        for comp in card_list:
            if card < comp:
                card_list.insert(card_list.index(comp), card)
                break
        else:
            card_list.append(card)

        return card_list

    def sort(self):
        """ Sort the deck according to card rank. All aces, the all two's, then all threes, ... """

        sorted_deck = []  # Create a temporary deck

        while len(self.cards) > 0:
            # Go through the deck from left to right, insert the deck in the appropriate spot
            self.insert(sorted_deck, self.take())  # Take a card from the old deck, insert it into the new one

        self.cards = sorted_deck  # Replace the old (empty) deck with the new (sorted) one
    
    @staticmethod
    def insert_by_suit(card_list, card):
        """ Inserts a 'card' in the correct spot in the deck 'card_list' """

        index = 0
        for comp in card_list:
            if card.suite[0].upper() < comp.suite[0].upper():
                card_list.insert(index, card)
                break
            elif card.suite[0].upper() == comp.suite[0].upper():
                if card < comp:
                    card_list.insert(index, card)
                    break
            index += 1
        else:
            card_list.append(card)

        return card_list

    def sort_by_suit(self):
        """ Sort the deck according to card suit, then rank. All Clubs, then
        all Diamonds's, ... Each rank sorted by rank, ace, two, three, ... """

        sorted_deck = []  # Create a temporary deck

        while len(self.cards) > 0:
            # Go through the deck from left to right, insert the deck in the appropriate spot
            self.insert_by_suit(sorted_deck, self.take())  # Take a card from the old deck, insert it into the new one

        self.cards = sorted_deck  # Replace the old (empty) deck with the new (sorted) one

    @staticmethod
    def insert_by_value(card_list, card):
        """ Inserts a 'card' in the correct spot in the deck 'card_list' """

        index = 0
        for comp in card_list:
            if card < comp:
                card_list.insert(index, card)
                break
            elif card == comp:
                if card.suite[0].upper() < comp.suite[0].upper():
                    card_list.insert(index, card)
                    break
            index += 1
        else:
            card_list.append(card)

        return card_list

    def sort_by_value(self):
        """ Sort the deck according to card rank. All aces, the all two's, then all threes, ... """

        sorted_deck = []  # Create a temporary deck

        while len(self.cards) > 0:
            # Go through the deck from left to right, insert the deck in the appropriate spot
            self.insert_by_value(sorted_deck, self.take())  # Take a card from the old deck, insert it into the new one

        self.cards = sorted_deck  # Replace the old (empty) deck with the new (sorted) one
    
    def pick_by_random(self):
        """ Pick and remove a random card from the deck """
        num = random.randint(0, len(self.cards)-1)
        return self.cards.pop(num)
    
    def deal(self, n):
        """ Deals the deck to n hands/piles """
        piles = []
        for _ in range(n):
            piles.append([])
        i = 0
        while len(self.cards) > 0:
            piles[i].append(self.take())
            i += 1
            i %= n
        return piles
    
    def remove_duplicates(self):
        """ Removes duplicate cards from the deck """
        unique_cards = []
        for card in self.cards:
            unique = True
            for unique_card in unique_cards:
                if card == unique_card and card.suite == unique_card.suite:
                    unique = False
            if unique:
                unique_cards.append(card)
        self.cards = unique_cards
    
    def remove_jokers(self):
        """ Removes Jokers from the deck """
        index = 0
        index_list = []
        for card in self.cards:
            if card.suite == 'Joker':
                index_list.append(index)
            index += 1
        index = 0
        for i in index_list:
            self.cards.pop(i - index)
            index += 1

    def take(self):
        """ Take the top card from the deck """
        return self.cards.pop()

    def put(self, card):
        """ Put a card on top of the deck """
        self.cards.append(card)

    def python_sort(self):
        self.cards.sort()


if __name__ == '__main__':
    deck = Deck()
    print('Fresh deck:', deck)
    deck.shuffle()
    print('Shuffled deck:', deck)
    deck.sort()
    print('Sorted deck:', deck)
    deck.shuffle()
    print('Shuffled deck:', deck)
    deck.sort_by_suit()
    print('Sorted deck by suit:', deck)
    deck.shuffle()
    print('Shuffled deck:', deck)
    deck.sort_by_value()
    print('Sorted deck by value:', deck)
    deck.shuffle()
    print('Shuffled deck:', deck)
    deck.python_sort()
    print('Python Sorted deck:', deck)
    print()

    c1 = deck.pick_by_random()
    c2 = deck.pick_by_random()
    c3 = deck.pick_by_random()
    print(f"Removed cards: {c1}, {c2}, {c3}")
    print("Rest of the deck: ", deck)
    deck.put(c1)
    deck.put(c2)
    deck.put(c3)
    print()

    deck.shuffle()
    print('Shuffled deck:', deck)
    deck.remove_jokers()
    print("Deck with Jokers removed: ", deck)
    print("Size: ", len(deck))
    print()

    deck = Deck()
    deck.shuffle()
    print('Shuffled deck:', deck)
    piles = deck.deal(3)
    for pile in piles:
        print("Pile: ", pile)
    print()

    deck = Deck()
    deck2 = Deck()
    while len(deck2) > 0:
        deck.put(deck2.take())
    deck.shuffle()
    print(f"Two decks of cards: {deck}, size: {len(deck)}")
    deck.remove_duplicates()
    print(f"Unique cards: {deck}, size: {len(deck)}")
    print()
