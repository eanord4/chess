"""Tools for extracting elements of source SVGs"""


#==== SETUP ====#

import bs4
from from_root import from_root
import os




#==== DATA ====#

originals_path = from_root(
	"assets",
	"originals",
)

extracted_relpath = os.path.join(
	"assets",
	"extracted",
)

extracted_path = from_root(extracted_relpath)




#==== FUNCTIONS ====#

def load_original(filename="std_board.svg") -> bs4.BeautifulSoup:
	"""Load an original SVG as an XML-parsed BeautifulSoup"""

	path = os.path.join(originals_path, filename)
	with open(path, "r") as f:
		contents = f.read()
	return bs4.BeautifulSoup(contents, "lxml")


def extract_all() -> None:
	"""Perform all extractions of SVG elements of interest"""

	raise NotImplementedError("No extractions available yet.")





#==== USAGE ====#

__all__ = [
	"load_original",
	"extract_all",
]
