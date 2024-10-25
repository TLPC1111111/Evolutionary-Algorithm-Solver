import argparse
from EA_Solve_Max import EA


def default_init_argparse():
    parser =argparse.ArgumentParser(description = "Evolutionary_Computing")
    parser.add_argument("--pop_size" , default = 100 , type = int , help = "Population Size")   ###100
    parser.add_argument("--binary_length" , default = 10 , type = int , help = "Binary_length")
    parser.add_argument("--pc" , default = 0.6 , type = float , help = "possiblility of Crossover")
    parser.add_argument("--pm" , default = 0.001 , type = float , help = "possibility of Mutation")
    parser.add_argument("--generations" , default = 200 , type = int)

    return parser

def main():
    args = default_init_argparse().parse_args()
    ev = EA(pop_size = args.pop_size , binary_length = args.binary_length , pc = args.pc , pm = args.pm , generations = args.generations)
    ev.run()


if __name__ == '__main__':
    main()