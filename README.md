## Sample Visualization

The project supports loading and visualizing V2X-Sim 2.0 Mini LiDAR sweeps stored in `.pcd.bin` format.

- Input format: `(x, y, z, intensity, ring_index)`
- Sample frame: `scene_5_000006.pcd.bin`
- Number of points: `43,542`

![Point Cloud](images/pointcloud.png)

## Preprocessing

The preprocessing pipeline includes:

- Invalid point removal
- Distance filtering (50 m)
- Ground removal (z > -2 m)