Summary:	Open source replacement for Asus Launcher of EeePC
Name:     	lxlauncher
Version:	0.2
Release:	%mkrel 5
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
Patch0:		lxlauncher-0.2-mandriva-customization.patch
Patch1:		lxlauncher-0.2-nocharwrap.patch
# fix looking for icon names containing a dot which does not mark an extension, like ooo-writer3.0
# to be submitted upstream
Patch2:		lxlauncher-0.2-iconext.patch
Patch3:		lxlauncher-0.2-sysconf.patch
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	libgnome-menu-devel
Buildrequires:	gnome-common
BuildRequires:	startup-notification-devel
Requires:	desktop-common-data
Suggests:	nuoveXT2-icon-theme

%description
LXLauncher is part of LXDE project. It's designed for Asus EeePC as an
open source replacement for Asus Launcher included in EeePC provided by
Xandros. LXLauncher is standard-compliant and desktop-independent. It
follows freedesktop.org specs, so newly added applications will
automatically show up in the launcher, and vice versa for the removed ones.

%prep
%setup -q
%patch0 -p1 -b .mdv
%patch1 -p0 -b .charwrap
%patch2 -p1 -b .iconext
%patch3 -p1 -b .sysconf

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%dir %{_sysconfdir}/%{name}
%{_datadir}/%name
%{_datadir}/desktop-directories/*.directory
