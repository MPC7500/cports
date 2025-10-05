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
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "Lightweight and versatile audio player"
license = "BSD-2-Clause"
url = "https://audacious-media-player.org"
source = f"https://distfiles.audacious-media-player.org/audacious-{pkgver}.tar.bz2"
sha256 = "7194743a0a41b1d8f582c071488b77f7b917be47ca5e142dd76af5d81d36f9cd"

def post_install(self):
    self.install_license("COPYING")

@subpackage("audacious-devel")
def _(self):
    return self.default_devel()