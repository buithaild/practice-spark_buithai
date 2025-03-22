# import pandas as pd
# import numpy as np

# # Định nghĩa số lượng dòng cần tạo
# num_rows = 25000000

# # Tạo dữ liệu giả lập
# order_ids = np.arange(1, num_rows + 1)
# dates = pd.date_range(start="2013-07-25", periods=num_rows, freq='S')  # Giả lập thời gian theo giây
# customer_ids = np.random.randint(1000, 13000, size=num_rows)
# statuses = np.random.choice(["CLOSED", "PENDING_PAYMENT", "COMPLETE", "PROCESSING"], size=num_rows)

# # Gộp dữ liệu thành DataFrame
# df = pd.DataFrame({
#     "order_id": order_ids,
#     "order_date": dates.strftime('%Y-%m-%d %H:%M:%S.0'),  # Định dạng giống mẫu
#     "customer_id": customer_ids,
#     "status": statuses
# })

# # Lưu vào file CSV
# file_path = "D:\Learn-spark\learn-spark-maide\orders_large.csv"
# df.to_csv(file_path, index=False, header=False)  # Không ghi header

# file_path
 

import pandas as pd
import numpy as np
import os

# Định nghĩa số lượng dòng ước tính (~94.5MB)
estimated_rows = 1000000  # Ước tính khoảng 63 bytes/dòng

# Tạo dữ liệu giả lập
order_ids = np.arange(1, estimated_rows + 1)
dates = pd.date_range(start="2013-07-25", periods=estimated_rows, freq='S')
customer_ids = np.random.randint(1000, 13000, size=estimated_rows)
statuses = np.random.choice(["CLOSED", "PENDING_PAYMENT", "COMPLETE", "PROCESSING"], size=estimated_rows)

df = pd.DataFrame({
    "order_id": order_ids,
    "order_date": dates.strftime('%Y-%m-%d %H:%M:%S.0'),
    "customer_id": customer_ids,
    "status": statuses
})

# Lưu file CSV
file_path = "D:\Learn-spark\learn-spark-maide\orders_60MB.csv"
df.to_csv(file_path, index=False, header=False)

# Kiểm tra kích thước thực tế
file_size = os.path.getsize(file_path) / (1024 * 1024)  # MB
file_path, file_size
