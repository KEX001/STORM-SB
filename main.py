import sys
import glob
import asyncio
import logging
import importlib.util
from pathlib import Path

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

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

async def main():
    # Load plugins first so they register handlers in client_manager
    files = glob.glob("STORM/modules/*.py")
    for name in files:
        patt = Path(name)
        plugin_name = patt.stem
        load_plugins(plugin_name)

    from STORM.client_manager import start_clients
    clients = await start_clients()
    
    if not clients:
        print("No clients started. Exiting.")
        return
        
    print(f"\nꜱᴛᴏʀᴍ ʙᴏᴛ ɪꜱ ᴅᴇᴘʟᴏʏᴇᴅ ꜱᴜᴄᴄᴇꜱꜰᴜʟʟʏ ᴡɪᴛʜ {len(clients)} ᴄʟɪᴇɴᴛ(ꜱ)")
    
    tasks = [client.run_until_disconnected() for client in clients]
    try:
        await asyncio.gather(*tasks)
    except Exception as e:
        logging.error(f"ꜱᴛᴏʀᴍ ᴀɪ ꜰᴏᴜɴᴅ ᴀɴ ᴇʀʀᴏʀ ⚠️: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
