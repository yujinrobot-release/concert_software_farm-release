Name:           ros-indigo-concert-software-common
Version:        0.0.3
Release:        0%{?dist}
Summary:        ROS concert_software_common package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/concert_software_common
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-web-video-server
Requires:       ros-indigo-world-canvas-server
BuildRequires:  ros-indigo-catkin

%description
Collection of concert software

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Apr 06 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

