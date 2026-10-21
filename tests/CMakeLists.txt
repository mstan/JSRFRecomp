cmake_minimum_required(VERSION 3.20)
project(jsrf_visual_contract C)
enable_testing()
set(CMAKE_C_STANDARD 11)
set(XBOXLLR_ROOT "" CACHE PATH "Reviewed shared framework")
add_executable(jsrf_visual_contract visual_contract.c ../src/mods/visuals.c
  "${XBOXLLR_ROOT}/pilots/native-title/visual_mods.c"
  "${XBOXLLR_ROOT}/pilots/native-title/visual_mod_plan.c")
target_include_directories(jsrf_visual_contract PRIVATE "${XBOXLLR_ROOT}/pilots/native-title")
if(NOT WIN32)
  target_link_libraries(jsrf_visual_contract PRIVATE m)
endif()
foreach(mode disabled fixed adaptive)
  add_test(NAME jsrf_visual_${mode} COMMAND jsrf_visual_contract
    "${CMAKE_CURRENT_BINARY_DIR}/${mode}.plan" ${mode})
endforeach()
