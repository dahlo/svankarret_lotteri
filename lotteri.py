#!/usr/bin/env python3

import random
import sys
import argparse
import pdb
from pprint import pprint

# hämta argument
parser = argparse.ArgumentParser(description='Lotta fram husnummer.')
parser.add_argument('-s', '--seed', type=str, required=True, help='Hashsumman för ett Bitcoin block. (hexadecimalt)')
parser.add_argument('-n', '--n_numbers', type=int, default=1, help='Antal husnummer som ska lottas fram.')
args = parser.parse_args()


# ta in argument
antal_husnummer = args.n_numbers


# definiera listan av husnummer att välja mellan
husnummer = [
#            "6A", # sköter uthyrning av föreningshus
            "6B",
#            "6C", # avgående valberedning
            "6D",
#            "6E", # med i styrelsen
            "6F",
#            "6G", # avgående valberedning
#            "6H", # med i styrelsen
            "6J",
#            "6K", # vattenavläsning
            "6L",
            "6M",
            "6P",
            "6R",
            "6S",
#            "6T", # med i styrelsen
#            "6U", # med i styrelsen
#            "6V", # revisor
#            "8A", # med i styrelsen
            "8B",
#            "8C", # vattenavläsning
            "8D",
            "8E",
            "8F",
#            "8G", # revisor, snögruppen
            "8H",
            "8J",
            "8K",
            "8L",
            "8M",
            "8P",
            "8R",
            "8S",
#            "8T", # snögruppen
            ]

# konvertera det hexadecimala talet till ett vanligt heltal i bas 10
seed = int(args.seed, 16)

# använd denna seed för slumpgenereringen
random.seed(seed)

# slumpa fram så många husnummer som efterfrågats
valda_husnummer = random.sample(husnummer, antal_husnummer)

# skriv ut resultatet
print(f"Valda husnummer: {', '.join(valda_husnummer)}")



# tester som kan köras manuellt
def distribution(l, n=1, rep=1000):
    """
    Test run and print distribution. Takes list l, selects n elements from the list, repeat this rep times.
    Counts the number of times the elements in list l are selected and prints the distribution.
    """

    # init empty counter dict
    counter = { key:0 for key in l }

    # run the sampling n times
    for i in range(rep):

        # set a new random seed
        random.seed()

        for winner in random.sample(l, n):
            counter[winner] += 1


    pprint(counter)


#pdb.set_trace()

