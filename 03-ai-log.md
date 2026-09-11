# 03. AI Log & Reflection

## 1. AI đã hỗ trợ việc tìm ý tưởng hoặc phân tích như thế nào

Trong quá trình làm bài, tôi đã dùng AI (Claude) để hỗ trợ các thao tác với Git khi làm việc với repo `VinUni_Codelab_Day02_Template`, cụ thể:

- Hướng dẫn cách tạo nhánh (branch) mới bằng `git checkout -b` và `git switch -c`.
- Hướng dẫn clone repo từ GitHub và tạo nhánh làm việc riêng (`dung/lam-bai-tap`).
- Hướng dẫn cách xóa nhánh không cần dùng nữa (`git branch -d` / `-D`).
- Hướng dẫn quy trình `add → commit → push` khi mở lại VSCode sau khi đã tắt terminal.
- Giúp đọc và giải thích các thông báo lỗi Git (ví dụ: lỗi `cannot delete branch ... used by worktree`, lỗi `fatal: not a git repository`).

AI giúp tôi tiết kiệm thời gian tra cứu cú pháp lệnh Git và hiểu rõ hơn nguyên nhân gốc rễ của lỗi thay vì chỉ copy lệnh sửa lỗi một cách máy móc.

## 2. AI đã trả lời sai hoặc hallucinate ở đâu

- Khi tôi báo lỗi "cannot delete branch ... used by worktree", AI đưa ra giả định ban đầu là có thể có **worktree phụ** ở một thư mục khác đang giữ nhánh đó, và gợi ý dùng `git worktree list` / `git worktree remove`. Thực tế sau khi kiểm tra bằng `git branch`, nguyên nhân đơn giản hơn nhiều: tôi **đang đứng ngay trên chính nhánh đó**, không có worktree phụ nào cả. AI đã đưa ra một hướng suy luận rộng hơn cần thiết trước khi có đủ thông tin.
- AI cũng giả định tôi đã chạy `git checkout main` thành công ở bước trước đó (dựa trên hướng dẫn đã đưa ra trước đó), nhưng thực tế lệnh đó chưa được chạy hoặc chưa thành công, dẫn đến việc chẩn đoán ban đầu chưa khớp hoàn toàn với thực tế.
- Không phát hiện hallucinate về mặt cú pháp lệnh Git (các lệnh AI đưa ra đều đúng và chạy được), vấn đề chủ yếu nằm ở việc **suy luận nguyên nhân lỗi** khi chưa có đủ dữ liệu thực tế từ terminal.

## 3. Cách kiểm chứng kết quả

- Tôi luôn chạy lại lệnh AI gợi ý trên terminal thật (VSCode/PowerShell) thay vì tin tưởng ngay kết quả lý thuyết.
- Dùng `git status` và `git branch` để xác minh trạng thái thực tế của repo trước khi thực hiện lệnh tiếp theo (ví dụ: xác nhận đang ở nhánh nào trước khi xóa nhánh).
- So sánh thông báo lỗi thực tế hiển thị trên terminal với lời giải thích của AI để kiểm tra xem có khớp hay không.
- Chụp lại ảnh màn hình kết quả và gửi lại cho AI để AI điều chỉnh hướng dẫn dựa trên dữ liệu thật, thay vì dựa vào giả định.

## 4. Cách sửa prompt hoặc thêm operational boundary

- Thay vì hỏi chung chung "sao bị lỗi", tôi đã gửi kèm **ảnh chụp màn hình kết quả lệnh thực tế** để AI có dữ liệu chính xác thay vì phải đoán.
- Yêu cầu AI xác nhận trạng thái hiện tại (`git branch`, `git status`) trước khi đưa ra bước tiếp theo, thay vì để AI tự giả định các bước trước đã hoàn tất đúng.
- Giới hạn phạm vi câu hỏi theo từng bước nhỏ (một lệnh - một vấn đề) để dễ kiểm chứng, thay vì hỏi gộp nhiều thao tác một lúc.

## 5. Những quyết định cuối cùng do bản thân tự đánh giá

- Tôi là người quyết định **thời điểm** chạy `git checkout main` trước khi xóa nhánh, sau khi tự kiểm tra bằng `git branch` để chắc chắn không bị mất nhánh đang làm việc.
- Tôi tự quyết định **không xóa nhánh `dung/lam-bai-tap`** ngay khi chưa chắc chắn code đã được lưu/push đầy đủ, để tránh mất công sức đã làm.
- Tôi tự kiểm tra lại đường dẫn thư mục (`CODE\VinAI` vs `VinUni_Codelab_Day02_Template`) trước khi chạy `git status`, thay vì làm theo hướng dẫn một cách máy móc khi có dấu hiệu bất thường (lỗi "not a git repository").
- Nội dung commit message và quyết định file nào cần được add/commit (`01-worksheet.md`, `REQUIREMENTS_SUMMARY.md`) là do tôi tự xem xét và quyết định, AI chỉ hỗ trợ cú pháp lệnh.