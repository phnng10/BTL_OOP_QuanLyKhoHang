class Product:
    def __init__(self, product_id, name, price, quantity, category):
        #Khởi tạo đối tượng sản phẩm chung (Product)
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def display_info(self):
        #In ra thông tin sản phẩm cơ bản
        print(f"ID: {self.product_id} - {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: {self.price} - Quantity: {self.quantity}")

    def update_stock(self, amount):
        #Cập nhật lại số lượng hàng tồn kho
        self.quantity += amount
        print(f"Updated quantity: {self.quantity}")

    def check_valid(self):
        #Kiểm tra xem giá và số lượng có hợp lệ không
        return self.price > 0 and self.quantity >= 0


class Toy(Product):
    def __init__(self, product_id, name, price, quantity, age_range):
        #Kế thừa từ Product, tự động gán category = "Toy"
        super().__init__(product_id, name, price, quantity, "Toy")
        self.age_range = age_range  #Độ tuổi phù hợp cho đồ chơi

    def display_info(self):
        #Gọi phương thức hiển thị từ lớp cha rồi thêm thông tin riêng
        super().display_info()
        print(f"Age Range: {self.age_range}")

    def check_valid(self):
        #Vừa kiểm tra điều kiện chung từ Product
        #Vừa đảm bảo age_range không bị bỏ trống
        return super().check_valid() and self.age_range != ""


class Fashion(Product):
    def __init__(self, product_id, name, price, quantity, size, brand):
        #Kế thừa Product, category mặc định là "Fashion"
        super().__init__(product_id, name, price, quantity, "Fashion")
        self.size = size     #Kích cỡ (XS, S, M, L, XL)
        self.brand = brand   #Thương hiệu

    def display_info(self):
        #Gọi hiển thị cơ bản rồi thêm thông tin thời trang
        super().display_info()
        print(f"Size: {self.size} - Brand: {self.brand}")

    def check_valid(self):
        #Danh sách size hợp lệ
        valid_sizes = ["XS", "S", "M", "L", "XL"]
        #Kiểm tra giá, số lượng, size hợp lệ và brand không rỗng
        return super().check_valid() and self.size in valid_sizes and self.brand != ""


class Beverage(Product):
    def __init__(self, product_id, name, price, quantity, volume, is_sugar_free):
        #Kế thừa Product, category mặc định là "Beverage"
        super().__init__(product_id, name, price, quantity, "Beverage")
        self.volume = volume #Dung tích (ml)
        self.is_sugar_free = is_sugar_free #Có đường hay không

    def display_info(self):
        #Gọi hiển thị từ lớp cha và bổ sung thông tin riêng
        super().display_info()
        sugar = "Yes" if self.is_sugar_free else "No"
        print(f"Volume: {self.volume} ml - Sugar-free: {sugar}")

    def check_valid(self):
        #Kiểm tra điều kiện hợp lệ chung + dung tích phải > 0
        return super().check_valid() and self.volume > 0
