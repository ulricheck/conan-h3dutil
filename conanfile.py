import os
from conans import ConanFile, CMake, tools


class H3DUtilConan(ConanFile):
    name = "h3dutil"
    version = "1.3"
    url = "https://github.com/ulricheck/conan-h3dutil.git"

    short_paths = True
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "FindH3DUTIL.txt"
    options = {"shared": [True, False]}
    default_options = "shared=True"

    # exports = "*"

    def requirements(self):
        if self.settings.os == "Windows":
            self.requires("h3dapi_windows_dependencies/[>=2.3]@camposs/stable")

    def source(self):
        repo_url = "https://www.h3dapi.org:8090/H3DUtil/branches/release%s/ source" % self.version
        self.run("git svn clone %s source" % repo_url)
       
    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(source_dir=os.path.join("source", "build"))
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern='*.h' , dst="include", src="package/include", keep_path=False)
        self.copy(pattern='*.cmake' , dst="cmake", src="package/cmake", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="package/lib", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src="package/lib", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src="package/lib", keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", src="package/lib", keep_path=False)  


    def package_info(self):
        # self.cpp_info.defines.append("HAVE_H3DUTIL")
        h3d_modules = ["h3dutil"]

        suffix = ""
        if self.settings.build_type == "Debug":
            suffix = "d"
        for lib in h3d_modules:
            self.cpp_info.libs.append("%s%s" % (lib, suffix))
