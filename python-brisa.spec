%define 	module	brisa
Summary:	UPnP framework for creating and managing UPnP devices
Name:		python-%{module}
Version:	0.8.0
Release:	0.2
License:	MIT
Group:		Development/Languages/Python
Source0:	https://garage.maemo.org/frs/download.php/5387/%{name}_%{version}-0maemo2.tar.gz
# Source0-md5:	426f8f861774948c65a763f1e5cc16a0
URL:		http://brisa.garage.maemo.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules >= 1:2.5
Requires:	python-cherrypy
Requires:	python-inotify
Requires:	python-mutagen
Requires:	python-gstreamer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BRisa is a UPnP framework for creating and managing UPnP devices, specially
MediaServer/MediaRenderer.

%prep
%setup -q -n %{name}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README 
%dir %{py_sitescriptdir}
%dir %{py_sitescriptdir}/brisa
%dir %{py_sitescriptdir}/brisa/config
%dir %{py_sitescriptdir}/brisa/control_point
%dir %{py_sitescriptdir}/brisa/log
%dir %{py_sitescriptdir}/brisa/services
%dir %{py_sitescriptdir}/brisa/services/cds
%dir %{py_sitescriptdir}/brisa/services/connmgr
%dir %{py_sitescriptdir}/brisa/services/web_server
%dir %{py_sitescriptdir}/brisa/threading
%dir %{py_sitescriptdir}/brisa/upnp
%dir %{py_sitescriptdir}/brisa/upnp/didl
%dir %{py_sitescriptdir}/brisa/upnp/message_handle
%dir %{py_sitescriptdir}/brisa/utils
%dir %{py_sitescriptdir}/brisa/xml_descriptions
%{py_sitescriptdir}/brisa/*.py[co]
%{py_sitescriptdir}/brisa/config/*.py[co]
%{py_sitescriptdir}/brisa/control_point/*.py[co]
%{py_sitescriptdir}/brisa/log/*.py[co]
%{py_sitescriptdir}/brisa/services/*.py[co]
%{py_sitescriptdir}/brisa/services/cds/*.py[co]
%{py_sitescriptdir}/brisa/services/connmgr/*.py[co]
%{py_sitescriptdir}/brisa/services/web_server/*.py[co]
%{py_sitescriptdir}/brisa/threading/*.py[co]
%{py_sitescriptdir}/brisa/upnp/*.py[co]
%{py_sitescriptdir}/brisa/upnp/didl/*.py[co]
%{py_sitescriptdir}/brisa/upnp/message_handle/*.py[co]
%{py_sitescriptdir}/brisa/utils/*.py[co]
%{py_sitescriptdir}/brisa/xml_descriptions/*.py[co]
%{py_sitescriptdir}/brisa/xml_descriptions/*.xml
%{py_sitescriptdir}/*.egg-info
%attr(755,root,root) %{_bindir}/brisa-conf
