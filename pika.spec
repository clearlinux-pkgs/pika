#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pika
Version  : 0.10.0
Release  : 14
URL      : https://pypi.python.org/packages/source/p/pika/pika-0.10.0.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pika/pika-0.10.0.tar.gz
Summary  : Pika Python AMQP Client Library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pika-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Pika, an AMQP 0-9-1 client library for Python
=============================================

%package python
Summary: python components for the pika package.
Group: Default

%description python
python components for the pika package.


%prep
%setup -q -n pika-0.10.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
