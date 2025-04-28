# A Chess Package

This repo aims to achieve exciting chess-related functionality with a lean setup. As of this project's inception, the primary goals are:
* To create novel chess exercises targeting key mental elements required for chess skill
* To create and enable the creation of novel chess variants
* To avoid dependence on weighty high-level features such as AI

Dependencies
* Python version: 3.10
* Packages: ./requirements.txt

The folder hierarchy and key files are explained as follow.
* /src: app production files
* /tools: scripts for use outside of production
	* /asset: scripts for obtaining and preparing assets which may be used for production. These scripts will generally have already been run, and the resulting files already included in /assets.
		* /get_originals: a packaged script for obtaining raw unmodified assets. To re-obtain all original assets: `python -m tools.asset.get_originals`
* /assets: files that have been gathered in preparation for creating the app
	* /originals: unmodified files obtained from somewhere external to this repo. The scripts used to obtain these are included in /tools/asset.
