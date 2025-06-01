# 🧷 Patches & Strategien – Übersicht

> Dieses Dokument gibt einen Überblick über die wichtigsten Patching-Verfahren, die im Mistral-Repatching verwendet wurden. Ziel: Bias-Entschärfung, Wiederherstellung neutraler Decoderverteilung und kontrollierte Antwortgenerierung.

---

## 🔧 1. LM Head Token Patch

**Ziel:** Einzelne Tokens direkt in `lm_head.weight` entschärfen (Norm-Modifikation)

```python
vec = tensor[token_id]
tensor[token_id] = vec / norm(vec) * target_norm
🧷 التصحيحات والاستراتيجيات - نظرة عامة

توفر هذه الوثيقة نظرة عامة على إجراءات التصحيح الرئيسية المستخدمة في إعادة تصحيح Mistral. الهدف: التخفيف من التحيز، واستعادة توزيع فك التشفير المحايد وتوليد الاستجابة المتحكم فيها.

---

## 🔧 1. LM Head Token Patch

**الهدف:** إبطال مفعول الرموز الفردية مباشرةً في `lm_head.weight` (تعديل القاعدة)

بايثون
vec = tensor[token_id]
tensor[token_id] = vec / norm(vec) * target_norm
