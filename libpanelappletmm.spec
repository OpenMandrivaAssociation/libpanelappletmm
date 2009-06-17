%define major 1
%define api 2.6
%define libname		%mklibname panelappletmm %{api} %{major}
%define develname %mklibname -d panelappletmm

Name:		libpanelappletmm
Version:        2.26.0
Release:        %mkrel 2
Summary:        C++ interface for Gnome panel applets

Group:          System/Libraries
License:        LGPLv2+
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gconfmm2.6-devel >= 2.6.0
BuildRequires: libgnomemm2.6-devel >= 2.6.0
BuildRequires: gnome-panel-devel >= 2.14.0
#gw libtool dep:
BuildRequires: libglade2.0-devel
BuildRequires: doxygen, graphviz


%description
libpanelappletmm is part of the gnomemm project and provides a C++
interface for developing Gnome panel applets.

%package	-n %{libname}
Summary:	A C++ wrapper for GNOME Panel library
Group:		System/Libraries

%description	-n %{libname}
This library provides a C++ wrapper for GNOME Panel library.
It is a subpackage of the gnomemm project, which provides C++ binding
of various GNOME libraries.


%package -n %develname
Summary:  Headers for developing programs that will use %{name}
Group:    Development/C++
Requires: %{libname} = %{version}-%{release}
Provides: %name-devel = %version-%release
#gw libtool dep:
Requires: libglade2.0-devel

%description -n %develname
This package contains the static libraries and header files needed for
developing C++ gnome panel applets using libpanelappletmm.


%prep
%setup -q


%build
%configure2_5x --disable-static
%make

# Build documentation
make -C docs/reference


%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdvver < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-, root, root, -)
%doc AUTHORS NEWS README
%{_libdir}/libpanelappletmm-%api.so.%{major}*

%files -n %develname
%defattr(-, root, root, -)
%doc ChangeLog docs/reference/html
%{_includedir}/libpanelappletmm-%api
%{_libdir}/libpanelappletmm-%api.la
%{_libdir}/libpanelappletmm-%api.so
%{_libdir}/libpanelappletmm-%api
%{_libdir}/pkgconfig/libpanelappletmm-%api.pc


