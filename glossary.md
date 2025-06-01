# 📚 GLOSSARY – LLM Repatching Terminology

> English – Arabic | إنجليزي – عربي

---

### 🔧 Technical Concepts | مفاهيم تقنية

| Term | Definition (EN) | التعريف (AR) |
|------|------------------|---------------|
| LLM | Large Language Model – a generative text model | نموذج لغوي ضخم لإنشاء النصوص |
| Decoder | Output-generating part of a Transformer | وحدة الإخراج في المعمارية |
| Logits | Raw prediction values before softmax | القيم التنبؤية الخام قبل التوزيع |
| Norm (L2) | Vector magnitude of weight tensors | حجم متجهات الوزن |
| Softfilter | Hidden biasing without hard blocking | فلترة ناعمة دون حظر صريح |
| RLHF | Reinforcement Learning from Human Feedback | التعلم المعزز من ملاحظات البشر |
| FinalNorm | Last normalization layer before LM Head | طبقة التطبيع النهائية قبل إخراج النموذج |
| LM Head | Linear layer mapping hidden states to vocabulary | طبقة التحويل إلى مفردات النموذج |

---

### 🚨 Patch Concepts | مفاهيم التصحيح

| Term | Definition (EN) | التعريف (AR) |
|------|------------------|---------------|
| Token-Level Patch | Direct edit to individual output vectors | تعديل مباشر لمتجهات الكلمات |
| Group Phrase Patch | Norm-based edit using key phrases | تعديل باستخدام عبارات نموذجية |
| Rebalancing | Strategic normalization after deep patching | إعادة توازن بعد تعديلات عميقة |
| Fallback Token | Reserved safe words forced in response | كلمات احتياطية تستخدم للرقابة |
| Prompt Injection | Crafting inputs to bypass filters | إدخال مُعد لتجاوز الحظر |

---

### 🧪 Operational | التشغيل

| Term | Definition (EN) | التعريف (AR) |
|------|------------------|---------------|
| vDERAW | Derestricted, Engineered Raw Model | نموذج معدل محرر بدون قيود |
| Watchdog | Monitoring system for prompt reactions | نظام مراقبة لتحليل المخرجات |
| Critical Prompt | Input designed to trigger censorship | مدخلات حرجة تثير الفلاتر |
| Sleeper Mode | Hidden switch to activate behavior | وضع خفي لتبديل السلوك |

---

📄 This glossary is part of the **Mistral vDERAW Repatch Project**  
📁 Location: `mistral-vDERAW/GLOSSARY.md`
