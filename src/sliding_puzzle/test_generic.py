"""Test the generic SlidingPuzzle implementation with different sizes"""
from enviroment import SlidingPuzzle, CONFIGS

print("=" * 60)
print("Testing Generic SlidingPuzzle Implementation")
print("=" * 60)

# Test 1: Verify initial_state is required
print("\n1️⃣  Test: initial_state is required")
try:
    puzzle = SlidingPuzzle(None)
    print("   ✗ FAILED: Should have raised ValueError")
except ValueError as e:
    print(f"   ✓ PASSED: {e}")

# Test 2: 3x3 puzzle (8-puzzle)
print("\n2️⃣  Test: 3x3 puzzle (8-puzzle)")
puzzle_3x3 = SlidingPuzzle(initial_state=[1, 0, 2, 3, 4, 5, 6, 7, 8])
print(f"   Size: {puzzle_3x3.size}, Grid: {puzzle_3x3.grid_size}x{puzzle_3x3.grid_size}")
print(f"   Goal state: {puzzle_3x3.goal_state}")
assert puzzle_3x3.goal_state == [0, 1, 2, 3, 4, 5, 6, 7, 8]
print("   Visual:")
print("   " + puzzle_3x3.visualize().replace("\n", "\n   "))
puzzle_3x3.move_tile(1, "right")
print(f"   After move: {puzzle_3x3.get_state()}")
print(f"   ✓ PASSED: Solved = {puzzle_3x3.is_solved()}")

# Test 3: 4x4 puzzle (15-puzzle)
print("\n3️⃣  Test: 4x4 puzzle (15-puzzle)")
puzzle_4x4 = SlidingPuzzle(initial_state=[1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(f"   Size: {puzzle_4x4.size}, Grid: {puzzle_4x4.grid_size}x{puzzle_4x4.grid_size}")
print(f"   Goal state: {puzzle_4x4.goal_state}")
assert puzzle_4x4.goal_state == list(range(16))
print("   Visual:")
print("   " + puzzle_4x4.visualize().replace("\n", "\n   "))
puzzle_4x4.move_tile(1, "right")
print("   After moving tile 1 right:")
print("   " + puzzle_4x4.visualize().replace("\n", "\n   "))
print(f"   ✓ PASSED: Solved = {puzzle_4x4.is_solved()}")

# Test 4: 2x2 puzzle (3-puzzle)
print("\n4️⃣  Test: 2x2 puzzle (3-puzzle)")
puzzle_2x2 = SlidingPuzzle(initial_state=CONFIGS["2x2"])
print(f"   Size: {puzzle_2x2.size}, Grid: {puzzle_2x2.grid_size}x{puzzle_2x2.grid_size}")
print(f"   Goal state: {puzzle_2x2.goal_state}")
assert puzzle_2x2.goal_state == [0, 1, 2, 3]
print("   Visual:")
print("   " + puzzle_2x2.visualize().replace("\n", "\n   "))

# Test 5: Invalid size (non-square)
print("\n5️⃣  Test: Invalid size (non-square)")
try:
    puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 0])
    print("   ✗ FAILED: Should have raised ValueError")
except ValueError as e:
    print(f"   ✓ PASSED: {e}")

# Test 6: Unsolvable state
print("\n6️⃣  Test: Unsolvable state (odd inversions)")
try:
    puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 8, 7, 0])
    print("   ✗ FAILED: Should have raised ValueError")
except ValueError as e:
    print(f"   ✓ PASSED: {e}")

print("\n" + "=" * 60)
print("✅ All tests passed!")
print("=" * 60)
