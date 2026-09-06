# 🚦 Real-Time Traffic Congestion Prediction & Monitoring Pipeline (Ngã Tư Hàng Xanh)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ultralytics YOLO](https://img.shields.io/badge/YOLO-26x-green?style=for-the-badge&logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Supervision](https://img.shields.io/badge/Roboflow-Supervision-orange?style=for-the-badge&logo=roboflow&logoColor=white)](https://github.com/roboflow/supervision)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*Hệ thống giám sát và dự đoán ùn tắc giao thông thời gian thực sử dụng Computer Vision tiên tiến*  
*Môn học: Python for Data Science — Trường Đại học Sư Phạm Kỹ thuật TP. Hồ Chí Minh (HCMUTE)*

</div>

---

## 👥 Tác giả & Thông tin dự án
* **Thực hiện bởi:**
* Nguyễn Tuấn Thịnh — MSSV: `25139048` (GitHub: [`Dev-TNT`](https://github.com/Dev-TNT))
* Nguyễn Lê Phúc Thịnh — MSSV: `25139047` (GitHub: [`thijnh1409`](https://github.com/thijnh1409))
* **Ngành học:** Kỹ thuật Nhúng & IoT — HCMUTE
* **Địa điểm khảo sát:** Ngã tư Hàng Xanh, TP. Hồ Chí Minh (Nguồn dữ liệu: [giaothong.hochiminhcity.gov.vn](https://giaothong.hochiminhcity.gov.vn))

---

## 🏗️ 1. Cấu trúc mã nguồn cốt lõi (Core Codebase)

Dự án được thiết kế theo dạng module hóa gọn gàng, hiệu suất cao:

```text
├── Get_frame.py       # Module thu thập snapshot camera giao thông realtime qua HTTP requests
├── Yolo_detect.py     # Module xử lý thị giác máy tính với YOLO26x & Roboflow Supervision (Inference Slicer)
└── README.md          # Tài liệu giới thiệu dự án
```

---

## ⚙️ 2. Chi tiết các module kỹ thuật

### 2.1. Thu thập dữ liệu thời gian thực (`Get_frame.py`)
* **Cơ chế hoạt động:** Kết nối trực tiếp với hệ thống camera công khai của Sở GTVT TP.HCM thông qua URL render hình ảnh theo thời gian thực kết hợp timestamp (`time.time()`).
* **Quản lý đa camera:** Hỗ trợ giám sát linh hoạt qua từ điển `cam_id` chứa định danh mã camera tại các nút giao trọng điểm khu vực Thủ Đức.
* **Xử lý luồng:** Sử dụng `requests` với các header giả lập trình duyệt và `cv2.imdecode` để chuyển đổi byte stream thành ma trận hình ảnh OpenCV phục vụ cho các bước phân tích tiếp theo.

### 2.2. Nhận diện & Slicing Inference (`Yolo_detect.py`)
* **Mô hình AI:** Sử dụng phiên bản **YOLO26x** (`yolo26x.pt`) mang lại khả năng trích xuất đặc trưng sâu, độ chính xác nhận diện phương tiện vượt trội trong mọi điều kiện khung hình.
* **Roboflow Supervision (`sv.InferenceSlicer`):** 
  * Chia nhỏ khung hình thành các patch kích thước `256x256` để xử lý triệt để bài toán nhận diện các phương tiện nhỏ (xe máy ở khoảng cách xa trong camera góc rộng).
  * Tự động tổng hợp kết quả bounding box thông qua callback tùy chỉnh kết hợp `sv.Detections.from_ultralytics()`.
* **Thống kê & Trực quan hóa:** 
  * Tách bạch và đếm số lượng chi tiết từng loại đối tượng: Người (`Person`), Ô tô (`Car`), Xe máy (`Motorbike`), Xe buýt (`Bus`), và Xe tải (`Truck`).
  * Sử dụng `sv.BoxAnnotator` để vẽ bounding box chuyên nghiệp và đóng dấu timestamp trực tiếp lên khung hình thời gian thực.

---

## 🚀 3. Hướng dẫn cài đặt & Chạy hệ thống

### Bước 1: Cài đặt các thư viện phụ thuộc
```bash
pip install ultralytics supervision opencv-python requests numpy
```

### Bước 2: Chạy module thu thập camera (`Get_frame.py`)
```bash
python Get_frame.py
```
*(Nhấn phím `q` để thoát cửa sổ stream camera trực tiếp).*

### Bước 3: Tích hợp module AI nhận diện và đếm xe (`Yolo_detect.py`)
Import hàm `image_processing` vào pipeline chính của Boss để xử lý từng khung hình thu được từ camera và trích xuất vector số lượng phương tiện phục vụ mô hình dự đoán ùn tắc.

---

## 📅 4. Tiến độ phát triển
* **Giai đoạn 1:** Xây dựng thành công script kết nối API camera công khai và bộ lọc khung hình.
* **Giai đoạn 2:** Tích hợp pipeline YOLO26x + Supervision Inference Slicer tối ưu hóa khả năng đếm xe chi tiết theo loại.
* **Giai đoạn 3:** Xây dựng mô hình chuỗi thời gian & dự đoán thời gian chuyển sang trạng thái ùn tắc (XGBoost/LightGBM).
