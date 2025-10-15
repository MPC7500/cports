pkgname = "masscan"
pkgver = "1.3.2"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "git",
]
makedepends = [
    "libpcap-devel",
    "linux-headers",
]
depends = [
    "libpcap",
    "libpcap-devel",
]
pkgdesc = "Internet-scale port scanner"
license = "AGPL-3.0-only"
url = "https://github.com/robertdavidgraham/masscan"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0363e82c07e6ceee68a2da48acd0b2807391ead9a396cf9c70b53a2a901e3d5f"

def post_install(self):
	self.install_license("LICENSE")
	
def check(self):
    pass