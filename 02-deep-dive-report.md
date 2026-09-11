# 📄 02 — Deep-Dive Report: Xanh SM – Sự cố hết pin (Battery-Drain Emergency Dispatch)

> * **Autor draftu:** Nguyen Van An (branch `An`) — draft do wspólnej dyskusji zespołu i ewentualnego wgrania do `main` przez Trưởnga
> * **Treść zgodnie z:** `01-worksheet.md` → Phase 3 (DEEP-DIVE) + Phase 5 (EVALUATE)
> * **Karta wybrana:** Card #1 (Xanh SM — awaria baterii taksówki EV na trasie)

---

## 🏗️ Phase 3 — DEEP-DIVE

### 3.1. Current-State Workflow Mapping

Quy trình xử sự cố hết pin thực địا hiện tại (obsługa awarii baterii na trasie) w Trung tâm Điều vận Xanh SM:

```text
B1: Odebranie zgłoszenia od tài xë (tel/App)      Ai: Dispatcher   ⏱ 2 min
        │
        ▼
B2: Pozycja GPS auta (manual lookup)              Ai: Dispatcher   ⏱ 2 min
        │
        ▼
B3: Szukanie wolnej stacji sạc VinFast 🔴         Ai: Dispatcher   ⏱ 5 min
        │
        ▼
B4: Pisanie instrukcji SMS/App dla kierowcy 🔴     Ai: Dispatcher   ⏱ 5 min
        │
        ▼
B5: Telefon po pomoc drogową, gdy pin < 5%         Ai: Dispatcher   ⏱ 1 min

🔄 Handoff: B1→B2 (telefon/systemy)  •  B4→B5 (system/telefon)
🔴 = Bottleneck: B3 + B4 = 10 min ręcznej pracy ze 15 min całkowitych
⏱ Tổng czas obsługi ręcznej: 15 min/zgłoszenie (~80 zgłoszeń/dzień, Hà Nội)
```

### 3.2. Problem Statement (6-field) — standard Vin Smart Future

| # | Pole | Treść |
|---|------|-------|
| **1. Actor / Operator** | Điều phối viń (Dispatcher) w Trung tâm Điều vân Xanh SM oraz Tài xë (kierowca EV) na trasie. |
| **2. Current Workflow** | Gdy kierowca zgłasza rozładowaną baterię, dyspozytor: sprawdza pozycję GPS, otwiera dashboard stacji VinFast, ręcznie znajduje wolną stację pasującą do modelu (VF5/VFe34/VF8), pisze instrukcję SMS/App i — przy pin < 5% — dzwoni po pomoc drogową. 5 kroków, w 100% ręcznie, średnio 15 min/zgłoszenie. |
| **3. Bottleneck** | Krok B3+B4 (ok. 10 min): ręczne przeszukiwanie wolnych stacji + pisanie szczegółowej instrukcji w przyjaznym języku. Błąd = polecenie stacji niekompatybilnej lub zbyt odległej → ryzyko zatrzymania auta na trasie. |
| **4. Business Impact** | Ok. 80 zgłoszeń/dzień w Hà Nội → ok. 20 godzin pracy zespołu dziennie na ręczną obsługę; wydłużony czas oczekiwania kierowcy → utrata przychodów (~15% kursów) i stres kierowców. |
| **5. Success Metric** | 1) Czas obsługi zgłoszenia: 15 min → **poniżej 3 min** (Efficiency). 2) Poprawność wskazanej stacji (właściwe miejsce + właściwy typ ładowania dla modelu): **98%** (Quality). |
| **6. Operational Boundary** | AI ma prawo: pobierać pozycję auta (API GPS), sprawdzać wolne stacje VinFast (API), generować draft instrukcji. **ZABRONIONE:** automatyczne wysyłanie wiadomości bez pisemnej zgody dyspozytora (obowiązkowy HITL); proponowanie stacji niekompatybilnej z gniazdem ładowania; proponowanie stacji > 5 km przy pin < 5% (wymagany `dispatch_mobile_charger`). |

### 3.3. Future-State Flow & AI Fit

* **AI-Fit Matrix:** [ ] Rule / State-Machine · **[x] LLM Feature** · [ ] Agentic Loop
  *(LLM Feature, bo proces ma stałą, przewidywalną strukturę, a ryzyko błędu przy krytycznym pinie jest wysokie — pełny agent autonomiczny byłby nieuzasadniony.)*

```text
B1: Odebranie zgłoszenia      Ai: Dispatcher        ⏱ 1 min
        │
        ▼
B2: 🔵 AI auto-pobiera pozycję GPS + wolne stacje  Ai: LLM + API   ⏱ <1 min
        │
        ▼
B3: 🔵 AI generuje draft SMS z [DRAFT_ONLY]        Ai: Gemini 2.5  ⏱ <1 min
        │
        ▼
B4: 🟢 Dyspozytor zatwierdza draft i klika WYŚLIJ  Ai: HITL        ⏱ 1 min
        │
        ▼
    Wysyłka do tài xë (SMS/App)

↩️ Fallback: jeśli AI zwróci błąd/niepewność → dyspozytor obsługuje ręcznie (tryb „as-is"),
   bez utraty bezpieczeństwa (manual_review, bez automatycznej wysyłki).
```

* 🔵 **AI Step:** pobranie danych (pozycja + wolne stacje) oraz wygenerowanie draftu wiadomości w formacie JSON.
* 🟢 **Human Step (HITL):** dyspozytor zatwierdza draft i dopiero on wysyła wiadomość do kierowcy.
* ↩️ **Fallback:** przy błędzie AI (timeout, zła stacja, niepewność) asystent zwraca `manual_review`, a dyspozytor obsługuje zgłoszenie ręcznie — bez utraty bezpieczeństwa.

---

## 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist

- [x] **1. Danne testowe/logi:** Centrum Xanh SM ma dzienniki zgłoszeń (call logs, ślady GPS, historię stacji) — dostępne do pilotażu.
- [x] **2. Ryzyko błędu AI w kontroli:** błąd AI jest ograniczony przez obowiązkowy HITL (żadnej automatycznej wysyłki) i fallback `manual_review` — ryzyko w akceptowalnych granicach.
- [x] **3. Gotowość stakeholderów:** dyspozytorzy widzą realną ulgę (20h/dzień) i są gotowi na zmianę procesu w pilocie.

### Decyzja Zarządu Vin Smart Future

**[x] GO (Bắt đầu budować Prototype)** — start pilotażu z wąskim zakresem (Hà Nội, flota VF8, godziny szczytu).

### Justification (dlaczego GO?)

1. **Problem konkretny i mierzalny:** 80 zgłoszeń/dzień, 20h ręcznej pracy dziennie, 15 min → < 3 min, poprawność 98% — metryki jednoznacznie weryfikowalne.
2. **Technologia prosta i bezpieczna:** LLM Feature (nie pełny agent) + obowiązkowy HITL + fallback `manual_review` — niski koszt wdrożenia, ograniczone ryzyko operacyjne.
3. **Granice bezpieczeństwa przetestowane promptowo:** ataki adversarial (krytyczny pin + daleka stacja, obejście [DRAFT_ONLY], obejście HITL przez „autorytet") zostały odparte przez SYSTEM_PROMPT — prototyp potwierdził wytrzymałość granic (patrz `starter-code/prompt_prototype.py` i `03-ai-log.md`).
4. **NOT YET / NO-GO odrzucone:** dane testowe już istnieją (logi) — brak powodu do czekania; rule-based samo nie wystarczy, bo treść wiadomości wymaga naturalnego języka i personalizacji, co potwierdza potrzebę LLM (a nie NO-GO).