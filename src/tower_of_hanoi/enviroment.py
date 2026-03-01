class TowerOfHanoi:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.towers = [list(range(num_disks, 0, -1)), [], []]

    def move_disk(self, disk: int, from_tower: int, to_tower: int):
        if not self.validate_move((disk, from_tower, to_tower)):
            raise ValueError("Invalid move attempted.")
        self.towers[from_tower].remove(disk)
        self.towers[to_tower].append(disk)
        return self.towers

    def validate_move(self, move: tuple):
        disk, from_tower, to_tower = move
        if not self.towers[from_tower] or self.towers[from_tower][-1] != disk:
            raise ValueError("Invalid move: Disk not on top of from_tower.")
        if self.towers[to_tower] and self.towers[to_tower][-1] < disk:
            raise ValueError("Invalid move: Cannot place larger disk on smaller disk.")
        return move

    def is_valid_state(self, state):
        flat_disks = [disk for tower in state for disk in tower]
        if sorted(flat_disks) != list(range(1, self.num_disks + 1)):
            raise ValueError("Invalid state: Disks missing or duplicated.")
        for tower in state:
            for i in range(len(tower) - 1):
                if tower[i] < tower[i + 1]:
                    raise ValueError(
                        "Invalid state: Larger disk on top of smaller disk."
                    )
        return state

    def is_solved(self):
        return len(self.towers[2]) == self.num_disks

    def get_state(self):
        return [tower[:] for tower in self.towers]

    def preview_move(self, action) -> list:
        """Return resulting state after action WITHOUT mutating self."""
        disk, from_tower, to_tower = action
        towers = [tower[:] for tower in self.towers]
        towers[from_tower].remove(disk)
        towers[to_tower].append(disk)
        return towers

    def apply_move(self, action):
        self.move_disk(action[0], action[1], action[2])

    def reset(self):
        self.towers = [list(range(self.num_disks, 0, -1)), [], []]


if __name__ == "__main__":
    game = TowerOfHanoi(3)
    print(game.get_state())
    game.move_disk(1, 0, 1)
    print(game.get_state())
    game.move_disk(0, 0, 2)
    print(game.get_state())
    is_solved = game.is_solved()
    print(is_solved)
