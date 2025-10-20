pkgname = "tellico"
pkgver = "4.1.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_YAZ=OFF",
    "-DENABLE_WEBCAM=OFF",
    "-DBUILD_TESTING=OFF",
]
hostmakedepends = [
	"clang",
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "git",
    "ninja",
    "pkgconf",
    "qt6-qttools",
]
makedepends = [
    "boost-devel",
    "exempi-devel",
    "karchive-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemmodels-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kparts-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libcdio-devel",
    "libexif-devel",
    "liblangtag-devel",
    "libxml2-devel",
    "libxslt-devel",
    "poppler-devel",
    "qt6-qtbase-devel",
    "qt6-qtcharts-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwebengine-devel",
    "solid-devel",
    "sonnet-devel",
]
depends = [
    "kio",
    "qt6-qtbase",
]
pkgdesc = "Collection manager for books, videos, music, coins, stamps etc"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://tellico-project.org"
source = f"{url}/files/{pkgname}-{pkgver}.tar.xz"
sha256 = "6cac452bc10480d50fb0e33c74829aec1ce9880aef39d8b7fdf63bc5a85b3a4f"
  
def post_install(self):
    self.install_license("COPYING")