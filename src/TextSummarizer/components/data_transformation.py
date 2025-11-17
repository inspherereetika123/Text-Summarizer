import os
from TextSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from TextSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        # Encode input dialogue
        input_encodings = self.tokenizer(
            example_batch["dialogue"],
            max_length=1024,
            truncation=True
        )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(
                example_batch["summary"],
                max_length=128,
                truncation=True
            )

        return {
            "input_ids": input_encodings["input_ids"],
            "attention_mask": input_encodings["attention_mask"],
            "labels": target_encodings["input_ids"]
        }

    def convert(self):
        # Load raw dataset
        datasets_samsum = load_from_disk(self.config.data_path)

        # Apply tokenization
        datasets_samsum_pt = datasets_samsum.map(
            self.convert_examples_to_features,
            batched=True
        )

        # Save processed dataset
        output_path = os.path.join(self.config.root_dir, "samsum_dataset")
        datasets_samsum_pt.save_to_disk(output_path)

        return output_path
