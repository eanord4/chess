"""Tools for extracting elements of source SVGs"""


#==== SETUP ====#

from bs4 import BeautifulSoup
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

def load_original(filename="std_board.svg") -> BeautifulSoup:
	"""Load an original SVG as an XML-parsed BeautifulSoup"""

	path = os.path.join(originals_path, filename)
	with open(path, "r") as f:
		contents = f.read()
	return BeautifulSoup(contents, "lxml")


def extract_all() -> None:
	"""Perform all extractions of SVG elements of interest"""

	raise NotImplementedError("No extractions available yet.")





#==== USAGE ====#

__all__ = [
	"load_original",
	"extract_all",
]
