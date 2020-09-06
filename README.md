# Standards Comparison Tool


## Changelog:

### 8/24-8/30 

**Major Changes:**

- Fixed issue where not selecting a file after pushing a button would cause the program to stop working
- Added Discovery Education logo as base64 image to allow it to be present in the program without the file being required
- Exported the script to Windows & MacOS executables
- Fixed issue where report generated on MacOS was created inside of the app package instead of the directory the program was in
- Fixed issue where MacOS executable would hang after pushing button

**Minor Changes/QOL:**

- Added toolbar icon to the Windows executable
- Changed the backslash to a forward slash on MacOS version to accurately represent the path

### 8/31 - 9/6:

**Major Changes:**

- Standard descriptions are now matched based upon their similarities instead of their position in their files

> In the original version of the script, the standard descriptions were written out in order. This means that the description from line 5 from the first document would be aligned with line 5 from the second document. With this change, the program now looks for which description is the closest to another, and then writes them out with each description having its closest match next to it. For this to work, the descriptions must be at least 50% similar to avoid matching standards with little similarity. Each description can only be matched with one other description, and standards with no match are now placed at the bottom.


**Minor Changes/QOL:**

- Removed print commands used for testing



