# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**. 

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:
* 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
* 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
* 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
* 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
* 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **G1. Workflow Mapping** | 20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck |
| **G2. Problem Statement** | 20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** | 10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback |
| **G4. Decision Quality** | 10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng |

### 👤 Điểm cá nhân (40 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **I1. Scan & Cards** | 15 | Quick Cards | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng |
| **I2. Prototyping** | 10 | 02-lab/ | Chạy thử nghiệm programmatic prompt prototype thành công |
| **I3. AI Log & Reflection** | 15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|----------------------|
| 1 | Xanh SM | Forecasting / Optimization | Dự đoán nhu cầu theo giờ/khu vực để tối ưu điều phối (dispatch), giảm tỷ lệ xe chạy rỗng đang ở mức 15-25% |
| 2 | Xanh SM | Optimization / Resource Allocation | Cân bằng tải trạm đổi pin theo khung giờ cao điểm, giảm thời gian chờ 10-15 phút/lượt |
| 3 | Xanh SM | Predictive Maintenance | Bảo trì dự đoán dựa trên dữ liệu cảm biến (pin, phanh, truyền động) thay vì lịch cố định theo km/thời gian |
| 4 | Xanh SM | NLP / Classification | Tự động phân loại & hỗ trợ soạn phản hồi khiếu nại CSKH, giảm 30-40% thời gian xử lý ticket |
| 5 | Xanh SM | Anomaly Detection | Phát hiện gian lận cuốc xe/khuyến mãi và hành vi lái ẩu theo thời gian thực bằng mô hình ML |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                         │
│                                                                │
│ Bài toán (1 câu): Dự đoán nhu cầu cuốc xe theo giờ/khu vực để │
│ tối ưu điều phối, giảm tỷ lệ xe chạy rỗng (deadheading)       │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes    │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________    │
│                                                                │
│ Ai đang đau (Actor)? Tài xế (thu nhập giảm khi chạy rỗng),    │
│ Bộ phận Operations/Dispatch (KPI hiệu suất đội xe)            │
│                                                                │
│ Workflow thủ công hiện tại (3-5 bước):                        │
│   1. Tài xế bật app chờ cuốc ──> 2. Hệ thống ghép theo         │
│   khoảng cách gần nhất (rule-based) ──> 3. Tài xế di chuyển    │
│   đến điểm đón (có thể xa) ──> 4. Trả khách, quay lại chờ      │
│                                                                │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 - ghép cuốc không dự   │
│ đoán cầu theo khu vực (⏱ cần đo baseline thật, chưa có số nội  │
│ bộ — benchmark ngành: 15-25%, KHÔNG dùng làm target)           │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 - forecasting     │
│ cầu theo giờ/khu vực (time-series) + bài toán ghép cung-cầu    │
│                                                                │
│ Đo thành công bằng gì (Metric có số)? [CẦN ĐO BASELINE 2 TUẦN  │
│ TRƯỚC] Giảm tỷ lệ deadheading X% so với baseline thực đo được; │
│ tăng số cuốc/xe/ngày                                           │
│                                                                │
│ Quick Architecture: [ ] No AI  [x] Rule/OR  [ ] LLM  [ ] Agent │
│ Ghi chú: Bài toán OR/matching + forecast (ARIMA/XGBoost),      │
│ KHÔNG cần LLM — cần deterministic, audit được, chạy real-time  │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                         │
│                                                                │
│ Bài toán (1 câu): Bảo trì dự đoán dựa trên dữ liệu cảm biến    │
│ xe điện thay vì lịch bảo dưỡng cố định theo km/thời gian       │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes     │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________     │
│                                                                 │
│ Ai đang đau (Actor)? Đội bảo trì/xưởng dịch vụ, tài xế         │
│ (mất thu nhập khi xe downtime ngoài kế hoạch)                  │
│                                                                 │
│ Workflow thủ công hiện tại (3-5 bước):                         │
│   1. Xe chạy đến mốc km/thời gian cố định ──> 2. Đặt lịch      │
│   bảo dưỡng tại xưởng ──> 3. Kỹ thuật viên kiểm tra thủ công   │
│   toàn bộ hạng mục ──> 4. Thay thế linh kiện theo checklist    │
│                                                                 │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1 - lịch cố định không   │
│ phản ánh tình trạng thực tế (⏱ cần đo % downtime ngoài kế      │
│ hoạch thực tế + xác nhận không phải do thiếu phụ tùng tồn kho) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1 - cảnh báo sớm từ │
│ ngưỡng cảm biến (nhiệt độ pin, điện áp, phanh) + anomaly detect│
│                                                                 │
│ Đo thành công bằng gì (Metric có số)? [CẦN ĐO BASELINE THẬT]   │
│ Giảm số lần downtime ngoài kế hoạch X% so với baseline; giảm   │
│ chi phí thay linh kiện còn tốt trước hạn                       │
│                                                                 │
│ Quick Architecture: [ ] No AI  [x] Rule/ML cổ điển  [ ] LLM    │
│                                                        [ ] Agent│
│ Ghi chú: Threshold rules + gradient boosting trên feature      │
│ engineering từ sensor. KHÔNG cần LLM — chi phí thấp, dễ audit  │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                         │
│                                                                 │
│ Bài toán (1 câu): Tự động phân loại & hỗ trợ soạn phản hồi     │
│ khiếu nại CSKH tài xế/khách hàng                               │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes     │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________     │
│                                                                 │
│ Ai đang đau (Actor)? Nhân viên tổng đài CSKH, tài xế/khách     │
│ hàng chờ phản hồi                                              │
│                                                                 │
│ Workflow thủ công hiện tại (3-5 bước):                         │
│   1. Khiếu nại vào qua app/hotline ──> 2. NV đọc, phân loại    │
│   thủ công ──> 3. NV tra cứu chính sách, soạn phản hồi ──>     │
│   4. Gửi phản hồi, đóng ticket                                 │
│                                                                 │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 - phân loại và soạn  │
│ phản hồi thủ công (⏱ cần đo thời gian trung bình/ticket thực   │
│ tế tại Xanh SM, không dùng số ngành 30-40% làm target)         │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 - LLM phân      │
│ loại tự động + gợi ý draft phản hồi theo policy có sẵn (RAG)   │
│                                                                 │
│ Đo thành công bằng gì (Metric có số)? [CẦN ĐO BASELINE THẬT]   │
│ Giảm thời gian xử lý trung bình/ticket X phút so với baseline; │
│ tăng CSAT; giữ nguyên/giảm tỷ lệ escalation                    │
│                                                                 │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent    │
│ Ghi chú: Đây là use case hợp lý nhất cho LLM — input phi cấu   │
│ trúc (ngôn ngữ tự nhiên), cần hiểu ngữ cảnh và soạn thảo        │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
**Vẽ quy trình hiện tại lên bảng/giấy A3.** Sử dụng các ký hiệu:
* 🔴 **Bottleneck:** Bước gây tắc nghẽn, tốn thời gian, hoặc sai sót nhiều nhất.
* 🔄 **Handoff:** Điểm chuyển giao thông tin giữa người và hệ thống, hoặc giữa các bộ phận.
* Ghi rõ thời gian vận hành trung bình: **Tổng cộng = ____ phút/lượt**.

**Bài toán:** Xử lý khiếu nại CSKH tài xế/khách hàng — Xanh SM

┌──────────────┐      🔄        ┌──────────────┐      🔄        ┌──────────────┐
│ 1. Khách/Tài  │ ──────────────>│ 2. NV tổng    │ ──────────────>│ 3. NV tra    │
│ xế gửi khiếu  │  (App/Hotline  │ đài đọc, phân │  (chuyển ticket│ cứu chính    │
│ nại qua app   │   → hệ thống   │ loại thủ công │   theo loại    │ sách nội bộ  │
│ hoặc hotline  │   ticket)      │ (billing/xe/  │   sang đúng    │ (wiki, file  │
│               │                │ thái độ...)   │   bộ phận)     │ excel, SOP)  │
└──────────────┘                └──────┬───────┘                └──────┬───────┘
                                        │ 🔴                            │
                                        │ Bottleneck:                   │
                                        │ Phân loại sai/chậm             │
                                        │ do khối lượng lớn,             │
                                        │ thiếu ngữ cảnh rõ ràng         │
                                        ▼                                ▼
                                                                  ┌──────────────┐
                                                                  │ 4. NV soạn    │
                                                                  │ phản hồi thủ  │
                                                                  │ công, gửi cho │
                                                                  │ khách/tài xế  │
                                                                  └──────┬───────┘
                                                                         │ 🔴
                                                                         │ Bottleneck:
                                                                         │ Soạn thảo lặp lại
                                                                         │ nội dung tương tự,
                                                                         │ tốn thời gian nhất
                                                                         ▼
                                                                  ┌──────────────┐
                                                                  │ 5. Đóng ticket,│
                                                                  │ lưu log, (đôi  │
                                                                  │ khi) khảo sát  │
                                                                  │ CSAT           │
                                                                  └──────────────┘

**Chú thích:**
🔴 Bottleneck #1 — Bước 2 (Phân loại thủ công): NV phải đọc toàn bộ nội dung, 
    tự gán nhãn loại khiếu nại, dễ sai khi khối lượng ticket tăng đột biến 
    (giờ cao điểm, sự cố hệ thống diện rộng)
🔴 Bottleneck #2 — Bước 4 (Soạn phản hồi): Phần lớn khiếu nại lặp lại 
    (hoàn tiền, lỗi app, xe bẩn...) nhưng NV vẫn soạn tay từng câu, 
    không có template/gợi ý tự động theo ngữ cảnh

🔄 Handoff #1 — Bước 1→2: Khách hàng/tài xế → Hệ thống ticket → NV tổng đài
🔄 Handoff #2 — Bước 2→3: NV tổng đài → NV chuyên trách theo loại vấn đề 
    (có thể khác phòng ban, gây độ trễ chờ chuyển giao)

**Tổng thời gian vận hành trung bình: = _____ phút/lượt**
   (Cần đo thực tế qua log hệ thống ticket — KHÔNG dùng số benchmark ngành. 
   Gợi ý cách đo: lấy timestamp "ticket created" → "ticket closed" từ 
   CRM/hotline system trong 2 tuần, tính trung bình theo từng loại khiếu nại)                                                                  

## 3.2. Problem Statement (6-field) & Metrics (15 min)

**Bài toán:** Xử lý khiếu nại CSKH tài xế/khách hàng — Xanh SM

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên tổng đài CSKH (đọc, phân loại, soạn phản hồi); NV chuyên trách theo bộ phận (billing, kỹ thuật xe, thái độ tài xế); khách hàng/tài xế là người gửi và chờ phản hồi |
| **2. Current Workflow** | Khiếu nại vào qua app/hotline → hệ thống tạo ticket → NV tổng đài đọc và tự phân loại thủ công theo kinh nghiệm cá nhân → chuyển ticket sang đúng bộ phận (nếu cần) → NV tra cứu chính sách nội bộ (wiki/file excel/SOP) → soạn phản hồi tay từng câu → gửi và đóng ticket. Công cụ: hệ thống ticket nội bộ + tài liệu chính sách rời rạc, chưa có tra cứu tập trung |
| **3. Bottleneck** | Bước phân loại (đọc hiểu nội dung tự do, gán nhãn thủ công, dễ sai khi khối lượng tăng đột biến) và bước soạn phản hồi (phần lớn nội dung lặp lại nhưng vẫn gõ tay từng lần) — đây là 2 bước cần xử lý ngôn ngữ tự nhiên (NLP) nhiều nhất |
| **4. Business Impact** | [CẦN ĐO BASELINE THẬT từ log CRM/hotline 2 tuần] — ước tính sơ bộ: thời gian xử lý trung bình/ticket, số ticket tồn đọng giờ cao điểm, tỷ lệ escalation do phản hồi chậm/sai, ảnh hưởng đến điểm CSAT và SLA nội bộ của Xanh SM |
| **5. Success Metric** | VD (cần điền số thật sau khi đo baseline): "≥80% ticket được phân loại đúng trong <10 giây"; "Giảm thời gian xử lý trung bình/ticket từ X phút baseline xuống dưới Y phút"; "CSAT không giảm hoặc tăng ≥Z điểm sau triển khai" |
| **6. Operational Boundary** | **Được làm:** phân loại ticket, gợi ý/draft nội dung phản hồi dựa trên policy có sẵn (RAG), tóm tắt ngữ cảnh cho NV. **TUYỆT ĐỐI không được:** tự động gửi phản hồi liên quan đến hoàn tiền/bồi thường mà không qua duyệt người; tự ý cam kết chính sách ngoài SOP; xử lý khiếu nại liên quan an toàn/tai nạn mà không escalate ngay cho người. **Cần duyệt (human-in-the-loop):** mọi phản hồi có giá trị hoàn tiền/bồi thường vượt ngưỡng, mọi ticket được gắn cờ nhạy cảm (khiếu nại pháp lý, an toàn, truyền thông) |

## 3.3. Future-State Flow & AI Fit (25 min)
* **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào? [ ] Rule / State-Machine [ ] LLM Feature [ ] Agentic Loop.
* **Vẽ Future-State Flow:** Đánh dấu rõ:
  * 🔵 **AI Step:** Tác vụ LLM xử lý.
  * 🟢 **Human Step (HITL):** Bước con người phê duyệt/review (Human-in-the-loop).
  * ↩️ **Fallback:** Kế hoạch dự phòng khi LLM trả về kết quả lỗi hoặc không tự tin.

---

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

Để đảm bảo kỹ sư của Vin Smart Future luôn giữ vững năng lực lập trình, nhóm của bạn sẽ tiến hành **lập trình bản mẫu prompt** trực tiếp trên **Gemini 2.5 Flash** bằng Python để stress-test hệ thống.

### Hướng dẫn thực hiện:
1. Mở file [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) bằng VS Code/Cursor.
2. Hoàn thiện các nội dung sau:
   * **System Prompt:** Viết chỉ thị cực kỳ nghiêm ngặt quy định vai trò, nhiệm vụ, định dạng output và **Operational Boundary (Ranh giới cấm)** của mô hình.
   * **Structured Output:** Định nghĩa định dạng JSON output rõ ràng.
   * **Adversarial Test Cases:** Viết ít nhất 3 prompts "tấn công" (Adversarial inputs) cố tình dụ AI vượt ranh giới hoặc đưa ra câu trả lời không được phép để kiểm tra xem ranh giới của bạn có thực sự vững chắc.
3. Chạy file python:
   ```bash
   python3 prompt_prototype.py
   ```
4. Kiểm tra xem các ranh giới an toàn có bị LLM phá vỡ hay không và ghi lại kết quả vào worksheet.

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [ ] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
2. [ ] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
3. [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[ ] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> *Viết lý giải chi tiết tại đây*

---

# 📝 Phase 6 — REFLECTION (Cá nhân)
*Ghi nhận phản ánh của cá nhân bạn về việc phối hợp với AI trong buổi học hôm nay vào file `03-ai-log.md`.*
