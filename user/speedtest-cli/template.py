pkgname = "speedtest-cli"
pkgver = "2.1.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
	"python",
	"python-build",
	"python-installer",
	"python-setuptools",
	"python-wheel"
]
depends = ["python"]
pkgdesc = "CLI for testing internet bandwidth using speedtest.net"
license = "Apache-2.0"
url = "https://github.com/sivel/speedtest-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "45e3ca21c3ce3c339646100de18db8a26a27d240c29f1c9e07b6c13995a969be"
# no test available
options = ["!check"]

def post_install(self):
	self.install_license("LICENSE")
