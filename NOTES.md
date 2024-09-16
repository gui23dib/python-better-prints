# TODO

    - make detailedPrint usable
    - implement colors and enum

## Setup tools step by step

    '''
    pip install setuptools wheel twine
    py setup.py sdist bdist_wheel
    pip install dist/betterprints-0.1-py3-none-any.whl --force-reinstall
    twine upload dist/*
    '''
