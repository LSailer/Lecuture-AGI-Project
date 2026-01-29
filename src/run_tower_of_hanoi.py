"""Entry point for running Tower of Hanoi solver"""
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tower_of_hanoi.main import main

if __name__ == "__main__":
    main()
