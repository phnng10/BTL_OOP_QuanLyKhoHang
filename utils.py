# utils.py
import os
import time

# ==========================
# Các hàm tiện ích dùng chung
# ==========================

def format_currency(amount):
    "Định dạng tiền tệ VNĐ"
    try:
        return f"{amount:,.0f} đ"
    except (ValueError, TypeError):
        return "0 đ"


def confirm_action(message="Bạn có chắc chắn muốn tiếp tục? (y/n): "):
    "Hỏi xác nhận thao tác"
    while True:
        ans = input(message).strip().lower()
        if ans in ("y", "yes"):
            return True
        elif ans in ("n", "no"):
            return False
        else:
            print("Vui lòng nhập 'y' hoặc 'n'.")


def pause():
    "Tạm dừng màn hình"
    input("\nNhấn Enter để tiếp tục...")


def clear_screen():
    "Xóa màn hình console"
    os.system("cls" if os.name == "nt" else "clear")


def print_title(title):
    "In tiêu đề có khung"
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def slow_print(text, delay=0.02):
    "Hiệu ứng in chữ chậm"
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()
