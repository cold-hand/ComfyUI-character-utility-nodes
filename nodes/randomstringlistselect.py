import random


class RandomStringListSelect:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list": ("LIST", {"default": []}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "random_string_list_select"
    CATEGORY = "character utils/lora"

    def random_string_list_select(self, list):
        # log list value
        if not list:
            return list

        # Select a random word from the list
        trigger = random.choice(list)
        return (trigger,)

LIST_CLASS_MAPPINGS = {
    "RandomStringListSelect+": RandomStringListSelect,
}

LIST_NAME_MAPPINGS = {
    "RandomStringListSelect+": "🔧 Random String List Select",
}