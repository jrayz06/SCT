# Standards Comparison Tool


## Changelog:

### 8/24-8/30 

**Major Changes:**

- Fixed issue where not selecting a file after pushing a button would cause the program to stop working
- Added Discovery Education logo as base64 image to allow it to be present in the program without the file being required
- Exported the script to Windows & MacOS executables
- Fixed issue where report generated on MacOS was created inside of the app package instead of the directory the program was in
- Fixed issue where MacOS executable would hang after pushing button

**Minor Changes/Bug Fixes/QOL:**

- Added toolbar icon to the Windows executable
- Changed the backslash to a forward slash on MacOS version to accurately represent the path

### 8/31 - 9/5:

**Major Changes:**

- Standard descriptions are now matched based upon their similarities instead of their position in their files

> In the original version of the script, the standard descriptions were written out in order. This means that the description from line 5 from the first document would be aligned with line 5 from the second document. With this change, the program now looks for which description is the closest to another, and then writes them out with each description having its closest match next to it. For this to work, the descriptions must be at least 50% similar to avoid matching standards with little similarity. Each description can only be matched with one other description, and standards with no match are now placed at the bottom.


**Minor Changes/Bug Fixes/QOL:**

- Removed print commands used for testing

###9/6 - 9/12###

**Major Changes:**

- New standards, removed standards, and the individual alignment of the standards are now listed in the rightmost columns

- Removed "mostly similar" and "changed standard name" entries at the top of the list

> Before the script aligned the standards in each row, the method to determine if a standard name had changed would be to compare a standard name in one row to another in the same row. Since the standards were not aligned by similarity but row number, some standards may have been marked to have a name change due to not being in the same order. This change ensures that standards whose names have changed or remained the same are properly tracked.

**Minor Changes/Bug Fixes/QOL:**

- Fixed error where the program would not execute properly if the file selection window was closed by requiring the user to choose a file before proceeding

- Fixed error where standards were not aligned by similarity if the length of the second file's list was larger than the first's


