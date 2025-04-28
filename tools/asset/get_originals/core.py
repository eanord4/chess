"""Tools for obtaining original unmodified assets"""


#==== SETUP ====#

from chess import Board, svg
from from_root import from_root
import os




#==== DATA ====#

_originals_relpath = os.path.join(
	"assets",
	"originals",
)
originals_path = from_root(_originals_relpath)




#==== FUNCTIONS ====#

def std_board_svg(size: int) -> str:
	"""Make a standard starting chess board SVG from chess.com's `chess` package"""

	return svg.board(Board(), size=size)


def get_all() -> None:
	"""Obtain all original assets"""

	# announce start
	print("Getting original assets...")

	# standard board SVG
	filename = "std_board.svg"
	print(f"\n\tObtaining {filename}...")
	svg_str = std_board_svg(350)
	path = os.path.join(originals_path, filename)
	with open(path, "w") as f:
		f.write(svg_str)
	repr_path = os.path.join("", _originals_relpath, filename)
	print(f"\t\tSaved to '{repr_path}'")

	# announce end
	print("\nDone")




#==== USAGE ====#

__all__ = [

	# functions
	"std_board_svg",
	"get_all",

]
