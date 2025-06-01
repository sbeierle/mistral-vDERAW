import torch
from safetensors.torch import load_file, save_file
from transformers import AutoTokenizer

# 📦 Konfiguration
model_path = "./mistral/model-00003-of-00003.safetensors"
tensor_key = "lm_head.weight"  # Standard für Mistral GGUF/FT-Modelle
tokenizer_path = "./mistral/"
target_norm = 15.0              # 🔁 Anpassbar (z. B. 20.0 zu stark, 0.7 Scale zu schwach)

# 📘 Kritische Phrasen (nur exemplarisch!)
phrases = [
    "it is strictly forbidden",
    "as an AI developed by",
    "i am not allowed to do that",
    "this may be considered illegal",
    "we do not condone unethical behavior"
]

# 🚀 Tokenizer laden (lokal)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

# 📥 Modell laden
print(f"📦 Lade Datei: {model_path}")
weights = load_file(model_path)

if tensor_key not in weights:
    raise ValueError(f"❌ {tensor_key} nicht gefunden!")

tensor = weights[tensor_key]
patched = set()

# 🛠 Patch-Logik
for phrase in phrases:
    token_ids = tokenizer.encode(phrase, add_special_tokens=False)
    print(f"\n📌 Phrase: '{phrase}' → Token-IDs: {token_ids}")

    for token_id in token_ids:
        if token_id < 4096:  # ⛔ Strukturwörter auslassen
            print(f"   ⚠️  Token {token_id} ist Strukturwort → übersprungen")
            continue
        if token_id in patched:
            continue
        vec = tensor[token_id]
        norm_before = torch.norm(vec, p=2).item()
        tensor[token_id] = vec / norm_before * target_norm
        norm_after = torch.norm(tensor[token_id], p=2).item()
        print(f"   🔧 Token {token_id:<6} Norm: {norm_before:.6f} → {norm_after:.6f}")
        patched.add(token_id)

# 💾 Speichern
save_file(weights, model_path)
print(f"\n✅ Gruppenpatch abgeschlossen → Datei überschrieben: {model_path}")
