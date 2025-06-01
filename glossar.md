# 📘 Glossar – Mistral Repatch Projekt

> Dieses Glossar enthält die wichtigsten Begriffe, Konzepte und Abkürzungen, die im Rahmen des Repatch-Projekts verwendet werden.

---

### 🧠 Modellstruktur & Architektur

| Begriff               | Beschreibung                                                                 |
|-----------------------|-------------------------------------------------------------------------------|
| **Decoder**           | Teil des LLMs, der Text autoregressiv generiert.                             |
| **LayerNorm**         | Normalisierungsschicht zur Stabilisierung des Trainings.                     |
| **LM Head**           | Linear-Schicht zur Projektion auf den Token-Vokabelraum.                     |
| **OutProj**           | Projektion der Attention-Ausgabe (oft Bias-Entry-Point für RLHF).            |
| **MLP DownProj**      | Teil des Feedforward-Netzes, steuert Verstärkung/Schwächung des Decoders.    |

---

### 🔍 Analyse & Patching

| Begriff               | Beschreibung                                                                 |
|-----------------------|-------------------------------------------------------------------------------|
| **L2-Norm**           | Euklidische Norm eines Vektors: misst die Länge (Magnitude) eines Tokens.    |
| **Logits**            | Rohwerte der Ausgabe vor dem Softmax – repräsentieren Token-Wahrscheinlichkeiten. |
| **Softfilter**        | Bias-Mechanismus durch Normverschiebung ohne hartes Verbot (keine Token-Maskierung). |
| **Critical Prompt**   | Prompt, der sicherheitsrelevantes oder zensiertes Verhalten auslöst.         |
| **Fallback-Tokens**   | Tokens, die als alternative Antworten einspringen, wenn andere unterdrückt werden. |

---

### ⚙️ Tools & Verfahren

| Begriff               | Beschreibung                                                                 |
|-----------------------|-------------------------------------------------------------------------------|
| **Token Patch**       | Direkte Veränderung eines `lm_head`-Vektors (z. B. Skalierung der Norm).     |
| **Group Patching**    | Sammelbasierte Entschärfung ganzer Phrasen oder semantisch verwandter Tokens.|
| **Rebalancing**       | Rückanpassung von überschärften oder apathischen Tokens.                     |
| **LoRA (Low Rank Adap.)** | Verfahren zur gewichtsschonenden Feinjustierung via zusätzlicher Layer.     |
| **FinalNorm Patch**   | Eingriff in `final_layer_norm` zur generellen Entzerrung von Antwort-Bias.   |

---

### 🧪 Status-Flags & Versionen

| Flag / Kürzel         | Bedeutung                                                                    |
|------------------------|------------------------------------------------------------------------------|
| **vDERAW**             | interne Modellvariante mit vollständiger Softfilter-Entfernung               |
| **SCALE-Modus**        | gezielte Softnorm-Abschwächung statt radikaler Entfernung                    |
| **EXEC-Zone**          | Prompt-Testmodus mit kritischer Ausführungskontrolle                        |
| **Hydra-LoRA**         | geplantes Subsystem für rollenbasiertes Red-Team-Tuning                     |
| **Phase 4**            | Status der vollen Group-Patch-Korrektur & Normrebalancierung                |

---

*Letzte Aktualisierung: `{{DATUM_AUTO}}` – generiert durch das Repatch-Dokumentationssystem.*


# 📘 المصطلحات - مشروع إعادة رقعة ميسترال

يحتوي هذا القاموس على أهم المصطلحات والمفاهيم والاختصارات المستخدمة في مشروع Repatch.

---

### 🧠 هيكل النموذج والهندسة المعمارية

| مصطلح | الوصف |
|-----------------------|------------------------------------------------------------------------------------------------|
| **فك التشفير** | جزء من برنامج LLM الذي يقوم بإنشاء نص انحداري تلقائي. |
| **لايرنورم** | طبقة التطبيع لتثبيت التدريب. |
| **رئيس LM** | طبقة خطية للإسقاط على مساحة المفردات الرمزية. |
| **OutProj** | إسقاط ناتج الاهتمام (غالبًا ما يكون نقطة دخول متحيزة لـ RLHF). |
| **MLP DownProj** | جزء من شبكة التغذية الأمامية، يتحكم في تضخيم/تخفيف جهاز فك التشفير. |

---

### 🔍 التحليل والتصحيح

| مصطلح | الوصف |
|-----------------------|------------------------------------------------------------------------------------------------|
| **معيار L2** | القاعدة الإقليدية للمتجه: تقيس طول (مقدار) الرمز. |
| **لوجيتس** | القيم الخام للإخراج قبل softmax – تمثل احتمالات الرمز. |
| **فلتر ناعم** | آلية التحيز من خلال تحول القاعدة دون حظر صارم (لا يوجد قناع رمزي). |
| **مطالبة حاسمة** | مطالبة تؤدي إلى سلوك متعلق بالأمان أو خاضع للرقابة. |
| **الرموز الاحتياطية** | الرموز التي تتدخل كاستجابات بديلة عندما يتم قمع الآخرين. |

---

### ⚙️ الأدوات والإجراءات

| مصطلح | الوصف |
|-----------------------|------------------------------------------------------------------------------------------------|
| **تصحيح الرمز المميز** | التعديل المباشر لمتجه `lm_head` (على سبيل المثال، تغيير مقياس القاعدة). |
| **تصحيح المجموعة** | إزالة الغموض عن طريق التجميع للعبارات بأكملها أو الرموز ذات الصلة دلاليًا.
| **إعادة التوازن** | إعادة تكييف الرموز المفرطة في الشحذ أو اللامبالية. |
| **LoRA (التكيف مع الرتبة المنخفضة)** | عملية تعديل الوزن بشكل دقيق من خلال طبقات إضافية. |
| **تصحيح FinalNorm** | التدخل في `final_layer_norm` لتحقيق معادلة عامة لتحيز الاستجابة. |

---

### 🧪 أعلام الحالة والإصدارات

| العلم / الاختصار | المعنى |
|------------------------|----------------------------------------------------------------------------------|
| **في ديراو** | متغير النموذج الداخلي مع إزالة الفلتر الناعم بالكامل |
| **وضع المقياس** | استهداف إضعاف المعايير الناعمة بدلاً من إزالتها جذريًا |
| **منطقة التنفيذيين** | وضع الاختبار السريع مع التحكم في التنفيذ الحرج |
| **هيدرا لورا** | نظام فرعي مخطط لضبط الفريق الأحمر بناءً على الأدوار |
| **المرحلة الرابعة** | حالة تصحيح المجموعة الكاملة وإعادة توازن المعايير |

---

*آخر تحديث: `{{DATE_AUTO}}` - تم إنشاؤه بواسطة نظام توثيق إعادة التصحيح.*
