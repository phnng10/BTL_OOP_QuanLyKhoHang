import re
class Customer:
    def __init__(self, customer_id, name, phone, address):
        if not self.is_valid_phone(phone):
            raise ValueError(f"Số điện thoại không hợp lệ: {phone}")
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.address = address

    @staticmethod
    def is_valid_phone(phone):
        return bool(re.match(r"^0\d{9}$", phone))

    def update(self, new_name, new_address):
        self.name = new_name
        self.address = new_address
        print(f"Đã cập nhật thông tin cho khách hàng {self.customer_id}")

    def show_info(self):
        print(f"[{self.customer_id}] {self.name} - {self.phone} - {self.address}")

    def __str__(self):
        return f"[{self.customer_id}] {self.name} - {self.phone} - {self.address}"

class CustomerManager:
    def __init__(self):
        self.customers = []  # Danh sách các đối tượng Customer

    def find_by_id(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def add_customer(self):
        print("\n--- THÊM KHÁCH HÀNG ---")
        customer_id = input("Nhập ID khách hàng: ").strip()

        # Kiểm tra trùng ID
        if self.find_by_id(customer_id):
            print(f"Lỗi: ID '{customer_id}' đã tồn tại.")
            return

        name = input("Nhập tên: ").strip()
        phone = input("Nhập SĐT: ").strip()
        address = input("Nhập địa chỉ: ").strip()

        # Kiểm tra và thêm khách hàng
        try:
            customer = Customer(customer_id, name, phone, address)
            self.customers.append(customer)
            print(f"Đã thêm khách hàng '{name}' thành công.")
        except ValueError as e:
            print(f"{e}")

    def show_all(self):
        print("\n--- DANH SÁCH KHÁCH HÀNG ---")
        if not self.customers:
            print("(Chưa có khách hàng nào)")
            return
        for c in self.customers:
            c.show_info()

    def update_customer(self):
        print("\n--- CẬP NHẬT KHÁCH HÀNG ---")
        customer_id = input("Nhập ID khách hàng: ").strip()
        customer = self.find_by_id(customer_id)

        if not customer:
            print(f"Không tìm thấy khách hàng có ID '{customer_id}'.")
            return

        new_name = input(f"Tên mới (hiện tại: {customer.name}): ").strip()
        new_address = input(f"Địa chỉ mới (hiện tại: {customer.address}): ").strip()
        customer.update(new_name, new_address)

    def delete_customer(self):
        print("\n--- XÓA KHÁCH HÀNG ---")
        customer_id = input("Nhập ID khách hàng: ").strip()
        customer = self.find_by_id(customer_id)

        if not customer:
            print(f"Không tìm thấy khách hàng có ID '{customer_id}'.")
            return

        # Xác nhận xóa
        confirm = input(f"Bạn có chắc muốn xóa khách hàng '{customer.name}'? (y/n): ").lower()
        if confirm == "y":
            self.customers.remove(customer)
            print(f"Đã xóa khách hàng '{customer.name}'.")
        else:
            print("Hủy thao tác xóa.")
    
    # Tìm kiếm khách hàng
    def search_customer(self):
        print("\n--- TÌM KIẾM KHÁCH HÀNG ---")
        keyword = input("Nhập tên hoặc SĐT cần tìm: ").strip().lower()

        results = [
            c for c in self.customers
            if keyword in c.name.lower() or keyword in c.phone
        ]

        if results:
            print(f"Tìm thấy {len(results)} kết quả:")
            for c in results:
                c.show_info()
        else:
            print(f"Không tìm thấy khách hàng phù hợp với '{keyword}'.")

if __name__ == "__main__":
    manager = CustomerManager()

    # Thêm khách hàng
    manager.add_customer()
    manager.add_customer()

    # Hiển thị danh sách
    manager.show_all()

    # Cập nhật khách hàng
    manager.update_customer()
    manager.show_all()

    # Tìm kiếm khách hàng
    manager.search_customer()

    # Xóa khách hàng
    manager.delete_customer()
    manager.show_all()
