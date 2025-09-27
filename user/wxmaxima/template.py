pkgname = "wxmaxima"
pkgver = "25.04.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_INSTALL_PREFIX=/usr",
    "-DCMAKE_INSTALL_DATADIR=/usr/share",
    "-DUSE_OPENMP=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
	"gettext-devel",
    "wxwidgets-devel",
]
depends = ["maxima"]
pkgdesc = "Graphische Oberfläche für Maxima basierend auf wxWidgets"
license = "GPL-2.0-or-later"
url = "https://wxmaxima-developers.github.io/wxmaxima"
source = f"https://github.com/wxMaxima-developers/wxmaxima/archive/refs/tags/Version-{pkgver}.tar.gz"
sha256 = "ec0b3005c3663f1bb86b0cc5028c2ba121e1563e3d5b671afcb9774895f4191b"
# test
options = ["!check"]

def post_install(self):
    self.install_license("COPYING")