# main.py
from warehouse import Warehouse
from customer import CustomerManager
from order import Order
from product import Toy, Fashion, Beverage
from utils import clear_screen, pause, print_title, confirm_action, format_currency, slow_print


def main():
    slow_print("Khởi động hệ thống quản lý bán hàng...", 0.01)
    warehouse = Warehouse()
    customer_manager = CustomerManager()
    orders = []

    while True:
        clear_screen()
        print_title("HỆ THỐNG QUẢN LÝ BÁN HÀNG")
        print("1. Quản lý sản phẩm")
        print("2. Quản lý kho")
        print("3. Quản lý khách hàng")
        print("4. Quản lý đơn hàng")
        print("5. Thoát")

        choice = input("\n→ Chọn chức năng: ").strip()
        if choice == "1":
            menu_product(warehouse)
        elif choice == "2":
            menu_warehouse(warehouse)
        elif choice == "3":
            menu_customer(customer_manager)
        elif choice == "4":
            menu_order(orders, customer_manager, warehouse)
        elif choice == "5":
            if confirm_action("Bạn có chắc muốn thoát? (y/n): "):
                slow_print("Cảm ơn bạn đã sử dụng chương trình ", 0.02)
                break
        else:
            print(" Lựa chọn không hợp lệ!")
            pause()


# ==== Các menu con (đồng bộ theo class thực tế) ====
def menu_product(warehouse):
    while True:
        clear_screen()
        print_title("QUẢN LÝ SẢN PHẨM")
        print("1. Thêm sản phẩm mới")
        print("2. Hiển thị tất cả sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Quay lại")
        c = input("\n→ Chọn: ").strip()

        if c == "1":
            add_product_ui(warehouse)
        elif c == "2":
            warehouse.show_all()
            pause()
        elif c == "3":
            pid = input("Nhập ID sản phẩm cần xóa: ").strip()
            if confirm_action(f"Xác nhận xóa sản phẩm {pid}? (y/n): "):
                warehouse.remove_product(pid)
            pause()
        elif c == "4":
            break
        else:
            print("Lựa chọn không hợp lệ!")
            pause()


def add_product_ui(warehouse):
    clear_screen()
    print_title("THÊM SẢN PHẨM MỚI")
    pid = input("Mã sản phẩm: ").strip()
    name = input("Tên sản phẩm: ").strip()
    try:
        price = float(input("Giá (VNĐ): "))
        quantity = int(input("Số lượng: "))
    except ValueError:
        print(" Giá hoặc số lượng không hợp lệ!")
        pause()
        return

    print("\nLoại sản phẩm:")
    print("1. Đồ chơi (Toy)")
    print("2. Thời trang (Fashion)")
    print("3. Đồ uống (Beverage)")
    type_choice = input("→ Chọn loại: ").strip()

    if type_choice == "1":
        age = input("Độ tuổi phù hợp: ").strip()
        product = Toy(pid, name, price, quantity, age)
    elif type_choice == "2":
        size = input("Kích cỡ (XS/S/M/L/XL): ").strip().upper()
        brand = input("Thương hiệu: ").strip()
        product = Fashion(pid, name, price, quantity, size, brand)
    elif type_choice == "3":
        try:
            volume = int(input("Dung tích (ml): "))
        except ValueError:
            print("Dung tích phải là số!")
            pause()
            return
        sugar = input("Không đường? (y/n): ").lower() == "y"
        product = Beverage(pid, name, price, quantity, volume, sugar)
    else:
        print(" Lựa chọn không hợp lệ.")
        pause()
        return

    warehouse.add_product(product)
    pause()


def menu_warehouse(warehouse):
    while True:
        clear_screen()
        print_title("QUẢN LÝ KHO HÀNG")
        print("1. Xem hàng sắp hết")
        print("2. Cập nhật tồn kho")
        print("3. Quay lại")
        c = input("\n→ Chọn: ").strip()

        if c == "1":
            warehouse.show_low_stock_items()
            pause()
        elif c == "2":
            pid = input("Mã sản phẩm: ").strip()
            try:
                amount = int(input("Nhập số lượng (+ để nhập, - để xuất): "))
                warehouse.update_stock(pid, amount)
            except ValueError:
                print(" Số lượng phải là số nguyên.")
            pause()
        elif c == "3":
            break
        else:
            print("Lựa chọn không hợp lệ!")
            pause()


def menu_customer(manager):
    while True:
        clear_screen()
        print_title("QUẢN LÝ KHÁCH HÀNG")
        print("1. Thêm khách hàng")
        print("2. Danh sách khách hàng")
        print("3. Cập nhật khách hàng")
        print("4. Xóa khách hàng")
        print("5. Tìm kiếm khách hàng")
        print("6. Quay lại")
        c = input("\n→ Chọn: ").strip()

        if c == "1":
            manager.add_customer()
        elif c == "2":
            manager.show_all()
        elif c == "3":
            manager.update_customer()
        elif c == "4":
            manager.delete_customer()
        elif c == "5":
            manager.search_customer()
        elif c == "6":
            break
        else:
            print(" Lựa chọn không hợp lệ!")
        pause()


def menu_order(orders, customer_manager, warehouse):
    while True:
        clear_screen()
        print_title("QUẢN LÝ ĐƠN HÀNG")
        print("1. Tạo đơn hàng mới")
        print("2. Xem danh sách đơn hàng")
        print("3. Quay lại")
        c = input("\n→ Chọn: ").strip()

        if c == "1":
            create_order(orders, customer_manager, warehouse)
        elif c == "2":
            if not orders:
                print("(Chưa có đơn hàng nào)")
            else:
                for o in orders:
                    print(f" Đơn {o.order_id} - {o.customer.name} - Tổng: {format_currency(o.calculate_total())}")
            pause()
        elif c == "3":
            break
        else:
            print(" Lựa chọn không hợp lệ!")
            pause()


def create_order(orders, customer_manager, warehouse):
    clear_screen()
    print_title("TẠO ĐƠN HÀNG MỚI")
    oid = input("Nhập mã đơn hàng: ").strip()
    customer_id = input("Nhập ID khách hàng: ").strip()
    customer = customer_manager.find_by_id(customer_id)

    if not customer:
        print(" Khách hàng chưa tồn tại, vui lòng thêm trước.")
        pause()
        return

    order = Order(oid, customer, warehouse)

    while True:
        pid = input("Nhập mã sản phẩm (hoặc 0 để dừng): ").strip()
        if pid == "0":
            break
        try:
            quantity = int(input("Số lượng: "))
            order.add_item(pid, quantity)
        except ValueError:
            print("Số lượng không hợp lệ.")
    print(f"ổng tiền: {format_currency(order.calculate_total())}")
    order.export_invoice()
    orders.append(order)
    pause()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Lỗi chương trình: {e}")
