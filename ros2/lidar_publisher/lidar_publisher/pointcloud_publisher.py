import rclpy
from rclpy.node import Node

import numpy as np

from std_msgs.msg import Header
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2

class PointCloudPublisher (Node):
    def __init__(self):
        super().__init__('pointcloud_pub')
        self.publisher_ = self.create_publisher(PointCloud2 , '/pointcloud',10)
        self.timer = self.create_timer(1.0, self.publish_pointcloud)
        self.file_path = (
            "/media/zbook/New Volume/robotics-projects/"
            "lidar-pointcloud-processing/data/sample/"
            "scene_5_000006.pcd.bin"
        )
    def publish_pointcloud(self):
            points = np.fromfile(self.file_path, dtype=np.float32).reshape(-1,5)
            xyz = points[:, :3]

            header = Header()

            #header tells ROS when data was created and which coordinate
            #frame the data belongs to 
            #Without a header , RViz and other ROS nodes dont know how to place 
            # the point cloud in space 

            header.stamp = self.get_clock().now().to_msg()
            #ROS uses timestamps to synchornize sensors (LiDAR , camera IMU)
            #replay data accurately from rosbags
            #ROS align messages with similar timestamps

            header.frame_id = 'map'
            #this tells ROS , these points are expressed
            # in the map coordinate

            #for now we use map as point cloud is static
            # but in real robot as there is base link 
            #lidar link(child) so it would be  header.frame_id = 'lidar_link'
            #  and TF tree would tell RVIZ how lider_link is related to map

            msg = point_cloud2.create_cloud_xyz32(header, xyz.tolist())

            #mere xyz points ko ROS k PointCloud2 format mei convert krdo
            #originally xyz numpy array hoti hai 
            #aur create_cloud_xyz32 ko python list chaheay
            # so we use xyz.tolist()

            #AB aik ros PointCloud2 message ban gya hai 

            self.publisher_.publish(msg)
            self.get_logger().info(f" Published point cloud  {len(xyz) :,} points")

def main(args=None):
    rclpy.init(args=args)

    node = PointCloudPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
                                                


            
            
