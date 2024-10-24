# git snapshot
%global snapshot 1
%if 0%{?snapshot}
	%global commit		983caa8047f79578d65d0126a7d68179858ab373
	%global commitdate	20240729
	%global shortcommit	%(c=%{commit}; echo ${c:0:7})
%endif

Summary:	Open source replacement for Asus Launcher of EeePC
Name:		lxlauncher
Version:	0.2.6
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://lxde.sourceforge.net/
#Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
Source0:	https://github.com/lxde/%{name}/archive/%{?snapshot:%{commit}}%{!?snapshot:%{version}}/%{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}.tar.gz
# fix looking for icon names containing a dot which does not mark an extension, like ooo-writer3.0
# to be submitted upstream
Patch2:	lxlauncher-0.2-iconext.patch
Patch13:	lxlauncher-0.2.2-gtk.patch

Buildrequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	locales-extra-charsets
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gconf-2.0)
#BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	pkgconfig(libmenu-cache)
BuildRequires:	pkgconfig(libstartup-notification-1.0)

Requires:	desktop-common-data

Suggests:	nuoveXT2-icon-theme

%description
Lightweight X11 Desktop Environment project (a.k.a LXDE) aimed to provide a
new desktop environment which is useful enough and keep resource usage lower
at the same time. Useabiliy, speed, and memory usage are our main concern.

Unlike other tightly integrated desktops LXDE strives to be modular, so each
component can be used independently with few dependencies. This makes
porting LXDE to different distributions and platforms easier.

LXLauncher is designed for Asus EeePC as an open source replacement for Asus
Launcher included in EeePC provided by Xandros. LXLauncher is
standard-compliant and desktop-independent. It follows freedesktop.org
specs, so newly added applications will automatically show up in the
launcher, and vice versa for the removed ones.

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/desktop-directories/lxde-*.directory
%{_sysconfdir}/xdg/menus/lxlauncher-applications.menu
%{_sysconfdir}/xdg/lxlauncher
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{?snapshot:%{commit}}%{!?snapshot:%{version}}

%build
autoreconf -fiv
%configure \
	--enable-gtk3 \
	%{nil}
%make_build

%install
%make_install

# locales
%find_lang %{name}

