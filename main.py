#!/usr/bin/env python3
import sys
import glob
import asyncio
import logging
import importlib.util
from pathlib import Path
from typing import List, Optional, Dict, Any
from config import (
    KEX1, KEX2, KEX3, KEX4, KEX5, 
    KEX6, KEX7, KEX8, KEX9, KEX10
)

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class PluginManager:
    @staticmethod
    def load_plugin(plugin_path: Path) -> Optional[Any]:
        plugin_name = plugin_path.stem
        try:
            spec = importlib.util.spec_from_file_location(
                f"STORM.modules.{plugin_name}", 
                plugin_path
            )
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                module.logger = logging.getLogger(plugin_name)
                spec.loader.exec_module(module)
                sys.modules[f"STORM.modules.{plugin_name}"] = module
                logger.info(f"Successfully loaded plugin: {plugin_name}")
                return module
        except Exception as e:
            logger.error(f"Failed to load plugin {plugin_name}: {str(e)}")
        return None

    @classmethod
    def load_all_plugins(cls, plugins_dir: str = "STORM/modules/") -> None:
        plugin_files = glob.glob(f"{plugins_dir}*.py")
        for plugin_file in map(Path, plugin_files):
            cls.load_plugin(plugin_file)

class BotManager:
    COMPULSORY_BOTS = [KEX1, KEX2, KEX3, KEX4, KEX5]
    OPTIONAL_BOTS = [KEX6, KEX7, KEX8, KEX9, KEX10]

    @classmethod
    async def run_bots(cls) -> None:
        tasks: List[asyncio.Task] = []
        
        for i, bot in enumerate(cls.COMPULSORY_BOTS, 1):
            tasks.append(asyncio.create_task(
                cls._run_bot(bot, f"Compulsory Bot {i}"),
                name=f"compulsory_bot_{i}"
            ))
        
        for i, bot in enumerate(cls.OPTIONAL_BOTS, 1):
            if bot is not None:
                tasks.append(asyncio.create_task(
                    cls._run_bot(bot, f"Optional Bot {i}"),
                    name=f"optional_bot_{i}"
                ))
            else:
                logger.info(f"Optional Bot {i} is not configured - skipping")

        try:
            await asyncio.gather(*tasks)
        except Exception as e:
            logger.critical(f"Critical error in bot operation: {str(e)}")
            raise

    @staticmethod
    async def _run_bot(bot: Any, bot_name: str) -> None:
        try:
            logger.info(f"Starting {bot_name}")
            await bot.run_until_disconnected()
        except Exception as e:
            logger.error(f"{bot_name} encountered an error: {str(e)}")
            raise

async def main() -> None:
    logger.info("Initializing Storm Bot System")
    
    PluginManager.load_all_plugins()
    
    await BotManager.run_bots()
    
    logger.info("Storm Bot system shutdown complete")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Received shutdown signal - terminating gracefully")
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}")
        sys.exit(1)
