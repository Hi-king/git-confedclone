from setuptools import setup
setup(
    name="git-confedclone",
    version="1.0.0",
    py_modules=['git_confedclone'],
    entry_points={
        "console_scripts": ["git-confedclone = git_confedclone:main"]
    }
)
