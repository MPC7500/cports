pkgname = "maxima"
pkgver = "5.48.1"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--with-sbcl",
    "--with-gmp",
    "--prefix=/usr",
    "--infodir=/usr/share/info"
    "--mandir=/usr/share/man",
]
hostmakedepends = [
    "autoconf",
    "automake",
    "texinfo",
]
makedepends = [
    "gmp-devel",
    "readline-devel",
    "sbcl",
]
depends = [
    "gnuplot",
    "sbcl",
]
checkdepends = [
    "perl",
]
pkgdesc = "Computer algebra system based on Lisp"
license = "GPL-2.0-or-later"
url = "http://maxima.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "b0916b5fb37b6eeaae400083175e68e28f80b9a1ab580c106a05448cf1c496b2"
# take hours
options = ["!check"]

def post_install(self):
    self.install_file("doc/info/maxima-index.lisp",
        "usr/share/info", name="maxima-index.lisp")
    self.install_file("doc/info/maxima-index-html.lisp",
        "usr/share/info", name="maxima-index-html.lisp")

def check(self):
    self.make.check()