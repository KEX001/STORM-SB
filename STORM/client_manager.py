import logging
from telethon import TelegramClient, events
from os import getenv
import config

logger = logging.getLogger("STORM")

CLIENTS = []
_handlers = []

def on_cmd(command_name, **kwargs):
    """
    Decorator to register a command handler for all clients with the configured prefix.
    """
    def decorator(func):
        from config import CMD_HNDLR
        pattern = r"\%s%s(?: |$)(.*)" % (CMD_HNDLR, command_name)
        kwargs.setdefault('incoming', True)
        kwargs['pattern'] = pattern
        _handlers.append((func, events.NewMessage, kwargs))
        return func
    return decorator

def on_message(**kwargs):
    """
    Decorator to register a raw message handler for all clients.
    """
    def decorator(func):
        _handlers.append((func, events.NewMessage, kwargs))
        return func
    return decorator

@on_message(incoming=True)
async def log_commands(event):
    if event.text and event.text.startswith(config.CMD_HNDLR):
        if event.sender_id in config.SUDO_USERS:
            logger.warning(f"Received command: '{event.text}' from sender {event.sender_id} (is_sudo: True)")

def on_callback(**kwargs):
    """
    Decorator to register a callback query handler for all clients.
    """
    def decorator(func):
        _handlers.append((func, events.CallbackQuery, kwargs))
        return func
    return decorator

async def start_clients():
    global CLIENTS
    tokens = []
    # Load BOT_TOKEN first
    t1 = getenv("BOT_TOKEN")
    if t1:
        tokens.append(t1)
    
    # Load BOT_TOKEN2 to BOT_TOKEN50
    for idx in range(2, 51):
        tok = getenv(f"BOT_TOKEN{idx}")
        if tok:
            tokens.append(tok)
    
    # Filter valid non-empty tokens
    valid_tokens = [t.strip() for t in tokens if t and t.strip()]
    if not valid_tokens:
        logger.error("No valid bot tokens provided in environment variables!")
        return []
    
    for i, token in enumerate(valid_tokens, start=1):
        session_name = f"storm_session_{i}"
        client = TelegramClient(session_name, config.API_ID, config.API_HASH)
        try:
            await client.start(bot_token=token)
            me = await client.get_me()
            client.me_id = me.id
            logger.warning(f"Successfully started client {i}: @{me.username} ({me.first_name})")
            CLIENTS.append(client)
        except Exception as e:
            logger.error(f"Failed to start client {i}: {e}")
            
    # Register all handlers to all active clients
    for client in CLIENTS:
        for func, event_class, kwargs in _handlers:
            client.add_event_handler(func, event_class(**kwargs))
            
    logger.warning(f"Registered {len(_handlers)} handlers to {len(CLIENTS)} clients.")
    return CLIENTS
