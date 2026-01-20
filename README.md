# OpenCV Testing

## Nix

Using direnv opening a terminal in the current directory will do the following:

- Use `flake.nix` and load the packages
- Use the layout, uv, in the `.envrc` file
- Able to run `python3 main.py` almost natively

Cd'ing out the directory removes this and then cd'ing back into it will reload the environment.

## UV/Venv 

If you are using this without Nix, then:

```bash
# uv -> by astral
$ uv sync
# or venv -> by python
$ python3 -m pip install -r requirements.txt
```

Simply done.
