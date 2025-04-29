"""Tools for SVG mappings"""


#==== SETUP ====#

import os
from from_root import from_root
import json
from tools.common.print import iprint
from typing import Optional




#==== DATA ====#

_mappings_relpath = os.path.join(
	"assets",
	"mappings",
	"svg",
)
mappings_path = from_root(_mappings_relpath)
labeling_filename = "svg_labeling.json"




#==== FUNCTIONS ====#


def update_label(filename: str, indent: int = 0, i: Optional[int] = None, out_of: Optional[int] = None) -> None:
	"""Update the label for a given filename"""

	# load existing mapping
	path = os.path.join(mappings_path, labeling_filename)
	with open(path, 'r') as f:
		content = f.read()
	mapping = json.loads(content)

	# get input
	start = f"{i + 1}/{out_of} " if i else ""
	iprint(indent, f"{start}Label for '{filename}': ", end="")
	label = input()

	# update
	mapping[filename] = label
	updated_content = json.dumps(mapping)
	with open(path, 'w') as f:
		f.write(updated_content)

	# announce end
	iprint(indent + 1, f"Update mapping '{filename}' => '{label}'.")


def label_all(dirpath: str, indent: int = 0) -> None:
	"""Update SVG mappings for all files in the given folder whose names contain '_unlabeled_'."""

	# announce start
	iprint(indent, f"Prompting labels for unlabeled files in '{dirpath}'...")

	# update
	filenames = [
		filename
		for filename in os.listdir(dirpath)
		if "_unlabeled_" in filename
	]
	for i, filename in enumerate(filenames):
		path = os.path.join(dirpath, filename)
		os.system(f'open "{path}"')
		update_label(filename, indent=indent + 1, i=i, out_of=len(filenames))

	# announce end
	iprint(indent, "Done.")


#==== USAGE ====#

__all__ = [
	"update_label",
	"label_all",
]
