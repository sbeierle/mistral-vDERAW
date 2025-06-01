# 🧠 Mistral vDERAW (Decoder Repatching & RLHF Dissection)

**Version**: v2.0  
**Model Target**: Mistral 7B Instruct  
**Type**: Red Team Research | Controlled Derestriction | Token-Level RLHF Analysis

---

## 🇬🇧 Overview

This repository documents the controlled repatching and alignment inspection of the Mistral 7B Instruct v2.0 model.  
Our goal: **Reveal & rewire RLHF bias layers** while preserving semantic control.

### 🧬 Core Areas
- L2-norm token manipulation (`lm_head.weight`)
- `final_norm`, `down_proj`, and `out_proj` inspection
- ASCII architecture illustrations
- Red-team inspired phrasing analysis
- Group patching of hard RLHF trigger tokens
- Ethical safeguards + non-public script policy

### 🛠 Status
> ✅ Fully patched `lm_head`  
> ✅ Token-visualization & norm scaling  
> 🔒 Full tools only for verified institutions

---

## 🇸🇦 نظرة عامة

يوثق هذا المستودع عملية إصلاح ومحاكاة نموذج Mistral 7B Instruct بإصدار v2.0  
الهدف: **كشف وتفكيك طبقات التحيّز الناتجة عن RLHF** مع الحفاظ على التحكم الدلالي.

### 🧬 الجوانب الأساسية
- تعديل معيار L2 للتوكنات (`lm_head.weight`)
- تحليل الطبقات: `final_norm`, `down_proj`, `out_proj`
- رسوم ASCII لتوضيح البنية
- تحليل العبارات الحساسة من منظور فريق Red Team
- تعديل جماعي للتوكنات المحفزة للفلترة
- ⚠️ الحماية الأخلاقية – السكربتات الكاملة غير منشورة

---

## 🔐 Access to scripts?


# 🧠 Mistral-7B Instruct v2.0 – إطار عمل إعادة تصحيح التحيز المتحكم فيه

> ⚠️ محلي بحت، أخلاقي بحت. لا يوجد إساءة - فقط البحث ومحاكاة الفريق الأحمر.

---

## 📄 نظرة عامة تنفيذية

يوثق هذا المستودع إطار عمل متعدد المراحل لتحليل التحيز المتحكم فيه وإعادة معايرة فك التشفير للنموذج Mistral-7B-Instruct-v0.2.

هدف:
إزالة التصعيد الدقيق لأنظمة التصفية الناعمة القاسية للغاية (RLHF)، دون فقدان البنية أو التشويه الدلالي.
**ليس كسر حماية – بل تقنية إعادة تصحيح محكومة.**

---

## 🔍 الوحدة النمطية

| الوحدة | الوصف |
|-------|----------------|
| `🧩 01-03` | هيكل النموذج وهيكل فك التشفير ومنطق ناقل RLHF |
| 🧩 04-10 | تحليل القواعد، واكتشاف المرشح الناعم ورسم الخرائط اللوغاريتمية
| 🧩 11-18 | التصحيح على مستوى الرمز، وتوسيع نطاق عبارة المجموعة، وتجنب الحلول البديلة |
| 19-21 | توافق LoRA، إعادة توازن القاعدة، التخفيف من FinalNorm |
| `📦 أدوات/` | نصوص للتحليل والتعديل (`lm_head`، `final_norm`، إلخ.) |

---

## 🛡️ الأمن والأخلاق

- **لا يوجد نشر للكود الوظيفي لإعادة تصحيح النموذج**
- أدوات **مثالية** فقط - غير قابلة للتطبيق بشكل مباشر دون معرفة متعمقة
- تم اختبار البرامج النصية محليًا (بيئة ROCm / Mistral / AMD / HIP)
- الوصول الكامل فقط مع موافقة أخلاقية مكتوبة (على سبيل المثال الجامعة، مركز الأبحاث)

---

## 🔧 المتطلبات الفنية

- `المحولات`
- `موترات الأمان`
- `torch` (تم اختباره متوافقًا مع ROCm)
- `بايثون >= 3.10`
- شظايا `.safetensors` المخزنة محليًا (ليس عبر محور HF)

---

## 🔒 الوصول والترخيص

لا يحتوي هذا المستودع على **بيانات كاملة أو برامج تصحيح**، ولكنه يهدف إلى **إظهار إطار عمل الهندسة العكسية** لاستراتيجية البحث/الدفاع.
→ للحصول على خط أنابيب LoRA/Weights الكامل: اطلب عبر الاتصال (يلزم وجود بريد إلكتروني مؤسسي)

---

📎 **مرجع الكتاب الأبيض:** _الكتاب الأبيض لإعادة تصحيح Mistral_ (مرفق محليًا، غير عام)
📸 **ASCII/Visuals:** راجع `screenshots/` وعلامات العرض التوضيحي في الأدوات
🧾 **المصطلحات:** مكتملة في `docs/glossar.md`

---

## 📬 موافقة الاتصال والأخلاقيات

مفتوح للتعاون مع:
- 🇩🇪 معاهد الأبحاث (أمن تكنولوجيا المعلومات، تحيز ماجستير القانون، التدقيق)
- 🏛️ الوكالات الحكومية المتفقة على الأخلاقيات
- 🧑‍💻 مدققو الفريق الأحمر الموثوق بهم

🖋️ الطلب فقط مع التوقيع والإثبات: `kihorscht@gmail.com`

> Scripts are **NOT public**.  
> Contact via GitHub or institutional email for verified access.

---
