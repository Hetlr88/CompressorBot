#    This file is part of the Compressor distribution.
#    Copyright (c) Binary Tech
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.



from . import *

try:
    APP_ID = config("APP_ID",default=20077058, cast=int)
    API_HASH = config("API_HASH","349639880eb5b1cb0ff6c2b8a6f16717")
    BOT_TOKEN = config("BOT_TOKEN","7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE")
    OWNER = config("OWNER_ID", default=6169288210, cast=int)
    LOG = config("LOG_CHANNEL", default=-1002205938557, cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
