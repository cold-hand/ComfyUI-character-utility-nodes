from .nodes.randomstringlistselect import RandomStringListSelect
from .nodes.randomloraselector import RandomLoraSelector

NODE_CLASS_MAPPINGS = {
    "RandomStringListSelect": RandomStringListSelect,
    "RandomLoraSelector": RandomLoraSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RandomStringListSelect": "🧝 Random String List Select",
    "RandomLoraSelector": "🧝 Random Lora Selector",
}

print("\033[34mCharacter Util Nodes: \033[92mLoaded\033[0m")
