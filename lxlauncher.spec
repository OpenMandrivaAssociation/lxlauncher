Summary:	Open source replacement for Asus Launcher of EeePC
Name:		lxlauncher
Epoch:		1
Version:	0.2.2
Release:	8
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://lxde.sourceforge.net/
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
# fix looking for icon names containing a dot which does not mark an extension, like ooo-writer3.0
# to be submitted upstream
Patch2:	lxlauncher-0.2-iconext.patch
Patch13:	lxlauncher-0.2.2-gtk.patch
Requires:	desktop-common-data
Buildrequires:	gnome-common
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtk+-x11-2.0) intltool
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
Suggests:	nuoveXT2-icon-theme

%description
LXLauncher is part of LXDE project. It's designed for Asus EeePC as an
open source replacement for Asus Launcher included in EeePC provided by
Xandros. LXLauncher is standard-compliant and desktop-independent. It
follows freedesktop.org specs, so newly added applications will
automatically show up in the launcher, and vice versa for the removed ones.

%prep
%setup -q
%patch2 -p1 -b .iconext
%patch13 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxlauncher-applications.menu
%{_sysconfdir}/xdg/lxlauncher

