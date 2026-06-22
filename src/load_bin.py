import numpy as np
import open3d as o3d
from pathlib import Path

file_path = Path("data/sample/scene_5_000006.pcd.bin")

points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 5)

xyz = points[:, :3]

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)

print(f"Loaded {len(xyz):,} points")

o3d.visualization.draw_geometries(
    [pcd],
    window_name="V2X-Sim LiDAR Point Cloud",
    width=1280,
    height=720
)