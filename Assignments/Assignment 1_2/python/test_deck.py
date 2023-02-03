from deck import Deck, Card

# Implementera tester ni anser lämpliga här. Motivera gärna varför de behövs (vad de testar och varför).
"""
Bonusuppgift 1:
(En bonuspoäng inför tentan)
Skriv testfall för alla metoder. Antingen i python eller C++.
Python - test_deck.py
• Ni ska förutom sorteringsalgoritmen även skriva tester för hela kodbasen.
• Implementera lämpliga tester för er sorteringsalgoritm
• - Deck.insert(card_list, card))
• Implementera även tester för de andra metoderna:
• - Card.__init__()
• - Card.__eq__()
• - Card.__lt__()
• - Card.__gt__()
• - Deck.__len__()
• - Deck.sort()
• - Deck.take()
• - Deck.put()
• Skriv en kort motivering för era tester

Bonusuppgift 2:
(En bonuspoäng inför tentan)
Följande ska implementeras (antingen i C++ eller python):
• Lägg till tre jokrar till kortleken (ska läggas till när kortleken skapas)
• Lägg till minst tre av följande funktioner:
o sort_by_suit – Sortera så att kort av samma färg (suit) grupperas tillsammans.
Inom färgen ska de sorteras i ordning
o sort_by_value – Sortera korten i nummerordning. Notera: Sorteringen ska
alltid bli samma, så ni måste ta hänsyn även till färgen (suit)
o pick_by_random – Välj ut (och plocka bort) ett kort slumpmässigt ur leken.
o deal(int n) – Dela ut kortleken till n antal personer. Här får ni tänka efter hur ni
ska implementera denna, så att ni får jämnt antal korthögar. (Kan vara separat
/ statisk funktion)
o remove_duplicates – Leta upp och ta bort kort som är duplicerade
o remove_jokers – Ta bort jokrarna
"""

def test_card():
    # Test här
    pass


def test_deck():
    d = Deck()

    
