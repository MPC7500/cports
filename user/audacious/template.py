pkgname = "audacious"
pkgver = "4.5.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libxml2-devel",
    "qt5-qtbase-devel",
    "qt5-qtsvg-devel",
]
pkgdesc = "Lightweight and versatile audio player"
license = "BSD-2-Clause"
url = "https://audacious-media-player.org"
source = f"https://distfiles.audacious-media-player.org/audacious-{pkgver}.tar.bz2"
sha256 = "SKIP"

def post_install(self):
    self.install_license("COPYING")