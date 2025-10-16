pkgname = "superfile"
pkgver = "1.4.0"
pkgrel = 0
build_style = "go"
hostmakedepends = [
    "go",
]
pkgdesc = "Modern and intuitive terminal file manager"
license = "MIT"
url = "https://github.com/yorukot/superfile"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aa3ad00b3b89023c413a47f4f518f419d37ed3646eac3e9cfaf53d31e5dee82e"
# no test available
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
