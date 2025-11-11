import numpy as np
import matplotlib.pyplot as plt

# This algorithm is a classic implementation of the Nussinov algorithm for RNA secondary structure prediction, using dynamic programming.

def is_base_pair(a, b):
    return (a == 'A' and b == 'U') or (a == 'U' and b == 'A') or \
           (a == 'G' and b == 'C') or (a == 'C' and b == 'G')

def nussinov_matrix(seq):
    n = len(seq)
    dp = np.zeros((n, n), dtype=int)

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            if j - i >= 4:
                pair_score = dp[i+1][j-1] + is_base_pair(seq[i], seq[j])
                skip_i = dp[i+1][j]
                skip_j = dp[i][j-1]
                bifurcation = max([dp[i][k] + dp[k+1][j] for k in range(i+1, j)], default=0)
                dp[i][j] = max(pair_score, skip_i, skip_j, bifurcation)
    return dp

def traceback(dp, seq, i, j, pairs):
    if i < j:
        if dp[i][j] == dp[i+1][j]:
            traceback(dp, seq, i+1, j, pairs)
        elif dp[i][j] == dp[i][j-1]:
            traceback(dp, seq, i, j-1, pairs)
        elif dp[i][j] == dp[i+1][j-1] + is_base_pair(seq[i], seq[j]):
            pairs.append((i, j))
            traceback(dp, seq, i+1, j-1, pairs)
        else:
            for k in range(i+1, j):
                if dp[i][j] == dp[i][k] + dp[k+1][j]:
                    traceback(dp, seq, i, k, pairs)
                    traceback(dp, seq, k+1, j, pairs)
                    break
    return pairs

# --- Dot-Bracket Notation ---
def dot_bracket(seq, pairs):
    structure = ['.'] * len(seq)
    for i, j in pairs:
        structure[i] = '('
        structure[j] = ')'
    return ''.join(structure)

# --- Arc Plot Visualization ---
def plot_structure(seq, pairs):
    fig, ax = plt.subplots(figsize=(len(seq) * 0.6, 2))
    ax.set_xlim(0, len(seq))
    ax.set_ylim(0, 2)
    ax.axis('off')

    # Plot bases
    for i, base in enumerate(seq):
        ax.text(i + 0.5, 0.1, base, ha='center', va='bottom', fontsize=12)

    # Plot arcs
    for i, j in pairs:
        x = np.linspace(i + 0.5, j + 0.5, 100)
        y = 0.5 + 0.5 * np.sin(np.pi * (x - (i + 0.5)) / (j - i))
        ax.plot(x, y, color='blue')

    plt.title("RNA Secondary Structure", fontsize=14)
    plt.tight_layout()
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    seq = "UGGAUAGCCA"
    dp = nussinov_matrix(seq)
    pairs = traceback(dp, seq, 0, len(seq)-1, [])
    structure = dot_bracket(seq, pairs)

    print("Sequence: ", seq)
    print("Structure:", structure)
    plot_structure(seq, pairs)