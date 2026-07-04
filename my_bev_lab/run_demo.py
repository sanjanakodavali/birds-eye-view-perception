from pathlib import Path

from camera_projection import (
    make_camera_matrix,
    make_extrinsic_matrix,
    generate_ground_points,
    project_points,
    create_bev_grid,
)
from visualize_bev import save_projection_plot, save_bev_grid
from evaluate_predictions import occupancy_statistics


def main():
    output_dir = Path("my_bev_lab/results")
    output_dir.mkdir(parents=True, exist_ok=True)

    intrinsic = make_camera_matrix()
    extrinsic = make_extrinsic_matrix(camera_height=1.6, pitch_degrees=8.0)

    ground_points = generate_ground_points()
    projected_points = project_points(ground_points, intrinsic, extrinsic)
    bev_grid = create_bev_grid(ground_points)

    save_projection_plot(projected_points, output_dir / "camera_projection_demo.png")
    save_bev_grid(bev_grid, output_dir / "bev_occupancy_demo.png")

    stats = occupancy_statistics(bev_grid)

    metrics_path = output_dir / "metrics_summary.md"
    metrics_path.write_text(
        "# BEV Demo Metrics Summary\n\n"
        "This demo generates synthetic ground-plane points, projects them through a "
        "pinhole camera model, and converts them into a BEV occupancy grid.\n\n"
        f"- Occupied cells: {stats['occupied_cells']}\n"
        f"- Total cells: {stats['total_cells']}\n"
        f"- Occupancy ratio: {stats['occupancy_ratio']}\n"
    )

    print("Generated BEV demo outputs in my_bev_lab/results/")


if __name__ == "__main__":
    main()
