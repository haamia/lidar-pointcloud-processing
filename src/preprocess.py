import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path("data/sample/scene_5_000006.pcd.bin")

points = np.fromfile(file_path , dtype=np.float32).reshape(-1,5)
                                                           
xyz = points[:, :3]

mask = np.isfinite(xyz).all(axis=1)

distance = np.linalg.norm(xyz[:, :2] , axis=1)

xyz= xyz[distance <50]

xyz = xyz[xyz[:, 2] > -2.0]

print(f"Filtered points: {len(xyz):,}:)")
z = xyz[:, 2]
z_norm = (z - z.min()) / (z.max() - z.min())

colors = plt.get_cmap("jet")(z_norm)[:, :3]


pcd = o3d.geometry.PointCloud()

pcd.points = o3d.utility.Vector3dVector(xyz)

pcd.colors = o3d.utility.Vector3dVector(colors)

o3d.visualization.draw_geometries(
    [pcd],
    window_name="Filtered LiDAR Point Cloud",
    width=1280,
    height=720
)