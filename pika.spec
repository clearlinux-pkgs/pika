#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pika
Version  : 1.1.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/8c/6d/a526ad96ffb8aa0d3ab7e8660eb1c9fc964a02e7624112d70e4b63fb2bb7/pika-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8c/6d/a526ad96ffb8aa0d3ab7e8660eb1c9fc964a02e7624112d70e4b63fb2bb7/pika-1.1.0.tar.gz
Summary  : Pika Python AMQP Client Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pika-license = %{version}-%{release}
Requires: pika-python = %{version}-%{release}
Requires: pika-python3 = %{version}-%{release}
Requires: tornado
BuildRequires : buildreq-distutils3
BuildRequires : tornado

%description
Pika
====
Pika is a RabbitMQ (AMQP 0-9-1) client library for Python.
|Version| |Python versions| |Status| |Coverage| |License| |Docs|

%package license
Summary: license components for the pika package.
Group: Default

%description license
license components for the pika package.


%package python
Summary: python components for the pika package.
Group: Default
Requires: pika-python3 = %{version}-%{release}

%description python
python components for the pika package.


%package python3
Summary: python3 components for the pika package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pika package.


%prep
%setup -q -n pika-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563423703
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pika
cp LICENSE %{buildroot}/usr/share/package-licenses/pika/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pika/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
