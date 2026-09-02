import sys


if sys.platform.startswith('win32'):
    print('you are in windows')
elif sys.platform.startswith('darwin'):
    print('you are in macos')
elif sys.platform.startswith('linux'):
    print('you are in linux')


if sys.version.startswith('3.13.0') :
    print('the web site is runing')
else:
    print('python is old please update')

print('---------------------------------------------------')
