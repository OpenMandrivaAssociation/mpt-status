Summary:	Program Showing the Status of LSI FusionMPT RAID Controller
Name:		mpt-status
Version:	1.2.0
Release:	%mkrel 2
License:	GPLv2+
Group:          Monitoring
URL:		http://www.drugphish.ch/~ratz/mpt-status/
Source0:	http://www.drugphish.ch/~ratz/mpt-status/%{name}-%{version}.tar.gz
Patch0:		mpt-status.linux-compiler.patch
BuildRequires:	kernel-source
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This program shows the status of the physical and logical drives attached to a
LSI FusionMPT RAID (mptlinux, fusion, mpt, ioc) controller.

%prep

%setup -q
%patch0 -p1

%build
gcc %{optflags} -I/usr/src/linux/drivers/message/fusion -Iincl mpt-status.c -o mpt-status

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 mpt-status %{buildroot}%{_bindir}
install -m0644 man/mpt-status.8 %{buildroot}%{_mandir}/man8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/*
%{_bindir}/*
%{_mandir}/man?/*

