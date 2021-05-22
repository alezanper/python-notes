from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

print(platform())   # Windows-10-10.0.19041-SP0
print(platform(1))  # Windows-10-10.0.19041-SP0
print(platform(0, 1))   # Windows-10
print(machine())	# shows the processor AMD64
print(processor())	# Intel64 Family 6 Model 142 Stepping 11, GenuineIntel
print(system())		# returns operating system, like windows or linux
print(version())	# returns something like 10.0.19041
print(python_implementation())		# something like CPython
print(python_version_tuple())		#('3', '8', '5')
