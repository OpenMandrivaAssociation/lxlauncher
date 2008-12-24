%define svn 1109

Summary:	Open source replacement for Asus Launcher of EeePC
Name:     	lxlauncher
Version:	0.3
Release:	%mkrel -c %svn 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version-r%svn.tar.bz2
Patch0:		lxlauncher-0.3-mandriva-customization.patch
Patch1:		lxlauncher-0.3-nocharwrap.patch
# fix looking for icon names containing a dot which does not mark an extension, like ooo-writer3.0
# to be submitted upstream
Patch2:		lxlauncher-0.2-iconext.patch
Patch3:		lxlauncher-0.2-sysconf.patch
Patch4:		lxlauncher-0.2-background.patch
Patch5:		lxlauncher-0.2-buttonsize.patch
Patch6:		lxlauncher-0.2-vptr.patch
# (blino) if set, reuse bg_pixmap from main window as tab background
Patch7:		lxlauncher-0.2-main_bg_pixmap.patch
Patch8:		lxlauncher-0.2-largeicons.patch
Patch9:		lxlauncher-0.2-labelname.patch
Patch10:	lxlauncher-0.2-gconf.patch
Patch11:	lxlauncher-0.2-shift_background.patch
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
%setup -q -n %name
#patch0 -p1 -b .mdv
%patch1 -p0 -b .charwrap
%patch2 -p1 -b .iconext
#patch3 -p1 -b .sysconf
#patch4 -p1 -b .background
#patch5 -p1 -b .buttonsize
#patch6 -p1 -b .vptr
#patch7 -p1 -b .main_bg_pixmap
#patch8 -p1 -b .largeicons
#patch9 -p1 -b .labelname
#patch10 -p1 -b .gconf
#patch11 -p1 -b .shift_background

%build
NOCONFIGURE=1 ./autogen.sh
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
%{_datadir}/%name
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxlauncher-applications.menu
