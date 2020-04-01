from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="video_vcp",
    version="0.0.1",
    author="TurBoss",
    author_email="j.l.toledano.l@gmail.com",
    description="Video VCP - Computer Vision VCP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TurBoss/video-vcp",
    download_url="https://github.com/TurBoss/video-vcp/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'video_vcp=video_vcp:main',
        ],
        'qtpyvcp.vcp': [
            'video_vcp=video_vcp',
        ],
    },
    install_requires=[
	'qtpyvcp',
    ],
)
