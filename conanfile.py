import shutil
import os
from conans.tools import download, unzip, check_md5, check_sha1, check_sha256
from conans import ConanFile, CMake, tools


class ConfuBoostConan(ConanFile):
    name = "confu_boost"
    version = "0.0.1"
    license = "BSL-1.0"
    author = "werto87"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "convenience functions for reducing boilerplate while working with boost"
    topics = ("boost boilerplate")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
    
    def requirements(self):
        self.requires("boost/1.75.0")
        self.requires("magic_enum/0.6.6")
        self.requires("catch2/2.13.1")

    def source(self):
        zip_name = "confu_boost"
        download("https://github.com/werto87/confu_boost/archive/v0.0.1.zip", zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="confu_boost-0.0.1")
        cmake.build()

    def package(self):
        self.copy("*.h*", dst="include/confu_boost",
                  src="confu_boost-0.0.1/confu_boost")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["confuBoost"]
