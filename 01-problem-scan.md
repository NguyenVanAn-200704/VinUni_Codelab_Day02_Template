 ## Phase 1 — SCAN

| # | Company | Problem / Opportunity | Pain Point | AI Opportunity |
|---|---|---|---|---|
| 1 | Vinmec | Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary) | Bác sĩ phải rà soát và tổng hợp thủ công thông tin từ nhiều phần của hồ sơ bệnh án, làm tăng thời gian hoàn tất thủ tục xuất viện và có nguy cơ bỏ sót thông tin quan trọng. | AI trích xuất các thông tin liên quan từ bệnh án điện tử, kết quả xét nghiệm, thuốc, thủ thuật và ghi chú lâm sàng để tạo bản nháp Discharge Summary có cấu trúc. Bác sĩ kiểm tra, chỉnh sửa và phê duyệt trước khi sử dụng. |

## Quick Problem Card — Vinmec: AI-Assisted Discharge Summary Drafting

### 1. Actor
- Primary actor: Bác sĩ điều trị / bác sĩ phụ trách xuất viện.
- Secondary actors: Điều dưỡng, nhân viên hành chính y tế, bệnh nhân.

### 2. Current Process
1. Bác sĩ mở hồ sơ bệnh án của bệnh nhân.
2. Xem lại chẩn đoán, diễn biến điều trị và ghi chú lâm sàng.
3. Kiểm tra kết quả xét nghiệm, chẩn đoán hình ảnh và các thủ thuật đã thực hiện.
4. Kiểm tra thuốc điều trị và thuốc khi xuất viện.
5. Tổng hợp các thông tin quan trọng.
6. Tự soạn Discharge Summary.
7. Kiểm tra và hoàn tất hồ sơ xuất viện.

### 3. Bottleneck
Thông tin cần thiết nằm rải rác ở nhiều phần của hồ sơ bệnh án. Bác sĩ phải tìm kiếm, chọn lọc và tổng hợp thủ công trước khi viết Discharge Summary, gây tốn thời gian và có nguy cơ bỏ sót thông tin quan trọng.

### 4. AI Solution
Xây dựng AI assistant có khả năng:
- Trích xuất các thông tin liên quan từ hồ sơ bệnh án điện tử.
- Tổng hợp chẩn đoán, diễn biến điều trị, kết quả quan trọng, thủ thuật, thuốc và kế hoạch follow-up.
- Sinh bản nháp Discharge Summary theo một cấu trúc chuẩn.
- Đánh dấu các thông tin thiếu hoặc chưa chắc chắn để bác sĩ kiểm tra.

AI chỉ tạo bản nháp. Bác sĩ phải review, chỉnh sửa và phê duyệt trước khi hồ sơ được sử dụng.

### 5. Expected Value
- Giảm thời gian bác sĩ dành cho việc tổng hợp và soạn hồ sơ xuất viện.
- Giảm công việc hành chính lặp lại.
- Hạn chế nguy cơ bỏ sót các thông tin quan trọng.
- Tăng tính nhất quán giữa các Discharge Summary.

### 6. Success Metrics
Primary metric:
- Average time to prepare a discharge summary.

Supporting metrics:
- Tỷ lệ draft chỉ cần chỉnh sửa nhỏ trước khi được bác sĩ phê duyệt.
- Tỷ lệ thông tin quan trọng bị bỏ sót.
- Thời gian từ quyết định cho bệnh nhân xuất viện đến khi hoàn tất Discharge Summary.

### 7. AI Fit
High.

Lý do:
- Input chủ yếu là dữ liệu văn bản và dữ liệu có cấu trúc trong hồ sơ bệnh án.
- Bài toán yêu cầu extraction, summarization và text generation, phù hợp với LLM kết hợp rule-based extraction.
- Output có thể được human review trước khi sử dụng nên phù hợp với mô hình Human-in-the-loop.

### 8. Risks / Constraints
- AI có thể hallucinate hoặc thêm thông tin không tồn tại trong bệnh án.
- Có thể bỏ sót thông tin lâm sàng quan trọng.
- Dữ liệu y tế có yêu cầu cao về quyền riêng tư và bảo mật.
- Nội dung AI sinh ra không được coi là quyết định y khoa tự động.

### 9. Human-in-the-loop
Bác sĩ là người chịu trách nhiệm kiểm tra, chỉnh sửa và phê duyệt bản cuối cùng. AI không được tự động phát hành Discharge Summary.

### 10. Initial Scope
Pilot tại một khoa nội trú với một mẫu Discharge Summary chuẩn.

Input:
- Structured EMR data
- Doctor notes
- Lab results
- Medication
- Procedures

Output:
- Draft Discharge Summary for physician review