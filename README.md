## Sample Visualization

The project supports loading and visualizing LiDAR sweeps from the V2X-Sim 2.0 Mini dataset stored in `.pcd.bin` format.

**Input format:** `(x, y, z, intensity, ring_index)`  
**Sample frame:** `scene_5_000006.pcd.bin`  
**Number of points:** `43,542`

### Raw Point Cloud

![Raw Point Cloud](images/pointcloud.png)

## Preprocessing Pipeline

The preprocessing pipeline applies the following steps:

- Remove invalid points (`NaN` and `Inf`)
- Filter points beyond a 50 m radius
- Remove ground points with `z ≤ -2.0 m`

### Filtered Point Cloud

![Filtered Point Cloud](images/pointcloud_filtered.png)


## Bird's-Eye View Generation
This project converts V2X-Sim LiDAR point clouds into 2D occupancy maps.

![BEV Map](images/bev_map.png)

## Height Map Generation

The height map stores the maximum LiDAR height value for each grid cell in the Bird's-Eye View representation.

Higher values correspond to taller structures such as buildings, poles, and vegetation.

In the visualization below:
Dark blue regions correspond to ground surfaces and low-lying areas.

Green and yellow regions indicate medium-height objects such as vehicles and roadside structures.

Orange and red regions represent tall objects, including buildings, poles, and walls.

![Height Map](images/height_map.png)