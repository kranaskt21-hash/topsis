import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):

    data = pd.read_csv(input_file)

    # Check input validity
    if len(weights) != data.shape[1] - 1:
        raise Exception("Number of weights must match number of criteria")

    if len(impacts) != data.shape[1] - 1:
        raise Exception("Number of impacts must match number of criteria")

    # Convert weights to float
    weights = np.array(weights, dtype=float)

    # Extract numeric matrix
    matrix = data.iloc[:, 1:].values.astype(float)

    # Step 1: Normalize
    norm = matrix / np.sqrt((matrix**2).sum(axis=0))

    # Step 2: Weighted normalized matrix
    weighted = norm * weights

    # Step 3: Ideal best and worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(max(weighted[:, i]))
            ideal_worst.append(min(weighted[:, i]))
        elif impacts[i] == '-':
            ideal_best.append(min(weighted[:, i]))
            ideal_worst.append(max(weighted[:, i]))
        else:
            raise Exception("Impacts must be '+' or '-'")

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance calculation
    dist_best = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

    # Step 5: Score
    score = dist_worst / (dist_best + dist_worst)

    # Add results
    data['Topsis Score'] = score
    data['Rank'] = score.argsort()[::-1] + 1

    data.to_csv(output_file, index=False)


def main():
    if len(sys.argv) != 5:
        print("Usage: topsis input.csv weights impacts output.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2].split(',')
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)


if __name__ == "__main__":
    main()
    
