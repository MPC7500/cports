pkgname = "codeblocks"
pkgver = "25.03"
pkgrel = 0
pkgdesc = "Free, open-source, cross-platform C, C++, and Fortran IDE"
license = "GPL-3.0-or-later"
url = "https://www.codeblocks.org"
source = [f"https://sourceforge.net/code-snapshots/svn/c/co/codeblocks/code/codeblocks-code-r13682-trunk.zip"]
sha256 = ["8fbfe6e75c814766286811560d0c749bf42a7be08d475205ac849d519103b1f0"]

# No test suite available
options = ["!check"]

build_style = "gnu_configure"
configure_args = [
    "--prefix=/usr",
    "--with-contrib-plugins=all",
    "--enable-shared",
    "--disable-static",
    "--disable-werror",
]
hostmakedepends = [
    "pkgconf",
    "automake",
    "autoconf",
    "libtool",
    "gettext",
    "gmake",
    "zip",
]
makedepends = [
    "wxwidgets-devel",
    "libzip-devel",
    "hunspell-devel",
    "tinyxml2-devel",
    "zlib-ng-devel",
    "glib-devel",
    "gtk+3-devel",
    "boost-devel",
]
depends = [
    "wxwidgets",
    "libzip",
    "hunspell",
    "tinyxml2",
    "gcc",
    "glib",
    "gtk+3",
]

def prepare(self):
    self.do("sh", "bootstrap")

def post_install(self):
    self.install_license("COPYING")