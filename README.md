# pin
Introduction to intel pin tool

## Setup
Find the correct download here: https://software.intel.com/en-us/articles/pintool-downloads. This example was tested on Kali linux. Untar the file. I built my tool under the MyPinTool directory at .../pin-3.2-81205-gcc-linux/source/tools/MyPinTool.

## Running the tool
Drop the syscall tool into the MyPinTool directory. Open makefile.rules with your favorite text editor and change the target of the TEST_TOOL_ROOTS to the example syscall tool. Then:

```
make
../../../pin -t obj-intel64/syscalltest.so -- python http.py
```