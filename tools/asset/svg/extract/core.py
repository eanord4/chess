"""Tools for extracting elements of source SVGs"""


#==== SETUP ====#

import bs4
from from_root import from_root
import os

from ...get_originals.core import originals_path, _originals_relpath
from tools.common.print import iprint




#==== DATA ====#

_extracted_relpath = os.path.join(
	"assets",
	"extracted",
	"svg",
)
extracted_path = from_root(_extracted_relpath)




#==== FUNCTIONS ====#

def load_original(filename="std_board.svg", indent: int = 0) -> bs4.BeautifulSoup:
	"""Load an original SVG as an XML-parsed BeautifulSoup"""

	# announce start
	repr_dirpath = os.path.join("", _originals_relpath)
	iprint(indent, f"Loading '{filename}' from '{repr_dirpath}'...")

	# load
	path = os.path.join(originals_path, filename)
	with open(path, "r") as f:
		contents = f.read()
	return bs4.BeautifulSoup(contents, "lxml")


def extract_desc(soup: bs4.BeautifulSoup, filename: str, indent: int = 0) -> None:
	"""Extract the SVG"s description element"""

	# announce start
	iprint(indent, "Extracting SVG description...")

	# extract
	e = soup.find("desc")
	path = os.path.join(extracted_path, filename)
	with open(path, "w") as f:
		f.write(e.text)

	# announce end
	repr_path = os.path.join("", _extracted_relpath, filename)
	iprint(indent + 1, f"Saved to '{repr_path}'.")


def extract_all(indent: int = 0) -> None:
	"""Perform all extractions of SVG elements of interest"""

	# announce start
	iprint(indent, "Extracting all elements of interest...")

	# load
	std_board_soup = load_original(indent=indent + 1)

	# extract
	extract_desc(std_board_soup, "std_board_desc.txt", indent=indent + 1)




#==== USAGE ====#

__all__ = [
	"load_original",
	"extract_desc",
	"extract_all",
]
