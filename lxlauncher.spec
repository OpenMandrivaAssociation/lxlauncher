Summary:	Open source replacement for Asus Launcher of EeePC
Name:     	lxlauncher
Epoch:		1
Version:	0.2.2
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
# fix looking for icon names containing a dot which does not mark an extension, like ooo-writer3.0
# to be submitted upstream
Patch2:		lxlauncher-0.2-iconext.patch
Patch13:	lxlauncher-0.2.2-gtk.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	menu-cache-devel
Buildrequires:	gnome-common
BuildRequires:	startup-notification-devel
BuildRequires:	libGConf2-devel
Requires:	desktop-common-data
Suggests:	nuoveXT2-icon-theme

%description
LXLauncher is part of LXDE project. It's designed for Asus EeePC as an
open source replacement for Asus Launcher included in EeePC provided by
Xandros. LXLauncher is standard-compliant and desktop-independent. It
follows freedesktop.org specs, so newly added applications will
automatically show up in the launcher, and vice versa for the removed ones.

%prep
%setup -q -n %name-%version
%patch2 -p1 -b .iconext
%patch13 -p0

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxlauncher-applications.menu
%{_sysconfdir}/xdg/lxlauncher
