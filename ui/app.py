import sys
import os
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage, QPixmap

# --- XỬ LÝ ĐƯỜNG DẪN IMPORT ---
# Lấy đường dẫn thư mục hiện tại (thư mục ui/) và lùi lại 1 bước ra thư mục gốc
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir) # Thêm thư mục gốc vào hệ thống để nhận diện được thư mục core

# Import file UI tĩnh (vì app.py và giaodien_ui.py giờ đã nằm CÙNG thư mục ui)
from giaodien_ui import Ui_MainWindow

# Import các hàm lõi từ thư mục core
from core.Get_frame import get_traffic_image
from core.Yolo_detect import image_processing


# ---------------- LỚP XỬ LÝ CHẠY NGẦM (BACKEND) ----------------
class YoloThread(QThread):
    # Khai báo cấu trúc gói tin gửi về UI: Ảnh (ndarray), Xe máy, Ô tô, Xe buýt, Xe tải, Tổng xe, WTI
    update_signal = Signal(np.ndarray, int, int, int, int, int, int)

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            # Lấy ảnh từ URL
            frame = get_traffic_image("Camera 1") 
            
            if frame is not None:
                # Đẩy ảnh vào hàm YOLO, hàm này trả về 9 thông số
                annotated_frame, person, car, motor, bus, truck, total_vehicles, wti, wti_norm = image_processing(frame) 
                
                # Bắn tín hiệu kèm dữ liệu lên UI
                self.update_signal.emit(annotated_frame, motor, car, bus, truck, total_vehicles, int(wti))
            
            # Nghỉ 100ms để tránh quá tải CPU và nghẽn mạng
            self.msleep(100)

    def stop(self):
        self.running = False
        self.wait()


# ---------------- LỚP ĐIỀU KHIỂN GIAO DIỆN (FRONTEND) ----------------
class TrafficApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Nạp vỏ UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.prog_wti.setValue(0)
        
        # Khởi tạo luồng AI chạy ngầm
        self.yolo_thread = YoloThread()
        self.yolo_thread.update_signal.connect(self.cap_nhat_giao_dien)
        
        # Kết nối sự kiện nút bấm
        self.ui.btn_start.clicked.connect(self.bat_dau)
        self.ui.btn_stop.clicked.connect(self.dung_he_thong)
        
    def bat_dau(self):
        if not self.yolo_thread.isRunning():
            self.ui.lbl_status.setText("Trạng thái: Đang xử lý YOLO...")
            self.ui.lbl_status.setStyleSheet("color: #28a745; font-weight: bold;")
            self.yolo_thread.start()
            
    def dung_he_thong(self):
        if self.yolo_thread.isRunning():
            self.yolo_thread.stop()
            self.ui.lbl_status.setText("Trạng thái: Đã dừng camera.")
            self.ui.lbl_status.setStyleSheet("color: #dc3545; font-weight: bold;")
            self.ui.prog_wti.setValue(0)
            self.ui.lbl_camera.clear()
            self.ui.lbl_camera.setText("KHUNG HIỂN THỊ CAMERA")
            
    def cap_nhat_giao_dien(self, frame, motor, car, bus, truck, total, wti):
        """Hàm này liên tục nhận dữ liệu từ luồng YOLO và đổ lên màn hình"""
        
        self.ui.lcd_motor.display(motor)
        self.ui.lcd_car.display(car)
        self.ui.lcd_bus.display(bus)
        self.ui.lcd_truck.display(truck)
        self.ui.lcd_total.display(total)
        self.ui.prog_wti.setValue(min(wti, 100))
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame_rgb.shape
        bytes_per_line = ch * w
        qt_img = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img)
        
        self.ui.lbl_camera.setPixmap(pixmap.scaled(
            self.ui.lbl_camera.width(),
            self.ui.lbl_camera.height(),
            Qt.KeepAspectRatio
        ))

    def closeEvent(self, event):
        self.dung_he_thong()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrafficApp()
    window.show()
    sys.exit(app.exec())