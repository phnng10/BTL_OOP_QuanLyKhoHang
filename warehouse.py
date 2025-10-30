import pickle
import os

from product import Product, Toy, Fashion, Beverage

class Warehouse:
    """
    Lớp Warehouse quản lý danh sách sản phẩm.
    Thể hiện kỹ thuật Aggregation (Kết hợp) và Encapsulation (Đóng gói).
    """

    def __init__(self, data_file="kho_hang.dat"):
        self.data_file = data_file
        # self.__products là thuộc tính private -> Thể hiện tính Đóng gói
        # Lớp Warehouse "có" một danh sách sản phẩm -> Thể hiện tính Kết hợp
        self.__products = self.load_products()
        print(f"Hệ thống kho sẵn sàng (Đã tải {len(self.__products)} sản phẩm).")

    def add_product(self, product):
        """Thêm sản phẩm mới. (CRUD: Create)"""
        if self.search_product(product.product_id):
            print(f"Lỗi: ID '{product.product_id}' đã tồn tại.")
            return

        # Sử dụng Đa hình: Tự động gọi check_valid() của Toy, Fashion...
        if product.check_valid():
            self.__products.append(product)
            print(f"Đã thêm: {product.name}")
            self.save_products()
        else:
            print(f"Lỗi: Thông tin sản phẩm '{product.name}' không hợp lệ.")

    def remove_product(self, product_id):
        """Xóa sản phẩm. (CRUD: Delete)"""
        product = self.search_product(product_id)
        if product:
            self.__products.remove(product)
            print(f"Đã xóa: {product.name}")
            self.save_products()
        else:
            print(f"Lỗi: Không tìm thấy ID {product_id}.")

    def search_product(self, product_id):
        """Tìm sản phẩm theo ID. (CRUD: Read)"""
        for p in self.__products:
            if p.product_id == product_id:
                return p
        return None

    def show_all(self):
        """Hiển thị tất cả sản phẩm."""
        if not self.__products:
            print("Kho hàng hiện đang trống.")
            return
        print("\n=== DANH SÁCH SẢN PHẨM ===")
        for p in self.__products:
            # Sử dụng Đa hình: Tự động gọi display_info() tương ứng
            p.display_info()
            print("-" * 20)

    def update_stock(self, product_id, amount):
        """Cập nhật tồn kho (nhập/xuất). (CRUD: Update)"""
        product = self.search_product(product_id)
        if product:
            if amount < 0 and product.quantity < abs(amount):
                print(f"Lỗi: '{product.name}' không đủ tồn kho (Còn {product.quantity}).")
            else:
                product.update_stock(amount)
                print(f"Đã cập nhật tồn kho cho '{product.name}'.")
                self.save_products()
        else:
            print(f"Lỗi: Không tìm thấy ID {product_id}.")

    def get_low_stock_items(self, threshold=10):
        """Cảnh báo hàng sắp hết."""
        low_stock_list = []
        for p in self.__products:
            if p.quantity < threshold:
                low_stock_list.append(p)
        return low_stock_list
    
    def show_low_stock_items(self, threshold=10):
        """Hiển thị các sản phẩm sắp hết hàng."""
        items = self.get_low_stock_items(threshold)
        if not items:
            print(f"\nKhông có sản phẩm nào dưới {threshold} đơn vị.")
        else:
            print(f"\n=== CẢNH BÁO: SẢN PHẨM SẮP HẾT (Dưới {threshold}) ===")
            for item in items:
                print(f"ID: {item.product_id} - {item.name} (Chỉ còn: {item.quantity})")

    def save_products(self):
        """Lưu danh sách __products ra file."""
        try:
            with open(self.data_file, 'wb') as f:
                pickle.dump(self.__products, f)
        except IOError as e:
            print(f"Lỗi: Không thể lưu file {self.data_file}. Lỗi: {e}")

    def load_products(self):
        """Tải danh sách sản phẩm từ file."""
        if not os.path.exists(self.data_file):
            return []  # File mới, kho trống
        try:
            with open(self.data_file, 'rb') as f:
                return pickle.load(f)
        except (pickle.UnpicklingError, EOFError, FileNotFoundError):
            print(f"Cảnh báo: File dữ liệu bị lỗi. Bắt đầu với kho trống.")
            return []