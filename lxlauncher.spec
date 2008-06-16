Summary:	Open source replacement for Asus Launcher of EeePC
Name:     	lxlauncher
Version:	0.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	libgnome-menu-devel
BuildRequires:	startup-notification-devel

%description
LXLauncher is part of LXDE project. It's designed for Asus EeePC as an
open source replacement for Asus Launcher included in EeePC provided by
Xandros. LXLauncher is standard-compliant and desktop-independent. It
follows freedesktop.org specs, so newly added applications will
automatically show up in the launcher, and vice versa for the removed ones.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post  

%postun

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/desktop-directories/*.directory
