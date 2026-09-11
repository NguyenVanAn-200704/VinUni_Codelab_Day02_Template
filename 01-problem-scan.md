# 📄 01 — Problem Scan & Quick Cards (załącznik indywidualny)

> * **Học viên:** Nguyen Van An (branch `An`)
> * **Lab:** Lab 02 — AI Product Scoping (Vin Smart Future / Vingroup)
> * **Źródła:** `01-worksheet.md` → Phase 1 (SCAN) + Phase 2 (QUICK-ASSESS)
> * **Problem wybrany do deep-dive (Card #1):** Xanh SM — sự cố hết pin thực địa (awaria baterii taksówki EV na trasie)

---

# 🔍 Phase 1 — SCAN: Tìm kiếm bài toán (Cá nhân)

## 4 Lenses użyte do skanowania spółek Vingroup

| # | Lens | Opis |
|---|------|------|
| 1 | **Lặp lại (Repetitive)** | Zadania powtarzane wiele razy dziennie (np. ręczne przypisywanie kursów, reconciliacja danych). |
| 2 | **Tốn thời gian (Time-consuming)** | Ręczne czynności pochłaniające godziny pracy personelu (szukanie, pisanie, dzwonienie). |
| 3 | **AI-upgrade (AI może lepiej)** | Obsługa klienta wolna lub szablonowa, którą LLM może przyspieszyć i spersonalizować. |
| 4 | **Pain od ludzi (Stakeholder Pain)** | Bóle faktycznie zgłaszane przez klientów i pracowników w codziennej pracy. |

## 📝 Moja lista problemów (6)

| # | Subsidiary | Lens | Opis problema |
|---|------------|------|---------------|
| 1 | **Xanh SM** | Tốn thời gian | Ręczna obsługa awarii „rozładowana bateria" na trasie (15–20 min/zgłoszenie): szukanie wolnej stacji VinFast, pisanie instrukcji, kontakt z pomocą drogową. |
| 2 | **Xanh SM** | Lặp lại | Ręczne ponowne przypisywanie kursu, gdy pasażer zmienia cel podróży w trakcie jazdy (re-dispatch). |
| 3 | **VinFast** | Lặp lại | Tygodniowa reconciliacja faktur ładowania z danymi tysięcy stacji partnerskich (MCOS billing match). |
| 4 | **Vinhomes** | AI-upgrade | Klasyfikacja i routowanie skarg mieszkańców z aplikacji Vinhomes Resident (szablonowe odpowiedzi, ~12h reakcji). |
| 5 | **Vinmec** | Pain od ludzi | Lekarze tracą 20–30 min/pacjenta na pisanie streszczeń wypisu (Discharge Summary) zamiast poświęcać czas pacjentom. |
| 6 | **Vinpearl** | Tốn thời gian | Ręczne sprawdzanie grupowych rezerwacji e-mailowych (Group Booking) vs dostępność pokoi. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Wybrałem **top 3**: **#1 (Xanh SM bateria)**, **#4 (Vinhomes CSKH)**, **#5 (Vinmec wypis)**.

## 🃏 Card #1 — Xanh SM: sự cố hết pin (awaria baterii na trasie)

| Pole | Zawartość |
|------|-----------|
| **Bài toán (1 zdanie)** | Taksówka EV staje na trasie z rozładowaną baterią, a dyspozytor ręcznie znajduje stację, pisze instrukcje i wysyła je kierowcy. |
| **Công ty thành vina** | [x] Xanh SM (GSM) — Điều vận / Zarządzanie flotą |
| **Actor** | Tài xë (czeka zepsuty, zestresowany) + Điều phối viên (przeciążony: ~80 zgłoszeń/dzień w Hà Nội) |
| **Workflow hiện tại (5 kroków)** | 1. Tài xë dzwoni na centralę → 2. Dyspozytor sprawdza pozycję GPS auta → 3. Szuka wolnej stacji sạc VinFast odpowiedniej dla modelu (VF5/VFe34/VF8) → 4. Pisze instrukcję SMS/App dla kierowcy → 5. Dzwoni po pomoc drogową, gdy pin < 5% |
| **Bottleneck (najwolniejszy krok)** | Krok 3 + 4 — ⏱ 10 min z 15 min łącznego czasu (🔴 ręczne szukanie stacji + pisanie wiadomości) |
| **AI może pomóc w kroku** | 3–4: automatyczne pobranie pozycji → znalezienie wolnej stacji → draft wiadomości dla kierowcy |
| **Metric (liczba)** | Czas obsługi zgłoszenia: 15 min → poniżej 3 min; poprawność wskazanej stacji: 98% |
| **Quick Architecture** | [x] LLM Feature (generowanie draftu przy HITL) |

## 🃏 Card #2 — Vinhomes: Klasyfikacja i routowanie skarg mieszkańców

| Pole | Zawartość |
|------|-----------|
| **Bài toán (1 zdanie)** | Skargi mieszkańców (awarie, hałas, administracja) trafiają do jednej kolejki i są ręcznie przekierowywane do właściwych działów przez ~12 godzin. |
| **Công ty thành vina** | [x] Vinhomes — Smart City / Resident Services |
| **Actor** | Mieszkaniec (wpis w aplikacji) + Pracownik CSKH (klasyfikacja ręczna) |
| **Workflow hiện tại (4 kroki)** | 1. Mieszkaniec pisze skargę → 2. CSKH czyta i klasyfikuje → 3. Ręcznie routuje do działu budynku → 4. Pisze szablonową odpowiedź (12h) |
| **Bottleneck** | Krok 2–3 — ⏱ 10 min/skargę; odpowiedzi szablonowe, niska satysfakcja |
| **AI może pomóc w kroku** | 2–3: klasyfikacja + routing + draft odpowiedzi; HITL przed wysyłką |
| **Metric (liczba)** | Czas pierwszego kontaktu: 12h → < 2h; 95% skarg poprawnie zroutowanych bez edycji |
| **Quick Architecture** | [x] LLM Feature (z rule-based routerem fallback) |

## 🃏 Card #3 — Vinmec: Draft streszczenia wypisu (Discharge Summary)

| Pole | Zawartość |
|------|-----------|
| **Bài toán (1 zdanie)** | Lekarz ręcznie pisze streszczenie wypisu dla pacjenta, tracąc 20–30 min na każdy przypadek. |
| **Công ty thành vina** | [x] Vinmec — szpitale / opieka zdrowotna |
| **Actor** | Lekarz prowadzący (przeciążony) + pielęgniarka (weryfikacja) |
| **Workflow hiện tại (4 kroki)** | 1. Lekarz kończy wizytę → 2. Przegląda historię/EHR → 3. Pisze streszczenie ręcznie → 4. Podpisuje i wysyła do rejestracji |
| **Bottleneck** | Krok 3 — ⏱ 20–30 min/pacjenta (język dla pacjenta, dokładność danych klinicznych) |
| **AI może pomóc w kroku** | 2–3: ekstrakcja danych z EHR + draft streszczenia prostym językiem |
| **Metric (liczba)** | Czas pisania: 25 min → < 5 min; 100% streszczeń zatwierdzanych przez lekarza (HITL) |
| **Quick Architecture** | [x] LLM Feature (wysoki risk: błąd kliniczny → obowiązkowy przegląd lekarza) |

---

## ✅ Podsumowanie wyboru do Deep-Dive

Zespół (na bazie tej karty) wybrał **Card #1 — Xanh SM: sự cố hết pin** jako problem do fazy DEEP-DIVE, ponieważ:
* ma realny, mierzalny wpływ operacyjny (~80 zgłoszeń/dzień, 20h pracy zespołu dziennie),
* nadaje się do kontrolowanego pilotażu LLM Feature z obowiązkowym HITL,
* phải ograniczyć ryzyko (błędna stacja przy krytycznym poziomie baterii) — dobrze widoczne granice bezpieczeństwa, które można przetestować promptowo.