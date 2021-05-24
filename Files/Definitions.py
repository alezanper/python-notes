## Files 
"""
Windows     C:\directory\file
Linux       /directory/files
ThisIsTheNameOfTheFile != thisisthenameofthefile    on Linux but the same on Windows
"""
name = "/dir/file"  # Unix/Linux
name = "\\dir\\file"  # Windows

# Windows ends files as
# CR and LF (ASCII codes 13 and 10) which can be encoded as \r\n.

# Linux ends files as
# LF (ASCII code 10) designated in Python programs as \n

