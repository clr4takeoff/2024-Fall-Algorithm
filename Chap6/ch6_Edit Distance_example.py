#ch6_Edit Distance_example

def edit_distance_with_log(S1, S2):
    # Initialize table dimensions
    n, m = len(S1), len(S2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Log base case initialization
    print("Base case initialization:")
    for row in dp:
        print(row)
    print("\n")

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if S1[i - 1] == S2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j - 1] + cost,  # Substitution
                dp[i - 1][j] + 1,        # Deletion
                dp[i][j - 1] + 1         # Insertion
            )
            # Log the computation for each cell
            print(f"Edit({i}, {j}):")
            print(f"  Comparing S1[{i-1}] = '{S1[i-1]}' with S2[{j-1}] = '{S2[j-1]}'")
            print(f"  Substitution cost: {dp[i-1][j-1]} + {cost} = {dp[i-1][j-1] + cost}")
            print(f"  Deletion cost: {dp[i-1][j]} + 1 = {dp[i-1][j] + 1}")
            print(f"  Insertion cost: {dp[i][j-1]} + 1 = {dp[i][j-1] + 1}")
            print(f"  dp[{i}][{j}] = {dp[i][j]}")
            print("\n")

    # Log final table
    print("Final DP Table:")
    for row in dp:
        print(row)

    return dp[n][m]


# Example strings
S1 = "SNOW"
S2 = "SUNNY"

# Run the function
edit_distance_result = edit_distance_with_log(S1, S2)
