

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

**The Userbot should work by setting only the first two variables**

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  # 6 is the length of api id
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  # Use Your Own Api Hash
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration** Simply just leave the Config as it is.

**Local Configuration** Fortunately there are no Mandatory vars for the UniBorg
Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
  - `APP_ID`: You can get this value from https://my.telegram.org //Not getting
    your telegram channel please help me
  - `API_HASH`: You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

## IndianUserbot Session
[![Andencento Session](https://repl.it/badge/github/Andencento/Andencento)](https://replit.com/@TeamIndian/StringSession?v=1)
