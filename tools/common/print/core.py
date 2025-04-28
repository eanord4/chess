#==== FUNCTIONS =====#

def iprint(indent: int, *args, spacing: int = 0, **kwargs) -> None:
	"""Print as usual but preceded with the specified number of tabs. Optionally, `spacing` can be provided to precede this with a specified number of newlines."""

	args = list(args)
	first_arg = args.pop(0)

	print("\n" * spacing + "\t" * indent + str(first_arg), *args, **kwargs)




#==== USAGE ====#

__all__ = [
	"iprint",
]
