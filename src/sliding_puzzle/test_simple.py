"""Simple test to verify the sliding puzzle implementation works"""

from enviroment import SlidingPuzzle, CONFIGS


def test_environment():
    print("Testing SlidingPuzzle environment...")

    # Test 1: Simple one-move puzzle (blank at index 1, move tile 1 right)
    puzzle = SlidingPuzzle(initial_state=[1, 0, 2, 3, 4, 5, 6, 7, 8])
    print(f"Initial state: {puzzle.get_state()}")
    assert not puzzle.is_solved()

    puzzle.move_tile(1, "right")
    print(f"After move: {puzzle.get_state()}")
    assert puzzle.is_solved()
    print("✓ Simple puzzle solved!")

    # Test 2: Two-move puzzle
    puzzle = SlidingPuzzle(initial_state=[1, 4, 2, 3, 0, 5, 6, 7, 8])
    print(f"\nTwo-move puzzle initial: {puzzle.get_state()}")
    puzzle.move_tile(4, "down")
    print(f"After first move: {puzzle.get_state()}")
    puzzle.move_tile(1, "right")
    print(f"After second move: {puzzle.get_state()}")
    assert puzzle.is_solved()
    print("✓ Two-move puzzle solved!")

    # Test 3: Test invalid moves are caught
    puzzle = SlidingPuzzle(initial_state=[1, 0, 2, 3, 4, 5, 6, 7, 8])
    try:
        puzzle.move_tile(7, "up")
        print("✗ Should have raised ValueError")
    except ValueError as e:
        print(f"✓ Invalid move correctly rejected: {e}")

    # Test 4: Test unsolvable state is rejected (odd inversions for 3x3)
    try:
        puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 8, 7, 0])
        print("✗ Should have rejected unsolvable state")
    except ValueError as e:
        print(f"✓ Unsolvable state correctly rejected: {e}")

    # Test 5: Solvable hard state
    puzzle = SlidingPuzzle(initial_state=CONFIGS["3x3 (hardest)"])
    print(f"Hard initial state: {puzzle.get_state()}")
    assert not puzzle.is_solved()
    assert puzzle.goal_state == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("✓ Hard state accepted, goal is [0,1,...,8]")

    print("\n✅ All environment tests passed!")


if __name__ == "__main__":
    test_environment()
