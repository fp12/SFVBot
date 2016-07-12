import aiohttp
import asyncio
import os

CHALLONGE_API_URL = "api.challonge.com/v1"
url = "https://%s/tournaments.xml" % (CHALLONGE_API_URL)

params = {'tournament[name]': 'testmyherokusetup', 'tournament[url]': 'test_1', 'tournament[tournament_type]': 'swiss'}
"""
with aiohttp.ClientSession() as session:
    async with session.post(url, params=params, auth=aiohttp.BasicAuth('fp12', os.getenv('challonge_apikey', ''))) as resp:
        print(resp.status)
        print(await resp.text())

async with EXPR as VAR:
    BLOCK
"""
with aiohttp.ClientSession() as session:
    mgr = session.post(url, params=params, auth=aiohttp.BasicAuth('fp12', os.getenv('challonge_apikey', '')))
    aexit = type(mgr).__aexit__
    aenter = type(mgr).__aenter__(mgr)
    exc = True

    resp = aenter
    aexit(mgr, None, None, None)
