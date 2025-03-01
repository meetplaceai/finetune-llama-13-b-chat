from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    AutoTokenizer,
)
import torch


device = "auto"
local_model_path = "outputs_squad/merged_model"     # Path to the combined weights
repo_name = "Leul78/llama-13b-chat-priv"            # HuggingFace repo name
hf_token = "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"         # Huggingface token



model = AutoModelForCausalLM.from_pretrained(
    local_model_path, 
    trust_remote_code=True, 
    device_map=device, 
    torch_dtype=torch.float16,
).eval()
tokenizer = AutoTokenizer.from_pretrained(local_model_path)





model.push_to_hub(repo_name, token=hf_token)
tokenizer.push_to_hub(repo_name, token=hf_token)
