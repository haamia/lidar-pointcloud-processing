import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Load LiDAR data
file_path = Path("data/sample/scene_5_000006.pcd.bin")

points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 5)

xyz = points[:, :3]


mask = np.isfinite(xyz).all(axis=1)

xyz = xyz[mask]

# Filter points
distance = np.linalg.norm(xyz[:, :2], axis=1)

xyz = xyz[distance < 50]

xyz = xyz[xyz[:, 2] > -2.0]

# BEV parameters
x_min, x_max = -50, 50
y_min, y_max = -50, 50
resolution = 0.2  # meters per pixel

width = int((x_max - x_min) / resolution)

height = int((y_max - y_min) / resolution)


height_map = np.full((height, width), np.nan)

# Convert coordinates to image pixels
x_img = ((xyz[:, 0] - x_min) / resolution).astype(np.int32)

y_img = ((xyz[:, 1] - y_min) / resolution).astype(np.int32)


valid = (
    (x_img >= 0) & (x_img < width) &
    (y_img >= 0) & (y_img < height)
)

x_img = x_img[valid]
y_img = y_img[valid]
z = xyz[:, 2][valid]


for x, y, z_val in zip(x_img, y_img, z):
    if np.isnan(height_map[y, x]):

        height_map[y, x] = z_val
    else:
        height_map[y, x] = max(height_map[y, x], z_val)


height_map = np.nan_to_num(height_map, nan=-2.0)


plt.figure(figsize=(10, 10))

plt.imshow(
    height_map,
    cmap="jet",
    origin="lower",
    vmin=-2.0,
    vmax=np.max(height_map)
)

plt.colorbar(label="Height (m)")

plt.title("LiDAR Height Map")

plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("images/height_map.png", dpi=300, bbox_inches="tight")
plt.show()