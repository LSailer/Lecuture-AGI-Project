"""Test that the new project structure works correctly"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print("Testing New Project Structure")
print("=" * 60)

# Test 1: Import shared LLM
print("\n1️⃣  Testing shared utils.llm import...")
try:
    from utils.llm import LLM
    print("   ✓ Successfully imported LLM from utils")
except ImportError as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 2: Import Tower of Hanoi components
print("\n2️⃣  Testing tower_of_hanoi imports...")
try:
    from tower_of_hanoi.enviroment import TowerOfHanoi
    from tower_of_hanoi.parser import Parser as TohParser
    from tower_of_hanoi.decomposer import Agent as TohAgent
    print("   ✓ Successfully imported Tower of Hanoi components")
except ImportError as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 3: Import Sliding Puzzle components
print("\n3️⃣  Testing sliding_puzzle imports...")
try:
    from sliding_puzzle.enviroment import SlidingPuzzle
    from sliding_puzzle.parser import Parser as SpParser
    from sliding_puzzle.decomposer import Agent as SpAgent
    print("   ✓ Successfully imported Sliding Puzzle components")
except ImportError as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 4: Verify Tower of Hanoi still works
print("\n4️⃣  Testing Tower of Hanoi functionality...")
try:
    toh = TowerOfHanoi(num_disks=3)
    print(f"   Initial state: {toh.get_state()}")
    toh.move_disk(1, 0, 2)
    print(f"   After move: {toh.get_state()}")
    print("   ✓ Tower of Hanoi works correctly")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 5: Verify Sliding Puzzle still works
print("\n5️⃣  Testing Sliding Puzzle functionality...")
try:
    puzzle = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 0, 8])
    print(f"   Initial state: {puzzle.get_state()}")
    print(f"   Goal state: {puzzle.goal_state}")
    print(f"   Grid size: {puzzle.grid_size}x{puzzle.grid_size}")
    puzzle.move_tile(8, "left")
    print(f"   After move: {puzzle.get_state()}")
    print(f"   Solved: {puzzle.is_solved()}")
    print("   ✓ Sliding Puzzle works correctly")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

# Test 6: Verify 4x4 puzzle works
print("\n6️⃣  Testing 4x4 Sliding Puzzle...")
try:
    puzzle_4x4 = SlidingPuzzle(initial_state=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15])
    print(f"   Grid size: {puzzle_4x4.grid_size}x{puzzle_4x4.grid_size}")
    print(f"   Goal state: {puzzle_4x4.goal_state}")
    print("   Visual:")
    print("   " + puzzle_4x4.visualize().replace("\n", "\n   "))
    print("   ✓ 4x4 puzzle created successfully")
except Exception as e:
    print(f"   ✗ Failed: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ All structure tests passed!")
print("=" * 60)
print("\nProject structure is correct. You can now run:")
print("  uv run run_tower_of_hanoi.py")
print("  uv run run_sliding_puzzle.py")
print("=" * 60)
