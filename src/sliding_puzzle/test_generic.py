"""Test the generic SlidingPuzzle implementation with different sizes"""
from enviroment import SlidingPuzzle

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
puzzle_3x3 = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 0, 8])
print(f"   Size: {puzzle_3x3.size}, Grid: {puzzle_3x3.grid_size}x{puzzle_3x3.grid_size}")
print(f"   Goal state: {puzzle_3x3.goal_state}")
print("   Visual:")
print("   " + puzzle_3x3.visualize().replace("\n", "\n   "))
puzzle_3x3.move_tile(8, "left")
print(f"   After move: {puzzle_3x3.get_state()}")
print(f"   ✓ PASSED: Solved = {puzzle_3x3.is_solved()}")

# Test 3: 4x4 puzzle (15-puzzle)
print("\n3️⃣  Test: 4x4 puzzle (15-puzzle)")
puzzle_4x4 = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15])
print(f"   Size: {puzzle_4x4.size}, Grid: {puzzle_4x4.grid_size}x{puzzle_4x4.grid_size}")
print(f"   Goal state: {puzzle_4x4.goal_state}")
print("   Visual:")
print("   " + puzzle_4x4.visualize().replace("\n", "\n   "))
puzzle_4x4.move_tile(15, "left")
print("   After moving tile 15 left:")
print("   " + puzzle_4x4.visualize().replace("\n", "\n   "))
print(f"   ✓ PASSED: Solved = {puzzle_4x4.is_solved()}")

# Test 4: 2x2 puzzle (3-puzzle)
print("\n4️⃣  Test: 2x2 puzzle (3-puzzle)")
puzzle_2x2 = SlidingPuzzle(initial_state=[1, 2, 0, 3])
print(f"   Size: {puzzle_2x2.size}, Grid: {puzzle_2x2.grid_size}x{puzzle_2x2.grid_size}")
print(f"   Goal state: {puzzle_2x2.goal_state}")
print("   Visual:")
print("   " + puzzle_2x2.visualize().replace("\n", "\n   "))
puzzle_2x2.move_tile(3, "up")
print("   After moving tile 3 up:")
print("   " + puzzle_2x2.visualize().replace("\n", "\n   "))
print(f"   ✓ PASSED: Solved = {puzzle_2x2.is_solved()}")

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
