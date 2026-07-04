import matplotlib.pyplot as plt


def save_projection_plot(projected_points, output_path):
    """Save projected image-plane points."""
    plt.figure(figsize=(8, 5))
    plt.scatter(projected_points[:, 0], projected_points[:, 1], s=4)
    plt.gca().invert_yaxis()
    plt.title("Projected Ground Points in Camera Image Plane")
    plt.xlabel("Image X")
    plt.ylabel("Image Y")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()


def save_bev_grid(grid, output_path):
    """Save BEV occupancy grid visualization."""
    plt.figure(figsize=(6, 8))
    plt.imshow(grid, origin="upper")
    plt.title("Synthetic Bird's-Eye-View Occupancy Grid")
    plt.xlabel("Lateral Grid Cells")
    plt.ylabel("Forward Grid Cells")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
