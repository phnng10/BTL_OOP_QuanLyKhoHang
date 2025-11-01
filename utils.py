# utils.py
import os
import time

# ==========================
#Định dạng và tiện ích chung
# ==========================

def format_currency(amount):
    "Định dạng số tiền có dấu phẩy và đơn vị VNĐ"
    try:
        return f"{amount:,.0f} đ"
    except (ValueError, TypeError):
        return "0 đ"


def confirm_action(message="Bạn có chắc chắn muốn tiếp tục? (y/n): "):
    "Hỏi xác nhận thao tác"
    while True:
        ans = input(message).strip().lower()
        if ans in ["y", "yes"]:
            return True
        elif ans in ["n", "no"]:
            return False
        else:
            print("Vui lòng nhập 'y' hoặc 'n'.")


def pause():
    "Tạm dừng màn hình (ấn Enter để tiếp tục)"
    input("\nNhấn Enter để tiếp tục...")


def clear_screen():
    "Xóa màn hình console (hỗ trợ Windows & macOS/Linux)"
    os.system("cls" if os.name == "nt" else "clear")


def print_title(title):
    "In tiêu đề có khung"
    print("\n" + "=" * 40)
    print(title.center(40))
    print("=" * 40)


def slow_print(text, delay=0.02):
    "In từng ký tự (tạo hiệu ứng chạy chữ nhẹ)"
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()  # xuống dòng
