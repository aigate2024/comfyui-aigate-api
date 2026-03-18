class SettingsNode:
    def __init__(self):
        # Initialize any necessary parameters for the node
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "apiKey": ("STRING", {"default": ""}),
            },
        }

    RETURN_TYPES = ("STRUCT",)
    CATEGORY = "云扉AiGate"
    FUNCTION = "process"  # Add FUNCTION attribute pointing to process method

    def process(self, apiKey):
        return [
            {
                "apiKey": apiKey,
            }
        ]
