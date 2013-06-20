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
BuildRequires:	pkgconfig(gtk+-x11-2.0) intltool
BuildRequires:	pkgconfig(libmenu-cache)
Buildrequires:	gnome-common
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(gconf-2.0)
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


%changelog
* Tue Aug 02 2011 Александр Казанцев <kazancas@mandriva.org> 1:0.2.2-2
+ Revision: 692918
- update to 0.2.2

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.2.1-4mdv2011.0
+ Revision: 612786
- the mass rebuild of 2010.1 packages

* Wed Jun 09 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:0.2.1-3mdv2010.1
+ Revision: 547800
- add patch from upstream to fix segfault with libmenu-cache-3.0, should fix (mdv #59717)

* Sun Feb 28 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:0.2.1-2mdv2010.1
+ Revision: 512523
- rebuild for new menu-cache

* Fri Jul 10 2009 Funda Wang <fwang@mandriva.org> 1:0.2.1-1mdv2010.0
+ Revision: 394058
- fix file list
- no more autogen needed
- New version 0.2.1

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 0.3-0.1198.1mdv2009.1
+ Revision: 336578
- New snapshot

* Wed Dec 24 2008 Funda Wang <fwang@mandriva.org> 0.3-0.1109.1mdv2009.1
+ Revision: 318314
- customization patch not needed
- update to upstream svn snapshot
- rediff some patches

* Tue Nov 18 2008 Olivier Blin <blino@mandriva.org> 0.2-10mdv2009.1
+ Revision: 304048
- buildrequires libGConf2-devel
- shift background if /apps/lxlauncher/repos_background is true
- add experimental gconf support

* Fri Nov 14 2008 Olivier Blin <blino@mandriva.org> 0.2-9mdv2009.1
+ Revision: 303145
- name label and box button widgets according to the menu id (so that they can be customized per-menu-group in gtkrc)

* Sun Nov 02 2008 Olivier Blin <blino@mandriva.org> 0.2-8mdv2009.1
+ Revision: 299283
- use icons from /usr/share/icons/large when they exist (to support Mandriva icon policy)

* Fri Oct 17 2008 Olivier Blin <blino@mandriva.org> 0.2-7mdv2009.1
+ Revision: 294698
- if set, reuse bg_pixmap from main window as tab background
- fix viewport pointer type
- use full button size for button labels (workarounds OpenOffice.org being cut)

* Thu Oct 02 2008 Olivier Blin <blino@mandriva.org> 0.2-6mdv2009.0
+ Revision: 290949
- add backgrounds support back

* Mon Sep 29 2008 Olivier Blin <blino@mandriva.org> 0.2-5mdv2009.0
+ Revision: 289806
- load gtkrc/launcher.menu from /etc/lxlauncher if available

* Sun Sep 28 2008 Olivier Blin <blino@mandriva.org> 0.2-4mdv2009.0
+ Revision: 289031
- fix looking for icon names containing a dot which does not mark an extension, like ooo-writer3.0
- fix typo

* Sat Sep 27 2008 Funda Wang <fwang@mandriva.org> 0.2-3mdv2009.0
+ Revision: 288871
- change line wrap style

* Sat Sep 27 2008 Funda Wang <fwang@mandriva.org> 0.2-2mdv2009.0
+ Revision: 288866
- add desktop-direcoties customiztion

* Mon Jun 16 2008 Funda Wang <fwang@mandriva.org> 0.2-1mdv2009.0
+ Revision: 219477
- import lxlauncher


