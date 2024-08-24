import sys
import glob
import asyncio
import logging
import importlib.util
import urllib3
from pathlib import Path
from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def load_plugins(plugin_name):
    path = Path(f"STORM/modules/{plugin_name}.py")
    try:
        spec = importlib.util.spec_from_file_location(f"STORM.modules.{plugin_name}", path)
        load = importlib.util.module_from_spec(spec)
        load.logger = logging.getLogger(plugin_name)
        spec.loader.exec_module(load)
        sys.modules[f"STORM.modules.{plugin_name}"] = load
        print(f"ꜱᴛᴏʀᴍ ʜᴀꜱ ɪᴍᴘᴏʀᴛᴇᴅ {plugin_name}")
    except Exception as e:
        print(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ʟᴏᴀᴅ ᴘʟᴜɢɪɴ {plugin_name}: {e}")

files = glob.glob("STORM/modules/*.py")
for name in files:
    patt = Path(name)
    plugin_name = patt.stem
    load_plugins(plugin_name)

print("\nꜱᴛᴏʀᴍ ʙᴏᴛ ɪꜱ ᴅᴇᴘʟᴏʏᴇᴅ ꜱᴜᴄᴄᴇꜱꜰᴜʟʟʏ")

async def main():
    tasks = [
        KEX1.run_until_disconnected(),
        KEX2.run_until_disconnected(),
        KEX3.run_until_disconnected(),
        KEX4.run_until_disconnected(),
        KEX5.run_until_disconnected(),
        KEX6.run_until_disconnected(),
        KEX7.run_until_disconnected(),
        KEX8.run_until_disconnected(),
        KEX9.run_until_disconnected(),
        KEX10.run_until_disconnected()
    ]
    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        logging.error(f"ꜱᴛᴏʀᴍ ᴀɪ ꜰᴏᴜɴᴅ ᴀɴ ᴇʀʀᴏʀ ⚠️: {e}")

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
