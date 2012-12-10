Summary:	Program Showing the Status of LSI FusionMPT RAID Controller
Name:		mpt-status
Version:	1.2.0
Release:	%mkrel 5
License:	GPLv2+
Group:          Monitoring
URL:		http://www.drugphish.ch/~ratz/mpt-status/
Source0:	http://www.drugphish.ch/~ratz/mpt-status/%{name}-%{version}.tar.gz
Source1:	mpt-status-cron.conf
Source2:	mpt-status.crond
Source3:	mpt-status-cron
Source4:	README.Mandriva
Patch0:		mpt-status.linux-compiler.patch
BuildRequires:	kernel-source-latest
Requires:	nail
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This program shows the status of the physical and logical drives attached to a
LSI FusionMPT RAID (mptlinux, fusion, mpt, ioc) controller.

%prep

%setup -q
%patch0 -p1

cp %{SOURCE1} mpt-status-cron.conf
cp %{SOURCE2} mpt-status.crond
cp %{SOURCE3} mpt-status-cron
cp %{SOURCE4} README.Mandriva

%build
gcc %{optflags} -I/usr/src/linux/drivers/message/fusion -Iincl mpt-status.c -o mpt-status

%install
rm -rf %{buildroot}

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/* README.Mandriva
%dir %{_sysconfdir}/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/mpt-status-cron.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/%{name}
%dir %{_datadir}/%{name}
%attr(0755,root,root) %{_datadir}/%{name}/mpt-status-cron
%{_bindir}/*
%{_mandir}/man?/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-5mdv2011.0
+ Revision: 620407
- the mass rebuild of 2010.0 packages

* Thu Oct 08 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.2.0-4mdv2010.0
+ Revision: 456190
- Force buildrequires of main kernel-source (build fix).

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Sep 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdv2009.0
+ Revision: 279148
- added lots of changes by acecile@mandriva.com

* Mon Sep 01 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2009.0
+ Revision: 278392
- fix group and descriptons

* Mon Sep 01 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdv2009.0
+ Revision: 278361
- import mpt-status


* Mon Sep 01 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1
- initial Mandriva package (suse import)

* Sun Aug 05 2007 - olh@suse.de
- remove inclusion of linux/compiler.h
* Tue Nov 14 2006 - mjancar@suse.cz
- update to 1.2.0
  * works on 64bit architectures (FATE #301702)
* Fri Apr 07 2006 - mjancar@suse.cz
- update to 1.1.6
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Aug 01 2005 - anicka@suse.cz
- package created
