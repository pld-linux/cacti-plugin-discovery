%define		namesrc	discovery
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Discovery
Summary(pl.UTF-8):	Wtyczka do Cacti - Discovery
Name:		cacti-plugin-discovery
Version:	0.8.4
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{namesrc}-%{version}.zip
# Source0-md5:	abefb45b806d0bc0074b6d9516a940a4
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - This plugin adds the ability to auto-discover
devices on a subnet that are not monitored by Cacti and and tells you
if they are SNMP enabled.

%description -l pl.UTF-8
Wtyczka do Cacti dodająca możliwość automatycznego wykrywania urządzeń
w podsieci jeszcze nie monitorowanych przez Cacti i informująca, czy
urządzenia mają włączone SNMP.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -a * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{webcactipluginroot}
