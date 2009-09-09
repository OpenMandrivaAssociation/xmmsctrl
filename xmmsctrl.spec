%define name	xmmsctrl
%define summary	Xmmsctrl is a small xmms control program
%define version	1.9
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
License:	GPL
Source0:	http://www.cs.aau.dk/~adavid/utils/%{name}-%{version}.tar.bz2
URL:		http://www.cs.aau.dk/~adavid/utils/
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libxmms-devel

%description
Xmmsctrl is a small utility to control xmms from the command line. 
Its goal is to be used coupled with sh to test xmms state and perform 
an appropriate action, e.g. if playing then pause else play. The 
interest of this is to bind keys in a window manager to have control 
over xmms with keys that do play/next/pause, prev, control sound...

%prep
rm -rf $RPM_BUILD_ROOT
%setup -n %{name}-%{version}

%build
%make

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755  %{name} %{buildroot}%{_bindir}/
chmod 755 samples/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc HELP Changelog README samples/ 
%{_bindir}/%{name}

