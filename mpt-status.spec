Summary:	Program Showing the Status of LSI FusionMPT RAID Controller
Name:		mpt-status
Version:	1.2.0
Release:	6
License:	GPLv2+
Group:		Monitoring
Url:		http://www.drugphish.ch/~ratz/mpt-status/
Source0:	http://www.drugphish.ch/~ratz/mpt-status/%{name}-%{version}.tar.gz
Source1:	mpt-status-cron.conf
Source2:	mpt-status.crond
Source3:	mpt-status-cron
Source4:	README.Mandriva
Patch0:		mpt-status.linux-compiler.patch
BuildRequires:	kernel-source-latest
Requires:	nail

%description
This program shows the status of the physical and logical drives attached to a
LSI FusionMPT RAID (mptlinux, fusion, mpt, ioc) controller.

%files
%doc doc/* README.Mandriva
%dir %{_sysconfdir}/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/mpt-status-cron.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/%{name}
%dir %{_datadir}/%{name}
%attr(0755,root,root) %{_datadir}/%{name}/mpt-status-cron
%{_bindir}/*
%{_mandir}/man?/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

cp %{SOURCE1} mpt-status-cron.conf
cp %{SOURCE2} mpt-status.crond
cp %{SOURCE3} mpt-status-cron
cp %{SOURCE4} README.Mandriva

%build
spath=%(find /usr/src/ -name mpi_type.h | sed s,"/lsi/mpi_type.h",,g)
gcc %{optflags} -I$spath -Iincl mpt-status.c -o mpt-status

%install
install -d %{buildroot}%{_sysconfdir}/cron.d
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man8

install -m0755 mpt-status %{buildroot}%{_bindir}
install -m0644 man/mpt-status.8 %{buildroot}%{_mandir}/man8

install -m0644 mpt-status-cron.conf %{buildroot}%{_sysconfdir}/%{name}/mpt-status-cron.conf
install -m0644 mpt-status.crond %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -m0755 mpt-status-cron %{buildroot}%{_datadir}/%{name}/mpt-status-cron

