from types import SimpleNamespace
from src.utils.keyboards import create_keyboard

keys=SimpleNamespace(
    connect=':people_hugging:Random Connect',
    Setting=':gear:bot setting',
    empty='nothing to do'
)

keyboards=SimpleNamespace(
    main=create_keyboard(keys.connect, keys.Setting, keys.empty)
)