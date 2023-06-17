%define _libexecdir %_prefix/libexec
%define ver_major 1.0

Name: xdg-desktop-portal-xapp
Version: %ver_major.1
Release: alt2

Summary: Xapp Desktop Portal
License: LGPL-2.1-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/xdg-desktop-portal-xapp/

Source: %name-%version.tar

%define xdg_desktop_portal_ver 1.15.0

Requires: xdg-desktop-portal-gtk >= 1.14

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson libgtk4-devel pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(xdg-desktop-portal) >= %xdg_desktop_portal_ver
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libxapps-devel

%description
A backend implementation for xdg-desktop-portal that is using GTK
and various pieces of Cinnamon/MATE/Xfce4 infrastructure.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_libexecdir/%name
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.xapp.service
%_datadir/xdg-desktop-portal/portals/xapp.portal
%_userunitdir/%name.service
%doc README*


%changelog
* Sat Jun 17 2023 Andrey Vasilyev <andrey@crafted.su> 1.0.1-alt2
- Add a fix for using in WM like qtile

* Thu Jun 8 2023 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- first build for Sisyphus

