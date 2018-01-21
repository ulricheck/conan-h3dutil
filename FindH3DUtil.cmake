#=============================================================================
# Copyright 2001-2011 Kitware, Inc.
#
# Distributed under the OSI-approved BSD License (the "License");
# see accompanying file Copyright.txt for details.
#
# This software is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the License for more information.
#=============================================================================
# (To distribute this file outside of CMake, substitute the full
#  License text for the above reference.)

find_path(H3DUTIL_INCLUDE_DIR NAMES H3DUTIL.h PATHS ${CONAN_INCLUDE_DIRS_H3DUTIL})
find_library(H3DUTIL_LIBRARY NAMES ${CONAN_LIBS_H3DUTIL} PATHS ${CONAN_LIB_DIRS_H3DUTIL})

MESSAGE("** H3DUTIL ALREADY FOUND BY CONAN!")
SET(H3DUTIL_FOUND TRUE)
MESSAGE("** FOUND H3DUTIL:  ${H3DUTIL_LIBRARY}")
MESSAGE("** FOUND H3DUTIL INCLUDE:  ${H3DUTIL_INCLUDE_DIR}")

set(H3DUTIL_INCLUDE_DIRS ${H3DUTIL_INCLUDE_DIR})
set(H3DUTIL_LIBRARIES ${H3DUTIL_LIBRARY})

mark_as_advanced(H3DUTIL_LIBRARY H3DUTIL_INCLUDE_DIR)