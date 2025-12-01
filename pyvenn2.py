#!/usr/bin/env python
# pyvenn2.py
# Draws a very basic 2-condition Venn Diagram with Python.


import os
import sys
import argparse
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Inputs:
# Labels A & B
# Three numbers: left (A), right (B), and intersect
# Mode: all of left/right, or exclusive left/right


def main():
    """Draw venn. We don't need a more complex workflow than this."""
    parser = argparse.ArgumentParser(
        prog='pyvenn2.py',
        description='Python wrapper for a two-sample Venn Diagram.',
    )
    parser.add_argument('output')   # Output file name
    parser.add_argument('-c', '--counts', nargs='+', type=int)   # Counts, [left, right, center]
    parser.add_argument('-s', '--samples', nargs='+')   # Samples, [left, right]
    parser.add_argument(
        '-I', '--intersect', action='store_true',
        default=False,
        help='Whether the left/right counts include the intersection. Defaults to "no"'
    )
    args = parser.parse_args()

    counts = args.counts
    # Sanity checks
    if len(args.counts) != 3:
        raise ValueError("There should be three counts inputs!")
    if len(args.samples) != 2:
        raise ValueError("There should be two sample name inputs!")

    # Adjusting for intersect condition
    if args.intersect:
        counts[0] = counts[0] - counts[2]
        counts[1] = counts[1] - counts[2]
        
    # Plot
    venn2(
        subsets=counts,
        set_labels=args.samples
    )
    plt.savefig(args.output)
    plt.show()


if __name__ == '__main__':
    main()

