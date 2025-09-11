pkgname = "abook"
pkgver = "0.6.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-vcard",
    "--with-ncurses",
    "--with-readline",
]
hostmakedepends = ["autoconf", "automake", "gettext-devel", "libtool", "pkgconf"]
makedepends = ["ncurses-devel", "readline-devel"]
pkgdesc = "Text-based address book program"
license = "GPL-2.0-or-later"
url = "https://abook.sourceforge.io"
source = f"https://abook.sourceforge.io/devel/abook-{pkgver}.tar.gz"
sha256 = "f0a90df8694fb34685ecdd45d97db28b88046c15c95e7b0700596028bd8bc0f9"
# No check - requires manual interaction
options = ["!check"]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    # Manpage installieren (falls nicht automatisch installiert)
    self.install_man("abook.1")