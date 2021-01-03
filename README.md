# my-python-project
Template repository for python-based projects:
- Container-based development ([VSCode Remote Container extension](https://code.visualstudio.com/docs/remote/containers) can be used)
- `Makefile` for build and run recipes
- Python depedency management with vanilla `pip` and `requirements.txt` file

## Basic make recipes
- `make install-depedencies` : write unpinned or pinned dependencies in `bootstrap.req.txt` and pin all library versions in `requirements.txt`
