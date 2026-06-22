import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


file_path = Path("data/sample/scene_5_000006.pcd.bin")

points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 5)

xyz = points[:, :3]
intensity = points[:, 3]

mask = np.isfinite(xyz).all(axis=1)
xyz = xyz[mask]
intensity = intensity[mask]

distance = np.linalg.norm(xyz[:, :2], axis=1)
mask = distance < 50

xyz = xyz[mask]
intensity = intensity[mask]

mask = xyz[:, 2] > -2.0

xyz = xyz[mask]
intensity = intensity[mask]

# BEV parameters
x_min, x_max = -50, 50
y_min, y_max = -50, 50
resolution = 0.2

width = int((x_max - x_min) / resolution)

height = int((y_max - y_min) / resolution)

intensity_map = np.zeros((height, width))


x_img = ((xyz[:, 0] - x_min) / resolution).astype(np.int32)
y_img = ((xyz[:, 1] - y_min) / resolution).astype(np.int32)

valid = (
    (x_img >= 0) & (x_img < width) &
    (y_img >= 0) & (y_img < height)
)

x_img = x_img[valid]
y_img = y_img[valid]
intensity = intensity[valid]


for x, y, i in zip(x_img, y_img, intensity):
    intensity_map[y, x] = max(intensity_map[y, x], i)

# Normalize for visualization
intensity_map /= intensity_map.max()

plt.figure(figsize=(10, 10))

plt.imshow(
    intensity_map,
    cmap="gray",
    origin="lower"
)

plt.colorbar(label="Normalized Intensity")

plt.title("LiDAR Intensity Map")
plt.xlabel("X")
plt.ylabel("Y")

plt.savefig("images/intensity_map.png", dpi=300, bbox_inches="tight")
plt.show()