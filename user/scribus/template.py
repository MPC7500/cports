pkgname = "scribus"
pkgver = "1.6.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWANT_GRAPHICSMAGICK=1",
    "-DWANT_HUNSPELL=1",
    "-DWANT_NOOSG=1",
]
hostmakedepends = [
    "cmake",
    "dinit-chimera",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "cairo-devel",
    "cups-devel",
    "fontconfig-devel",
    "freetype-devel",
    "graphicsmagick-devel",
    "harfbuzz-devel",
    "hunspell-devel",
    "lcms2-devel",
    "libcdr-devel",
    "libfreehand-devel",
    "libjpeg-turbo-devel",
    "libmspub-devel",
    "libpagemaker-devel",
    "libpng-devel",
    "libqxp-devel",
    "libtiff-devel",
    "libvisio-devel",
    "libxml2-devel",
    "openssl3-devel",
    "poppler-devel",
    "python-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "zlib-ng-compat-devel",
]
depends = [
    "ghostscript",
    "python-pillow",
]
pkgdesc = "Professional desktop publishing software"
license = "GPL-2.0-or-later"
url = "https://www.scribus.net"
source = f"$(SOURCEFORGE_SITE)/scribus/scribus-{pkgver}.tar.xz"
sha256 = "533be7af03acfaa736ec5f7a3fc2562abd200fef5ca2a7cdee02b5f44d61829e"
# Tests require X11 display
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")