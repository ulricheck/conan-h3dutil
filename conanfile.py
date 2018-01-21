import os
from conans import ConanFile, CMake, tools


class H3DUtilConan(ConanFile):
    name = "h3dutil"
    version = "1.4-beta"
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
        repo_url = "https://www.h3dapi.org:8090/H3DUtil/trunk/H3DUtil/"
        self.run("svn checkout %s source" % repo_url)
       
    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        # fix a compiler issue with pthread on vs 2015+
#         if self.settings.os == "Windows":
#             vs_version = int(str(self.settings.compiler.version))
#             if vs_version >=14:
#                 tools.replace_in_file("source/build/CMakeLists.txt", "INCLUDE_DIRECTORIES( ${PTHREAD_INCLUDE_DIR} )", '''INCLUDE_DIRECTORIES( ${PTHREAD_INCLUDE_DIR} )
# add_definitions(-DHAVE_STRUCT_TIMESPEC)''')

        cmake.configure(source_dir=os.path.join("source", "build"))
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern='*.h' , dst="include", src="source/include", keep_path=False)
        self.copy(pattern='*.cmake' , dst="cmake", src="source/cmake", keep_path=False)

    def package_info(self):
        if self.settings.arch == "x86":
            libfolder = "lib32"
        else:
            libfolder = "lib64"

        self.cpp_info.libs = tools.collect_libs(self, folder=libfolder)
