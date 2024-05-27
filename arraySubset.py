def divide_array(arr):
    # Sort the array in non-ascending order
    arr.sort(reverse=True)
    
    # Initialize subsets A and B
    A = []
    B = []
    
    # Initialize sums of A and B
    sum_A = 0
    sum_B = 0
    
    # Iterate over the sorted array and distribute the elements
    for num in arr:
        if sum_A <= sum_B:
            A.append(num)
            sum_A += num
        else:
            B.append(num)
            sum_B += num
            
    return A, B

# Example usage:
original_array = [3, 1, 7, 4, 2, 10]
A, B = divide_array(original_array)
print("Subset A:", A)
print("Subset B:", B)
print("Sum of A:", sum(A))
print("Sum of B:", sum(B))



def max_subset_with_greater_sum(arr):
    # Sort the array in decreasing order to start picking from the largest element
    sorted_arr = sorted(arr, reverse=True)
    
    # Initialize subsets A and B
    subset_a = []
    subset_b = []

    # Iterate over the sorted array and greedily add elements to subsets
    for num in sorted_arr:
        if sum(subset_a) <= sum(subset_b):
            # Add to subset A if its sum is less than or equal to subset B
            subset_a.append(num)
        else:
            # Otherwise, add to subset B
            subset_b.append(num)
    
    # If there's a requirement for subset A to be in increasing order
    subset_a.sort()
    
    # Verify that the conditions are met, otherwise, it's not possible
    if sum(subset_a) <= sum(subset_b) or (len(subset_a) + len(subset_b) != len(arr)):
        return "No solution exists that satisfies all conditions."
    
    return subset_a

# Example usage:
arr = [3, 1, 4, 2, 2]
subset_a = max_subset_with_greater_sum(arr)
print("Subset A with minimal number of elements and greater sum:", subset_a)








def minimum_segments_to_win(segments):
    """
    Function to determine the minimum number of segments player 1 should play to ensure
    their score is greater than player 2's score.

    Args:
    segments (list): A list where each element represents a segment of the game.
                     1 if the segment contains a coin, 0 otherwise.

    Returns:
    int: Minimum number of segments player 1 should play to win.
    """

    total_segments = len(segments)
    player1_score, player2_score = 0, sum(segments)

    for i in range(total_segments):
        # Player 1 plays the current segment
        player1_score += segments[i]

        # Update Player 2's score as they will play one less segment
        player2_score -= segments[i]

        # Check if Player 1's score is now greater than Player 2's
        if player1_score > player2_score:
            return i + 1  # Return the number of segments played by Player 1

    # If Player 1 can never win, return total number of segments
    return total_segments

# Test the function with the provided example
segments = [1, 1, 0, 1]
minimum_segments_to_win(segments)





















def optimal_play(segments):
    """
    Determine the minimum number of segments Player 1 should play to ensure their
    score is higher than Player 2's score by the end of the level.

    Args:
    segments (list): List of integers where 1 represents a segment with a coin and 0 represents a segment without a coin.

    Returns:
    int: Minimum number of segments Player 1 should play to win.
    """
    n = len(segments)
    player1_score, player2_score = 0, 0

    for i in range(n):
        # Player 1's score if they stop at this segment
        player1_score += 1 if segments[i] == 1 else -1

        # Player 2's score if they start after this segment
        player2_score = sum(1 if x == 1 else -1 for x in segments[i+1:])

        # If Player 1's score is greater, return the number of segments played
        if player1_score > player2_score:
            return i + 1

    # If Player 1 can't win, return 0
    return 0

# Test the function with the example
segments = [1, 1, 0, 1]
optimal_play(segments)

