"""Simple test to verify the sliding puzzle implementation works"""

from enviroment import SlidingPuzzle


def test_environment():
    print("Testing SlidingPuzzle environment...")

    # Test 1: Simple one-move puzzle
    puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 0, 8])
    print(f"Initial state: {puzzle.get_state()}")
    assert not puzzle.is_solved()

    puzzle.move_tile(8, "left")
    print(f"After move: {puzzle.get_state()}")
    assert puzzle.is_solved()
    print("✓ Simple puzzle solved!")

    # Test 2: Two-move puzzle
    puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 0, 7, 8])
    print(f"\nTwo-move puzzle initial: {puzzle.get_state()}")
    puzzle.move_tile(7, "left")
    print(f"After first move: {puzzle.get_state()}")
    puzzle.move_tile(8, "left")
    print(f"After second move: {puzzle.get_state()}")
    assert puzzle.is_solved()
    print("✓ Two-move puzzle solved!")

    # Test 3: Test invalid moves are caught
    puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 0, 8])
    try:
        puzzle.move_tile(1, "down")  # Tile 1 is not adjacent to empty
        print("✗ Should have raised ValueError")
    except ValueError as e:
        print(f"✓ Invalid move correctly rejected: {e}")

    # Test 4: Test unsolvable state is rejected
    print(f"Initial state: {puzzle.get_state()}")
    try:
        puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 8, 7, 0])
        print("✗ Should have rejected unsolvable state")
    except ValueError as e:
        print(f"✓ Unsolvable state correctly rejected: {e}")

    puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 5, 4, 6, 8, 7, 0])
    print(f"Initial state: {puzzle.get_state()}")
    assert not puzzle.is_solved()

    print("\n✅ All environment tests passed!")


if __name__ == "__main__":
    test_environment()
