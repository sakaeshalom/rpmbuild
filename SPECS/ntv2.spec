Name: ntv2
Summary: AJA NTV2 SDK
Version: 16.2_bugfix5
Release: 1%{?dist}
License: MIT
URL: https://github.com/aja-video/ntv2
Source0: ntv2-16.2-bugfix5.tar.gz

%description
AJA NTV2 SDK is an open-source library and kernel module for AJA devices.

%prep
%autosetup -n ntv2-16.2-bugfix5

%build
%{cmake} \
	-DAJA_INSTALL_HEADERS=ON -DAJA_INSTALL_SOURCES=ON \
	-DAJA_DEPLOY_LIBS=ON \
	-DAJA_BUILD_OPENSOURCE=ON

%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/usr/libexec/ajantv2
mv %{buildroot}/usr/{CMakeLists.txt,ajadriver,ajalibraries,build,cmake,ajaapps} %{buildroot}/usr/libexec/ajantv2/

%files
%doc LICENSE README.md
/usr/bin/*
/usr/lib64/*
/usr/include/*
/usr/libexec/ajantv2
