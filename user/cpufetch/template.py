pkgname = "cpufetch"
pkgver = "1.06"
pkgrel = 0
build_style = "makefile"
make_use_env = True
makedepends = ["linux-headers"]
pkgdesc = "Simple yet fancy CPU architecture fetching tool"
license = "GPL-2.0-only"
url = "https://github.com/Dr-Noob/cpufetch"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b8ec1339cf3a3bb9325cde7fb0748dd609043e8d2938c292956da7e457bdb7d9"
# No test suite available
options = ["!check"]

def install(self):
    self.install_bin("cpufetch")
    self.install_man("cpufetch.1")
    self.install_license("LICENSE")