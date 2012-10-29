%define		plugin discovery
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Plugin for Cacti - Discovery
Summary(pl.UTF-8):	Wtyczka do Cacti - Discovery
Name:		cacti-plugin-%{plugin}
Version:	1.5
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:%{plugin}-v%{version}-1.tgz
# Source0-md5:	ed283c999d5c71a99f1e48d71d8f9913
URL:		http://docs.cacti.net/plugin:discovery
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	cacti(pia) >= 2.8
Requires:	php(core) >= %{php_min_version}
Requires:	php(mysql)
Requires:	php(pcre)
Requires:	php-date
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
This plugin adds the ability to auto-discover devices on a subnet that
are not monitored by Cacti and and tells you if they are SNMP enabled.

%description -l pl.UTF-8
Wtyczka do Cacti dodająca możliwość automatycznego wykrywania urządzeń
w podsieci jeszcze nie monitorowanych przez Cacti i informująca, czy
urządzenia mają włączone SNMP.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
