import numpy as np
import time
import argparse

# Argument Parser
parser = argparse.ArgumentParser(description="A simple Elementary Cellular Automata generator using Wolfram code to determine the transition rules")
parser.add_argument('-c', '--ca_size', default=71, help='Size/length of the Cellular Automaton')
parser.add_argument('-g', '--generation_count', default=50, required=False, help='Number of generations to run (-1 runs forever)')
args = parser.parse_args()

DELAY_DURATION_DEFAULT = 0.05 # seconds

CA_SIZE = int(args.ca_size)
GENERATION_COUNT = int(args.generation_count)


def displayPattern(generation):
    """Converts a CA generation array (consisting of 0s and 1s) to a pattern of cells and displays it"""
    gen_pattern = np.copy(generation)
    gen_pattern[generation == "0"] = " "
    gen_pattern[generation == "1"] = "■"
    print("".join(gen_pattern[1:len(generation)-1])) # doesn't display the boundary cells

def main():
    initial_generation = np.full(shape = CA_SIZE, dtype=str, fill_value=0)
    initial_generation[int(CA_SIZE / 2)] = 1

    current_generation = initial_generation
    next_generation = np.full(shape = CA_SIZE, dtype=str, fill_value=0)

    print("Wolfram Rule Number: ")
    wolfram_rule = int(input())
    wolfram_rule_binary = '{0:08b}'.format(wolfram_rule)

    ruleset = { "111": wolfram_rule_binary[0],
                "110": wolfram_rule_binary[1],
                "101": wolfram_rule_binary[2],
                "100": wolfram_rule_binary[3],
                "011": wolfram_rule_binary[4],
                "010": wolfram_rule_binary[5],
                "001": wolfram_rule_binary[6],  
                "000": wolfram_rule_binary[7]}

    counter = 0
    while(counter != GENERATION_COUNT):
        displayPattern(current_generation)
        time.sleep(DELAY_DURATION_DEFAULT)
        next_generation = np.full(shape = CA_SIZE, dtype=str, fill_value=0)
        for i in range(1, CA_SIZE-1):
            neighbourhood = "".join(current_generation[i-1:i+2])
            new_state = ruleset[neighbourhood]
            next_generation[i] = new_state
        current_generation = next_generation
        
        counter+=1


if __name__ == "__main__":
    main()