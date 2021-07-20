from random import choices
from typing import List

Genome = List[int]
Population = List[Genome]
Thing = namedtuple('Thing',['name','value','weight'])

def generate_genome(length)->Genome:
    return choices([0,1],k=length)

def generate_population(size,genome_length) ->Population:
    return [generate_genome(genome_length) for _ in range(size) ]

def fitness(genome,things,weight_linit)->int:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of the same length")
    
    weight = 0
    value = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > weight_limit:
                return 0
    return value
