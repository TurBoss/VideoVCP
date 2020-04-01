# Video VCP - computer vision


Video VCP - Test computer vision features

## Download LinuxCNC ISO

Install linuxcnc using the stretch iso

http://www.linuxcnc.org/testing-stretch-rtpreempt/ 

once boot upgrade to linuxcnc version 2.8 or master

### Dependencies

```
$ sudo apt install python-pyqt5 python-pyqt5.qtquick python-dbus.mainloop.pyqt5 python-pyqt5.qtopengl python-pyqt5.qsci python-pyqt5.qtmultimedia qml-module-qtquick-controls gstreamer1.0-plugins-bad libqt5multimedia5-plugins pyqt5-dev-tools python-dev python-setuptools python-pip git python-opencv
```

## VCP Installation

there are two ways to install the video_vcp "quick install" or "developer"

### Quick Install

This will install the video_vcp and allow you to use it

```
$ pip install --user git+https://github.com/kcjengr/qtpyvcp.computer-vision.git
$ pip install --user git+https://github.com/TurBoss/video_vcp.git
```

### Developer Install

This will install the video_vcp from a local directory allowing us to make any modifications
without having to reinstall each time


clone the video_vcp repository

```
$ git clone https://github.com/TurBoss/video_vcp.git
$ git clone https://github.com/kcjengr/qtpyvcp.computer-vision.git
```

Install the computer vision widget

```
$ cd qtpyvcp.computer-vision
$ pip install -e .
$ cd ..

```


Install localy using pip.

```
$ cd video_vcp
$ pip install -e .
$ cd ..
```

Now you can run editvcp to edit the interface.

```
$ editvcp video_vcp
```


## Running the VideoVCP

plug your camera and make sure its show in /dev/video0 or /dev/video1

then run 

```
$ linuxcnc video_vcp/linuxcnc/configs/sim.video_vcp/xyz.ini

```


## Documentation

QtPyVCP [documentation](https://kcjengr.github.io/qtpyvcp/).


## Resources

* [Development](https://github.com/TurBoss/video_vco/)
* [Documentation](https://kcjengr.github.io/qtpyvcp/)
* [Freenode IRC](http://webchat.freenode.net/?channels=%23hazzy) (#hazzy)
* [The Matrix](https://riot.im/app/#/room/#qtpyvcp:matrix.org) (#qtpyvcp:matrix.org)
* [Gitter](https://gitter.im/kcjengr/qtpyvcp)
* [Discord](https://discord.gg/463hMhd)
* [Issue Tracker](https://github.com/TurBoss/video_vcp/issues)


## Dependancies

* [LinuxCNC](https://linuxcnc.org)
* Python 2.7
* PyQt5 or PySide2
* [QtPyVCP](https://qtpyvcp.kcjengr.com/)

VideoVCP is developed and tested using the LinuxCNC Debian 9 and 10

It should run on any system that can have PyQt5 installed, but Debian 9 and 10 arr the only OS
that are officially supported.


## DISCLAIMER

THE AUTHORS OF THIS SOFTWARE ACCEPT ABSOLUTELY NO LIABILITY FOR
ANY HARM OR LOSS RESULTING FROM ITS USE.  IT IS _EXTREMELY_ UNWISE
TO RELY ON SOFTWARE ALONE FOR SAFETY.  Any machinery capable of
harming persons must have provisions for completely removing power
from all motors, etc, before persons enter any danger area.  All
machinery must be designed to comply with local and national safety
codes, and the authors of this software can not, and do not, take
any responsibility for such compliance.

This software is released under the GPLv2.