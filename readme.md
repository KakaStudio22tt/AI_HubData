### 0. Requirement

- Cài gói trong file [requirement.txt](./requirements.txt)
- conda install -r requirements.txt
- pip install -r requirements.txt

### 1. Chức năng thực hiện

#### Tìm kiếm và thống kê đối tượng

- Chọn 1 tập hợp ảnh gồm ít nhất 100 ảnh từ dataset mẫu của FifftyOne
- Viết script để lọc, tìm kiếm các ảnh theo tag/object hoặc theo label class (sử dụng chức năng filter/query trong FiftyOne).
- Đếm tổng số ảnh có đối tượng cần tìm, và tổng số object loại đó trong toàn bộ dataset.
- Vẽ biểu đồ thống kê đơn giản về tần suất xuất hiện các object phổ biến (matplotlib hoặc plotly).
- Hiển thị (show) một số ảnh có object cần tìm trong FiftyOne, xuất ra log danh sách file ảnh tương ứng.

  [Tham chiếu kết quả thực hiện](./notebook/main2.ipynb)
