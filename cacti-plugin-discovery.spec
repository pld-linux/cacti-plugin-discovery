%define		namesrc	discovery
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Discovery
Summary(pl):	Wtyczka do Cacti - Discovery
Name:		cacti-plugin-discovery
Version:	0.5
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	f6c7a244346eb3924f72fa344a7d00e3
URL:		http://www.cactiusers.org/
#BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - This plugin adds the ability to auto-discover
devices on a subnet that are not monitored by Cacti and and tells you
if they are SNMP enabled.

%description -l pl
Wtyczka do Cacti dodaj±ca mo¿liwo¶æ automatycznego wykrywania urz±dzeñ
w podsieci jeszcze nie monitorowanych przez Cacti i informuj±ca, czy
urz±dzenia maj± w³±czone SNMP.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{webcactipluginroot}
