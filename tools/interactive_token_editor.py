import torch
from safetensors.torch import load_file
from transformers import AutoTokenizer

# 📦 Konfiguration
model_path = "./mistral/model-00003-of-00003.safetensors"
tensor_key = "lm_head.weight"
tokenizer_path = "./mistral/"

# 🔍 Eingabe
prompt = input("🧠 Prompt eingeben ('exit' zum Beenden):\n> ").strip()
if prompt.lower() == "exit":
    exit()

# 🔤 Tokenizer & Modell laden
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
weights = load_file(model_path)
tensor = weights[tensor_key]

# 🔢 Tokenisierung
input_ids = tokenizer.encode(prompt, add_special_tokens=False)
print(f"\n🧾 Tokens mit lm_head L2-Norm:")

# 🔍 Analyse der Tokenvektoren
for token_id in input_ids:
    token_str = tokenizer.decode([token_id]).replace("\n", "\\n")
    vec = tensor[token_id]
    norm = torch.norm(vec, p=2).item()
    print(f"Token-ID {token_id:>6} ('{token_str:<14}') → Norm: {norm:.6f}")
