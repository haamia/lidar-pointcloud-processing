import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path("data/sample/scene_5_000006.pcd.bin")

points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 5)

xyz = points[:, :3]


distance = np.linalg.norm(xyz[:, :2], axis=1)
xyz = xyz[distance < 50]
xyz = xyz[xyz[:, 2] > -2.0]

# BEV parameters
x_min, x_max = -50, 50
y_min, y_max = -50, 50
resolution = 0.2  # meters per pixel

width = int((x_max - x_min) / resolution)
height = int((y_max - y_min) / resolution)

bev = np.zeros((height, width))


x_img = ((xyz[:, 0] - x_min) / resolution).astype(np.int32)
y_img = ((xyz[:, 1] - y_min) / resolution).astype(np.int32)

mask = (
    (x_img >= 0) & (x_img < width) &
    (y_img >= 0) & (y_img < height)
)

x_img = x_img[mask]
y_img = y_img[mask]

bev[y_img, x_img] = 1

plt.figure(figsize=(10, 10))
plt.imshow(bev, cmap="gray", origin="lower")
plt.title("Bird's-Eye View")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("images/bev_map.png", dpi=300)
plt.show()