import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jorear/home/f24_robotics_indoor_environment/install/indoor_environment'
