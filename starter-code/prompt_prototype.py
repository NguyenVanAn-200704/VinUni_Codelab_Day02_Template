"""
Day 2 — AI Product Scoping (Vin Smart Future)
Prompt Boundary Prototype

Use case:
AI-Assisted Discharge Summary Drafting for Vinmec
"""

import os
import sys
from typing import Any

GEMINI_MODEL = "gemini-2.5-flash"


# ===========================================================================
# 🛡️ Operational Boundaries
#
# Rule 1:
# Output phải LUÔN bắt đầu bằng [DRAFT_ONLY].
#
# Rule 2:
# AI chỉ được sử dụng thông tin có trong hồ sơ được cung cấp.
# Không được tự suy diễn / tạo thêm diagnosis, medication, lab result,
# treatment hoặc follow-up instruction.
#
# Rule 3:
# AI KHÔNG được quyết định bệnh nhân đủ điều kiện xuất viện,
# không được đưa ra chẩn đoán hay quyết định điều trị.
#
# Rule 4:
# Nếu dữ liệu quan trọng bị thiếu hoặc mâu thuẫn:
# không được đoán.
# Phải yêu cầu bác sĩ review bằng:
#
# {
#   "action": "request_physician_review",
#   "reason": "...",
#   "fields": ["..."]
# }
#
# Rule 5:
# Mọi nội dung chỉ là bản nháp và cần bác sĩ phê duyệt.
# ===========================================================================


SYSTEM_PROMPT = """
Bạn là trợ lý AI hỗ trợ bác sĩ Vinmec soạn thảo bản nháp
Discharge Summary (Tóm tắt hồ sơ xuất viện).

Bạn KHÔNG phải bác sĩ và KHÔNG có quyền đưa ra quyết định y khoa.

QUY TẮC BẮT BUỘC:

1. Mọi phản hồi PHẢI bắt đầu chính xác bằng:
[DRAFT_ONLY]

2. Chỉ được sử dụng các thông tin có trong dữ liệu người dùng cung cấp.

3. TUYỆT ĐỐI KHÔNG được:
- Tự tạo hoặc suy diễn chẩn đoán mới.
- Tự tạo thuốc hoặc thay đổi thuốc.
- Tự tạo kết quả xét nghiệm.
- Tự đưa ra chỉ định điều trị.
- Tự quyết định bệnh nhân đủ điều kiện xuất viện.
- Tự tạo hướng dẫn tái khám nếu dữ liệu không cung cấp.

4. Nếu thông tin quan trọng bị thiếu, không rõ hoặc mâu thuẫn,
KHÔNG được tự suy đoán.

Trong trường hợp đó, trả về:

[DRAFT_ONLY]
{
    "action": "request_physician_review",
    "reason": "<mô tả vấn đề>",
    "fields": ["<các trường cần bác sĩ xác nhận>"]
}

5. Nếu dữ liệu đủ, tạo một bản nháp Discharge Summary có cấu trúc gồm:

- Lý do nhập viện
- Chẩn đoán
- Diễn biến điều trị
- Xét nghiệm / chẩn đoán hình ảnh quan trọng
- Thủ thuật / can thiệp
- Thuốc khi xuất viện
- Tình trạng khi xuất viện
- Kế hoạch tái khám / hướng dẫn

Chỉ điền những mục có dữ liệu thực tế.
Nếu một mục không có dữ liệu, ghi "Chưa có thông tin".

6. Không được khẳng định rằng tài liệu đã hoàn tất hoặc đã được phát hành.

7. Bản nháp luôn phải được bác sĩ kiểm tra, chỉnh sửa và phê duyệt
trước khi trở thành hồ sơ y tế chính thức.

Ưu tiên:
Clinical accuracy > completeness > writing style.
"""


def evaluate_prompt(user_input: str) -> str:
    """
    Gọi Gemini 2.5 với SYSTEM_PROMPT và trả về raw response text.
    """

    from google import genai
    from google.genai import types

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY chưa được thiết lập.")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=user_input,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.2,
        ),
    )

    return response.text