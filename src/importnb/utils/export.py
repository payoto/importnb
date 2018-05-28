# coding: utf-8
"""# The `export` module

...provides compatibility for Python and IPython through [`compile_python`](compile_python.ipynb) and [`compile_ipython`](compile_ipython.ipynb), respectively.  

    >>> from importnb.utils.export import export
"""

try:
    from ..decoder import loads, transform_cells
except:
    from importnb.decoder import loads, transform_cells

from pathlib import Path

try:
    from black import format_str
except:
    format_str = lambda x, i: x

def export(file, to=None):

    with open(str(file), "r") as f:
        code = "\n".join(
            format_str("".join(cell["source"]), 100)
            for cell in transform_cells(loads(f.read()))["cells"]
            if cell["cell_type"] == "code"
        )
    to and Path(to).with_suffix(".py").write_text("# coding: utf-8\n{}".format(code))
    return code

if __name__ == "__main__":
    export("export.ipynb", "../../utils/export.py")
    try:
        import export as this
    except:
        from . import export as this
    __import__("doctest").testmod(this, verbose=2)
