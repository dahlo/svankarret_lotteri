#!/usr/bin/env python3

import random
import sys
import argparse
import pdb
from pprint import pprint

# hämta argument
parser = argparse.ArgumentParser(description='Lotta fram husnummer.')
parser.add_argument('-s', '--seed', type=str, required=True, help='Hashsumman för en Bitcoin block-header.')
parser.add_argument('-n', '--n_numbers', type=int, default=1, help='Antal husnummer som ska lottas fram.')
args = parser.parse_args()


# ta in argument
antal_husnummer = args.n_numbers


# definiera listan av husnummer att välja mellan
husnummer = [
#            "6A", # sköter uthyrning av föreningshus
            "6B",
            "6C",
            "6D",
#            "6E", # med i styrelsen
            "6F",
            "6G",
#            "6H", # med i styrelsen
            "6J",
#            "6K", # vattenavläsning
            "6L",
            "6M",
            "6P",
            "6R",
#            "6S", # avgående styrelsemedlem
#            "6T", # med i styrelsen
#            "6U", # snögruppen
#            "6V", # revisor
#            "8A", # med i styrelsen
            "8B",
#            "8C", # vattenavläsning
            "8D",
            "8E",
            "8F",
#            "8G", # revisor
            "8H",
#            "8J", # med i styrelsen, avgående valberedning
#            "8K", # odlingslådorna
#            "8L", # odlingslådorna
            "8M",
            "8P",
#            "8R", # avgående valberedning
            "8S",
#            "8T", # snögruppen, beskär äppelträden
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

        # loop over the picked winners
        for winner in random.sample(l, n):

            # add 1 to their winner count
            counter[winner] += 1

    # print the counter
    pprint(counter)


#pdb.set_trace()

