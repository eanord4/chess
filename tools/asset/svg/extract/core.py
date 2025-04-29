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


def wrap_as_svg_per(e: bs4.element.Tag, ref: bs4.BeautifulSoup) -> bs4.element.Tag:
	"""Wrap an individual SVG element with an 'svg' tag given by a reference SVG soup"""

	ref_svg_attrs = ref.find("svg").attrs
	new_soup = bs4.BeautifulSoup("", "lxml")
	new_svg = new_soup.new_tag("svg", **ref_svg_attrs)
	new_svg.append(e)
	return new_svg


def extract_description(soup: bs4.BeautifulSoup, filename: str, indent: int = 0) -> None:
	"""Extract the SVG's description element"""

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


def extract_definitions(soup: bs4.BeautifulSoup, indent: int = 0) -> None:
	"""Extract each of the definitions from a chessboard SVG soup as its own SVG"""

	# announce start
	repr_extracted_path = os.path.join("", _extracted_relpath)
	iprint(indent, f"Extracting definitions to '{repr_extracted_path}'...")

	# extract
	elements = list(soup.find("defs").children)
	for i, e in enumerate(elements):

		# announce start
		iprint(indent + 1, f"{i + 1}/{len(elements)} {e['id']}...")

		# save
		to_save = str(wrap_as_svg_per(e, soup))
		filename = f"{e.name}_{e['id']}.svg"
		path = os.path.join(extracted_path, filename)
		with open(path, 'w') as f:
			f.write(to_save)

		# announce end
		iprint(indent + 2, f"Saved as '{filename}'.")

	# don't announce end


def extract_all(indent: int = 0) -> None:
	"""Perform all extractions of SVG elements of interest"""

	# announce start
	iprint(indent, "Extracting all elements of interest...")

	# load
	std_board_soup = load_original(indent=indent + 1)

	# extract
	extract_description(std_board_soup, "std_board_desc.txt", indent=indent + 1)
	extract_definitions(std_board_soup, indent=indent + 1)

	# announce end
	iprint(indent, "Done.")




#==== USAGE ====#

__all__ = [
	"load_original",
	"wrap_as_svg_per",
	"extract_description",
	"extract_definitions",
	"extract_all",
]
