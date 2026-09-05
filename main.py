import cv2
from core.Get_frame import get_traffic_image, cam_id
from core.Yolo_detect import image_processing

def main():
    print(f"Bắt đầu luồng xử lý nhận diện cho các camera: {list(cam_id.keys())}...")
    print("Nhấn phím 'q' trên cửa sổ hiển thị để thoát chương trình.")

    window_name = "Traffic YOLO Detection"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    while True:
        frame = get_traffic_image("Camera 1")

        if frame is not None:
            annotated_frame, person, car, motorbike, bus, truck, total = image_processing(frame)
            cv2.imshow("Traffic YOLO Detection", annotated_frame)
        else:
            print("Không nhận được hình ảnh từ camera, đang thử lại...")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()