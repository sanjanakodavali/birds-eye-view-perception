import numpy as np


def occupancy_statistics(grid):
    """Compute simple BEV occupancy statistics."""
    occupied = np.count_nonzero(grid)
    total = grid.size
    occupancy_ratio = occupied / total if total else 0

    return {
        "occupied_cells": int(occupied),
        "total_cells": int(total),
        "occupancy_ratio": round(float(occupancy_ratio), 4)
    }
