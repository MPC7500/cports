pkgname = "xfce4-notes-plugin"
pkgver = "1.11.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "gtk+3-devel",
    "gtksourceview4-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce notes panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-notes-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-notes-plugin/{pkgver[:-2]}/xfce4-notes-plugin-{pkgver}.tar.bz2"
sha256 = "8301fcd397bbc98a3def3d94f04de30cc128b4a35477024d2bcb2952a161a3b5"
