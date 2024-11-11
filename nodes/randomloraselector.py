import os
import sys
import folder_paths
import random

import os
import sys
import folder_paths
import random


class RandomLoraSelector:
    @classmethod
    def INPUT_TYPES(s):
        # Get all subfolder paths in the loras directory
        lora_path = folder_paths.get_folder_paths("loras")[0]
        folders = ["root"]  # root represents the main loras folder

        # Add all subfolders and their subfolders recursively
        for root, dirs, files in os.walk(lora_path):
            rel_path = os.path.relpath(root, lora_path)
            if rel_path != ".":  # Skip the root directory itself
                folders.append(rel_path)

        return {"required": {
            "folder_path": (folders,),  # Dropdown for folder selection
            "seed": ("INT", {"default": random.randint(0, 0xffffffffffffffff), "min": 0, "max": 0xffffffffffffffff}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("LORA_NAME",)
    FUNCTION = "select_random_lora"
    CATEGORY = "character utils/lora"

    def get_loras_from_folder(self, folder_path):
        base_path = folder_paths.get_folder_paths("loras")[0]

        if folder_path == "root":
            search_path = base_path
        else:
            search_path = os.path.join(base_path, folder_path)

        lora_files = []

        # Get all .safetensors and .ckpt files in the specified folder
        for file in os.listdir(search_path):
            if file.endswith(('.safetensors', '.ckpt')):
                if folder_path == "root":
                    lora_files.append(file)
                else:
                    # Include the full relative path from loras folder
                    lora_files.append(os.path.join(folder_path, file))

        # Sort the files to ensure consistent ordering regardless of filesystem
        lora_files.sort()

        # Print debug information
        print(f"\nSearching in: {search_path}")
        print(f"Found LoRAs: {lora_files}")

        return lora_files

    def select_random_lora(self, folder_path, seed):
        # Get list of LoRAs from the selected folder
        lora_files = self.get_loras_from_folder(folder_path)

        if not lora_files:
            print(f"No LoRA files found in {folder_path}")
            return ("No LoRAs found",)

        # Create a new Random instance with the seed
        rng = random.Random(seed)

        # Randomly select a LoRA using the seeded RNG
        selected_lora = rng.choice(lora_files)

        # Print the selected LoRA for debugging
        print(f"Selected LoRA (seed {seed}): {selected_lora}")

        return (selected_lora,)
