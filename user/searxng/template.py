pkgname = "searxng"
pkgver = "2025.10.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
	"git",
    "python-build",
    "python-installer",
    "python-lxml",
    "python-pyyaml",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "python-devel",
]
depends = [
    "python-babel",
    "python-certifi",
    "python-dateutil",
    "python-flask",
#    "python-flask-babel",
#    "python-httpx",
    "python-jinja2",
    "python-lxml",
    "python-pygments",
    "python-pyyaml",
#    "python-redis",
    "python-setproctitle",
    "python-typing_extensions",
#    "python-uvloop",
#    "uwsgi-python",
]
pkgdesc = "Privacy-respecting metasearch engine"
license = "AGPL-3.0-or-later"
url = "https://github.com/searxng/searxng"
_commit = "cdf5f4343a18b40799dc4ab86ba5d791df0b27b2"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "ee7e932ccfd4a364e339f04d71a28a6fe9adf9122a1c5baaaee5c27b52b6b6bc"
# Skip test aiounittest n/a
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("etc/searxng")
    self.install_file(
        "searx/settings.yml",
        "etc/searxng",
        name="settings.yml.example"
    )