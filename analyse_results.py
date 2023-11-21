import json

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    fname = 'results.json'
    with open(fname, 'r') as f:
        results = json.load(f)

    df = pd.DataFrame(results)

    # Pivot the DataFrame to create a matrix format suitable for heatmap
    pivot_df = df.pivot(index='depth_percent', columns='context_length', values='score')

    # Plotting the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot_df, annot=True, fmt=".1f", cmap="viridis")
    plt.title("Parameter Sweep Heatmap")
    plt.ylabel('depth_percent')
    plt.xlabel('context_length')
    plt.savefig('result_plot.png')
    plt.show()


if __name__ == "__main__":
    main()