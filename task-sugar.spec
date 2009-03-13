# NOTE: Do not edit, file was generated by jhconvert

Name: task-sugar
Version: 0.84.0
Release: %mkrel 1
Summary: Sugar Platform
License: GPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Requires: sugar-fructose >= 0.84.0
Requires: sugar-glucose >= 0.84.0
Requires: gstreamer0.10-plugins-base  
Requires: gstreamer0.10-espeak >= 0.3
Requires: gstreamer0.10-plugins-good  
Requires: libxml2-python  
Requires: python-numpy  
Requires: olpcsound  
Requires: pygame  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The Sugar Platform is a set of versioned components on which activity
authors can rely when targeting their activities to run on a particular
Sugar version.

%files
%defattr(-,root,root,-)

