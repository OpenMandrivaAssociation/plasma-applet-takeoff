%define		oname	takeoff

Name:		plasma-applet-takeoff
Summary:	A full screen menu inspired by Slingshot and the OS X Launchpad menu
Version:	1.0.1
Release:	3
Group:		Graphical desktop/KDE
License:	GPLv3+
URL:		https://code.google.com/p/takeoff-launcher/
# Latest SVN snapshot
Source:		%{oname}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
Requires:	kdebase4-runtime

%description
Takeoff is a full screen menu inspired in the aspect of Slingshot and
the OS X Launchpad menu but adapted to the KDE users in a plasmoid.

%prep
%setup -q -n %{oname}-%{version}

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build
%find_lang plasma_applet_%{oname}

%clean
%__rm -rf %{buildroot}

%files -f plasma_applet_%{oname}.lang
%doc CHANGELOG COPYING COPYRIGHT README
%{_kde_libdir}/kde4/plasma_applet_%{oname}.so
%{_kde_services}/plasma-applet-%{oname}.desktop



%changelog
* Tue Mar 13 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.1-2mdv2011.0
+ Revision: 784577
- Fix typo in summary and description

* Tue Mar 13 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0.1-1
+ Revision: 784570
- imported package plasma-applet-takeoff

