# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/mnt/d/HSE/C++/Пояса/Yellow belt"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/mnt/d/HSE/C++/Пояса/Yellow belt/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Yellow_belt.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Yellow_belt.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Yellow_belt.dir/flags.make

CMakeFiles/Yellow_belt.dir/main.cpp.o: CMakeFiles/Yellow_belt.dir/flags.make
CMakeFiles/Yellow_belt.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/mnt/d/HSE/C++/Пояса/Yellow belt/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Yellow_belt.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Yellow_belt.dir/main.cpp.o -c "/mnt/d/HSE/C++/Пояса/Yellow belt/main.cpp"

CMakeFiles/Yellow_belt.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Yellow_belt.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/mnt/d/HSE/C++/Пояса/Yellow belt/main.cpp" > CMakeFiles/Yellow_belt.dir/main.cpp.i

CMakeFiles/Yellow_belt.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Yellow_belt.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/mnt/d/HSE/C++/Пояса/Yellow belt/main.cpp" -o CMakeFiles/Yellow_belt.dir/main.cpp.s

# Object files for target Yellow_belt
Yellow_belt_OBJECTS = \
"CMakeFiles/Yellow_belt.dir/main.cpp.o"

# External object files for target Yellow_belt
Yellow_belt_EXTERNAL_OBJECTS =

Yellow_belt: CMakeFiles/Yellow_belt.dir/main.cpp.o
Yellow_belt: CMakeFiles/Yellow_belt.dir/build.make
Yellow_belt: CMakeFiles/Yellow_belt.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/mnt/d/HSE/C++/Пояса/Yellow belt/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Yellow_belt"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Yellow_belt.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Yellow_belt.dir/build: Yellow_belt

.PHONY : CMakeFiles/Yellow_belt.dir/build

CMakeFiles/Yellow_belt.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Yellow_belt.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Yellow_belt.dir/clean

CMakeFiles/Yellow_belt.dir/depend:
	cd "/mnt/d/HSE/C++/Пояса/Yellow belt/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/mnt/d/HSE/C++/Пояса/Yellow belt" "/mnt/d/HSE/C++/Пояса/Yellow belt" "/mnt/d/HSE/C++/Пояса/Yellow belt/cmake-build-debug" "/mnt/d/HSE/C++/Пояса/Yellow belt/cmake-build-debug" "/mnt/d/HSE/C++/Пояса/Yellow belt/cmake-build-debug/CMakeFiles/Yellow_belt.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Yellow_belt.dir/depend

