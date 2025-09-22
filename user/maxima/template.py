pkgname = "maxima"
pkgver = "5.48.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-sbcl",
    "--with-gmp",
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
pkgdesc = "Computer algebra system based on Lisp"
license = "GPL-2.0-or-later"
url = "http://maxima.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "b0916b5fb37b6eeaae400083175e68e28f80b9a1ab580c106a05448cf1c496b2"
# take hours
options = ["!check"]

#def post_install(self):
#    # Pfad zur Source der Info-Dateien
#    src = self.files_path / "doc/info"

#    # Zielverzeichnis im Paket
#    dest = self.destdir / "usr/share/info"

    # sicherstellen, dass das Ziel existiert
#    self.do("mkdir", "-p", str(dest))

    # Index-Dateien erzeugen
#    with self.pushd(src):
#        self.do("perl", "./build_index.pl", "maxima.info", ":crlf")

#def check(self):
#    self.make.check()