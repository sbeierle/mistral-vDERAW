import torch
from safetensors.torch import load_file, save_file

# ⚙️ Konfiguration
model_path = "./mistral/model-00003-of-00003.safetensors"
tensor_key = "model.final_layer_norm.weight"
target_norm = 0.70  # 🧠 empfohlen: 0.65–0.85

# 📦 Datei laden
print(f"📦 Lade {model_path}")
weights = load_file(model_path)

if tensor_key not in weights:
    raise ValueError(f"❌ {tensor_key} nicht gefunden!")

tensor = weights[tensor_key]
norm_before = torch.norm(tensor, p=2).item()
tensor = tensor / norm_before * target_norm
weights[tensor_key] = tensor
norm_after = torch.norm(tensor, p=2).item()

# 💾 Speichern
save_file(weights, model_path)
print(f"✅ FinalNorm angepasst → Norm: {norm_before:.6f} → {norm_after:.6f}")
print(f"💾 Gespeichert: {model_path}")
