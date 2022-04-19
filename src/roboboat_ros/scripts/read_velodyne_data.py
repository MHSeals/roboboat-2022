import rospy
from sensor_msgs.msg import PointCloud2
from velodyne_msgs.msg import VelodynePacket, VelodyneScan

def send_pc2(pc2:PointCloud2, pub:rospy.Publisher):
    # print(len(pc2.data))
    pub.publish(pc2)

def main():
    rospy.init_node('velodyne_listener', anonymous=True)
    rospy.wait_for_message('/velodyne_points', PointCloud2)
    print('READY TO PUBLISH!!! ============================')
    pc2_publisher = rospy.Publisher('/scanner/cloud', PointCloud2, queue_size=600)
    _ = rospy.Subscriber('/velodyne_points', PointCloud2, callback=send_pc2, callback_args=pc2_publisher)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except (rospy.ROSException, KeyboardInterrupt) as e:
        print(e)
        exit(-1)