#!/usr/bin/env python3

from random import Random
import sys



# felmeddelande
usage = f"""
Använding:
python3 {sys.argv[0]} [<antal husnummer att slumpa>]
ex.
python3 {sys.argv[0]} 2
"""

# ta in argument
antal_husnummer = sys.argv[1]

# sätt seed till det heltal som mosvaras av ett bitcoin-blocks hashsumma
seed = 42

# slumpa fram ett heltal baserat på ovanstående seed
rand = Random(seed)
heltal = rand.getrandbits(64)

# definiera listan av husnummer att välja mellan
husnummer = [
            "6A",
            "6B",
            "6C",
            "6D",
            "6E",
            "6F",
            "6G",
            "6H",
            "6J",
            "6K",
            "6L",
            "6M",
            "6P",
            "6R",
            "6S",
            "6T",
            "6U",
            "6V",
            "8A",
            "8B",
            "8C",
            "8D",
            "8E",
            "8F",
            "8G",
            "8H",
            "8J",
            "8K",
            "8L",
            "8M",
            "8P",
            "8R",
            "8S",
            "8T",
            ]

# översätt det slumpade heltalet till ett nummer i listan av husnummer





