# git-confedclone
Changing git config according to repository urls. This helps you to  have various identities per organizations.

## Usage

1. `pip install git+https://github.com/pfnet/chainer.git` or `setup.py install`
2. write `~/.gitconfedclone` according to your environment
3. now `git confedclone https://github.com/xxxx/yyyy` do the trick

## Config

### example1: change your email according to the site

```yaml
- "github.yourcompany.com":
    - ".*":
        "user.name": "John Smith"
        "user.email": "john_smith@yourcompany.com"
- "github.com":
    - ".*":
        "user.name": "John Smith"
        "user.email": "john_smith@gmail.com"
- "bitbucket.org":
    - ".*":
        "user.name": "John Smith"
        "user.email": "john_smith@gmail.com"
```

### example2: change your name according to organization

```yaml
- "github.com":
    - "YOUR-OSS":
        "user.name": "John Smith"
        "user.email": "john_smith@gmail.com"
    - "Other-OSS":
        "user.name": "J.S."
        "user.email": "john_smith@gmail.com"
    - "John":
        "user.name": "J"
        "user.email": "john_smith@gmail.com"
```
