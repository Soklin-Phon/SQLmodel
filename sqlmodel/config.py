import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="sqlmodel",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="sqlmodel_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from sqlmodel.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export sqlmodel_KEY=value
export sqlmodel_KEY="@int 42"
export sqlmodel_KEY="@jinja {{ this.db.uri }}"
export sqlmodel_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
sqlmodel_ENV=production sqlmodel run
```

Read more on https://dynaconf.com
"""
