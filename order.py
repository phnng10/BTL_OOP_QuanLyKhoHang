from datetime import datetime
from warehouse import Warehouse
from customer import Customer
from product import Product


# ===============================
# Lớp OrderDetail: chi tiết từng sản phẩm trong đơn
# ===============================
class OrderDetail:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        """Tính tổng tiền của sản phẩm này trong đơn"""
        return self.product.price * self.quantity


# ===============================
# Lớp Order: đại diện cho một đơn hàng
# ===============================
class Order:
    def __init__(self, order_id: str, customer: Customer, warehouse: Warehouse):
        self.order_id = order_id
        self.customer = customer
        self.warehouse = warehouse
        self.items = []  # danh sách OrderDetail
        self.order_date = datetime.now()

    def add_item(self, product_id: str, quantity: int):
        """Thêm sản phẩm vào đơn hàng"""
        product = self.warehouse.search_product(product_id)
        if not product:
            print(f"Không tìm thấy sản phẩm có mã {product_id}.")
            return

        if product.quantity < quantity:
            print(f"Tồn kho của '{product.name}' không đủ (chỉ còn {product.quantity}).")
            return

        # Cập nhật tồn kho
        product.quantity -= quantity

        # Thêm vào danh sách đơn hàng
        detail = OrderDetail(product, quantity)
        self.items.append(detail)
        print(f"Đã thêm {quantity} x {product.name} vào đơn {self.order_id}.")

    def calculate_total(self):
        """Tính tổng tiền của toàn bộ đơn hàng"""
        return sum(item.get_total_price() for item in self.items)

    def export_invoice(self):
        """Xuất hóa đơn ra file .txt"""
        total = self.calculate_total()
        filename = f"invoice_{self.order_id}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write("========== HÓA ĐƠN MUA HÀNG ==========\n")
            f.write(f"Mã đơn hàng: {self.order_id}\n")
            f.write(f"Tên khách hàng: {self.customer.name}\n")
            f.write(f"Ngày lập đơn: {self.order_date.strftime('%d/%m/%Y %H:%M:%S')}\n")
            f.write("--------------------------------------\n")
            for item in self.items:
                f.write(f"{item.product.name} x{item.quantity} = {item.get_total_price():,.0f}đ\n")
            f.write("--------------------------------------\n")
            f.write(f"Tổng cộng: {total:,.0f}đ\n")
            f.write("======================================\n")

        print(f"Hóa đơn đã được xuất ra file: {filename}")


# ===============================
# TEST CHẠY THỬ (chạy trực tiếp file này)
# ===============================
if __name__ == "__main__":
    # Tạo dữ liệu mẫu
    warehouse = Warehouse()
    customer = Customer("C01", "Nguyễn Văn A", "0123456789", "TP.HCM")

    # Thêm vài sản phẩm mẫu vào kho
    p1 = Product("P01", "Áo thun", 120000, 10, "Thời trang")
    p2 = Product("P02", "Nước suối", 8000, 50, "Đồ uống")
    warehouse.add_product(p1)
    warehouse.add_product(p2)

    # Tạo đơn hàng và thêm sản phẩm
    order = Order("O01", customer, warehouse)
    order.add_item("P01", 2)
    order.add_item("P02", 5)

    # Xuất hóa đơn ra file .txt
    order.export_invoice()
  
    
