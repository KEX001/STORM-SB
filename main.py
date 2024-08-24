import sys
import glob
import asyncio
import logging
import importlib.util
import traceback
import urllib3
from pathlib import Path
from config import KEX1, KEX2, KEX3, KEX4, KEX5, KEX6, KEX7, KEX8, KEX9, KEX10

# Set up logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Asynchronous function to load plugins
async def load_plugins_async(plugin_name):
    path = Path(f"STORM/modules/{plugin_name}.py")
    try:
        spec = importlib.util.spec_from_file_location(f"STORM.modules.{plugin_name}", path)
        load = importlib.util.module_from_spec(spec)
        load.logger = logging.getLogger(plugin_name)
        await asyncio.to_thread(spec.loader.exec_module, load)  # Load the module in a thread pool
        sys.modules[f"STORM.modules.{plugin_name}"] = load
        print(f"ꜱᴛᴏʀᴍ ʜᴀꜱ ɪᴍᴘᴏʀᴛᴇᴅ {plugin_name}")
    except Exception as e:
        logging.error(f"ꜰᴀɪʟᴇᴅ ᴛᴏ ʟᴏᴀᴅ ᴘʟᴜɢɪɴ {plugin_name}: {e}")
        logging.error(traceback.format_exc())

# Function to load all plugins concurrently
async def load_all_plugins():
    files = [f for f in glob.glob("STORM/modules/*.py") if not f.endswith('__init__.py')]  # Filter out __init__.py
    tasks = []
    for name in files:
        patt = Path(name)
        plugin_name = patt.stem
        tasks.append(load_plugins_async(plugin_name))
    await asyncio.gather(*tasks)  # Load all plugins concurrently

# Main async function to run the bot
async def main():
    await load_all_plugins()  # Load all plugins asynchronously
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
        await asyncio.gather(*tasks)  # Run all tasks concurrently
    except Exception as e:
        logging.error(f"ꜱᴛᴏʀᴍ ᴀɪ ꜰᴏᴜɴᴅ ᴀɴ ᴇʀʀᴏʀ ⚠️: {e}")

# Entry point for the program
if __name__ == "__main__":
    # Use asyncio.run() for better loop management
    asyncio.run(main())
