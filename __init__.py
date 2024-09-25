class BatchSequenceString:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "batch_size": ("INT", {"default": 3}),  # Input batch_size parameter
            },
        }

    FUNCTION = "generate_sequence"
    RETURN_TYPES = ("STRING",)
    CATEGORY = "Sequence Generator 💡"

    def generate_sequence(self, batch_size: int):
        # Initialize the sequence with the first number
        sequence = [0]
        # Continue adding to the sequence according to the logic
        while sequence[-1] + batch_size + 1 < batch_size * batch_size:
            sequence.append(sequence[-1] + batch_size + 1)

        # Convert the sequence to a string for output
        sequence_str = ', '.join(map(str, sequence))

        return (sequence_str,)

# Node class mappings
NODE_CLASS_MAPPINGS = {
    "BatchSequenceString": BatchSequenceString
}

# Node display name mappings
NODE_DISPLAY_NAME_MAPPINGS = {
    "BatchSequenceString": "Batch Sequence String"
}
