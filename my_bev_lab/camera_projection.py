import numpy as np


def make_camera_matrix(fx=800, fy=800, cx=640, cy=360):
    """Create a simple pinhole camera intrinsic matrix."""
    return np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ], dtype=float)


def make_extrinsic_matrix(camera_height=1.6, pitch_degrees=8.0):
    """
    Create a simplified camera extrinsic matrix.

    Coordinate assumption:
    - X: lateral direction
    - Y: forward direction
    - Z: vertical direction
    """
    pitch = np.deg2rad(pitch_degrees)

    rotation_x = np.array([
        [1, 0, 0],
        [0, np.cos(pitch), -np.sin(pitch)],
        [0, np.sin(pitch), np.cos(pitch)]
    ])

    translation = np.array([[0], [0], [camera_height]])
    extrinsic = np.hstack([rotation_x, translation])
    return extrinsic


def generate_ground_points(x_range=(-10, 10), y_range=(5, 40), spacing=1.0):
    """Generate synthetic 3D points on the road plane."""
    xs = np.arange(x_range[0], x_range[1] + spacing, spacing)
    ys = np.arange(y_range[0], y_range[1] + spacing, spacing)

    points = []
    for x in xs:
        for y in ys:
            points.append([x, y, 0, 1])

    return np.array(points, dtype=float)


def project_points(points_3d_homogeneous, intrinsic, extrinsic):
    """Project 3D homogeneous ground points into image coordinates."""
    camera_points = extrinsic @ points_3d_homogeneous.T
    image_points = intrinsic @ camera_points

    z = image_points[2]
    valid = z > 1e-6

    image_points[:, valid] /= z[valid]
    projected = image_points[:2, valid].T

    return projected


def create_bev_grid(points_3d_homogeneous, x_limits=(-10, 10), y_limits=(0, 45), resolution=0.5):
    """Convert 3D ground points into a simple BEV occupancy grid."""
    width = int((x_limits[1] - x_limits[0]) / resolution)
    height = int((y_limits[1] - y_limits[0]) / resolution)

    grid = np.zeros((height, width), dtype=np.uint8)

    for point in points_3d_homogeneous:
        x, y = point[0], point[1]

        if x_limits[0] <= x < x_limits[1] and y_limits[0] <= y < y_limits[1]:
            col = int((x - x_limits[0]) / resolution)
            row = int((y - y_limits[0]) / resolution)
            grid[height - row - 1, col] = 255

    return grid
