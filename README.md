
<a href="https://codecov.io/gh/isys35/pyteledantic">
  <img src="https://codecov.io/gh/isys35/pyteledantic/branch/master/graph/badge.svg?token=OJ3FYTM2TE"/>
</a>
<a href="https://pypi.org/project/pyteledantic/">
  <img src="https://img.shields.io/pypi/dm/pyteledantic"/>
</a>
<a href="https://pypi.org/project/pyteledantic/">
  <img src="https://img.shields.io/pypi/v/pyteledantic"/>
</a>
<a href="https://github.com/isys35/pyteledantic">
  <img src="https://img.shields.io/github/last-commit/isys35/pyteledantic"/>
</a>
<h1>Pydantic models for Telegram Bot API</h1>


Install:

```pip install pyteledantic```


<h3>How to use</h3>

<h4>FastAPI</h4>


````python
from fastapi import FastAPI
from pyteledantic.models import Update


app = FastAPI()


@app.post("/")
async def root(update: Update):
    return update
````