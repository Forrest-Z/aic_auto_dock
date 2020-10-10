#ifndef GUI_WAY_H
#define GUI_WAY_H

#include <actionlib/server/simple_action_server.h>
#include <aic_auto_dock/gui_way2Action.h>
#include <aic_auto_dock/math/footprint.h>
#include <aic_auto_dock/math/pnpoly.hpp>
#include <aic_auto_dock/math/recognizeUtility.h>
#include <aic_msgs/Error.h>
#include <aic_msgs/RobotInfo.h>
#include <geometry_msgs/Polygon.h>
#include <geometry_msgs/Twist.h>
#include <math.h>
#include <nav_msgs/Odometry.h>
#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>
#include <tf/tf.h>
#include <tf/transform_broadcaster.h>
#include <tf/transform_listener.h>
#include <vector>
#include <visualization_msgs/Marker.h>
#include <aic_auto_dock/math/status.h>

typedef actionlib::SimpleActionServer< aic_auto_dock::gui_way2Action > Server;

using namespace std;
using namespace recognize_extraction;

struct detector
{
  double dist;
  double weight;
  int num;
};

struct AvoidType
{
  enum Avoid_type
  {
    ROUND,
    RECTANGLE
  };
};

class gui_way
{
public:
  gui_way(ros::NodeHandle&, ros::NodeHandle&);
  ~gui_way() {}

  void start(const aic_auto_dock::gui_way2GoalConstPtr&);

private:
  bool initDetector(double& percent, tf::Transform frame, double detector_y_coordinate);

  void initFrame(void);
  void workingFrame(void);

  void initStepProcess(const double& allowable_dist);

  void odomCallback(const nav_msgs::OdometryConstPtr&);
  void setFootprintCallback(const geometry_msgs::Polygon& msg);
  void LaserCallback(const sensor_msgs::LaserScan& msg);

  bool goalAccept();

  void pubMarkerCarStraightSquare();
  void pubMarkerCarTurnSquare();
  void pubVirtualPath();

  bool loadParamFromYaml();
  void cleanProcess(void);

  Server* as_;

  ros::NodeHandle local_nh_, nh_;
  ros::Subscriber setFootprint_sub_;
  ros::Subscriber laser_sub_;
  ros::Subscriber odom_sub_;
  ros::Publisher twist_pub_;
  tf::TransformListener listerner_;
  ros::Subscriber sub_robot_exception_;
  ros::Publisher marker_pub_CarRadius;
  ros::Publisher marker_pub_, virtual_path_pub_;
  tf::TransformBroadcaster br_;

  /*** 接口 ***/
  double back_dist_ = 0.0, obstacle_dist_ = 0.0;
  docking_direction direction_;
  double preparePosition_;

  /*** launch ***/
  double delta_detector_spacing_;
  double dangerRange_x_, dangerRange_y_;
  double yawThrehold_, radiusThrehold_, detector_y_coordinate_;
  double scale_;
  double aW_acc_, aW_dcc_;
  double prepare_lineVel_, prepare_angleVel_, prepare_scale_, angleVel_turn_;

  /*** global variable ***/
  tf::Transform realTime_odom_, port_foot_frame, prepare_foot_frame, prepareNav_foot_frame, odom_port_frame_,
      target_foot_frame;
  double prepareNavAngle_, preparePositionNav;
  StepProcess process_;

  double dangerRange_xMax_, dangerRange_xMin_, dangerRange_yMax_, dangerRange_yMin_;
  bool danger_mark_ = false;
  tf::StampedTransform foot_laser_frame_;
  double half_length_ = 0.0, half_width_ = 0.0;
  bool accept_robotInfo_ = false, accept_laserScan = false;
  AvoidType::Avoid_type avoidType_; // 0:circle  1:square

  actionlibStatus actionlib_status_;
  status motion_status_;

  vector< geometry_msgs::Point > points_;
  geometry_msgs::Polygon points_polygon_, points_straight_polygon_padding_, points_turn_polygon_padding_;

  double vel_line_, vel_angle_;
};

#endif // GUI_WAY_H