

cmake_minimum_required(VERSION 2.8)
project(url2msgid)

set(url2msgid_VERSION_MAJOR 1)
set(url2msgid_VERSION_MINOR 0)


set(c++version -std=c++11)


set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -lcrypto -Wall -Wextra -Weffc++ -pedantic -Wno-unused-function ${c++version}")

set(CMAKE_BUILD_TYPE Release)

set(SOURCE_FILES
        bignumber.cpp MyBigNumber.cpp CharIdMap.cpp Url2Msgid.cpp main.cpp )



add_executable(url2msgid ${SOURCE_FILES})
