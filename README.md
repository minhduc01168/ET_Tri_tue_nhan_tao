# Bài tập lớn: Phân tích rủi ro tín dụng qua phương pháp học máy

**Môi trường thực hiện: Google Colab**
**Scoping**
- Bài tập lớn: thuộc bài toán phân loại
- Input: Dữ liệu về khách hàng từ các ngân hàng
- Output: Trả về trạng thái cho vay đối với khách hàng đó

### The dataset
Bộ dữ liệu sẽ được sử dụng được tìm thấy trên [Kaggle](https://www.kaggle.com/datasets/laotse/credit-risk-dataset?resource=download) và nó chứa dữ liệu cho 32.581 người vay và 11 biến (tuổi, thu nhập hàng năm, quyền sở hữu nhà, thời gian làm việc, ý định vay, mức vay, số tiền vay, Lãi suất, tình trạng vay, phần trăm thu nhập, vỡ nợ lịch sử, lịch sử tín dụng) liên quan đến mỗi người vay.

Mô tả:
- person_age: Age in years
- person_income: Annual Income in dollars
- personhomeownership: Home ownership
- personemplength: Employment length (in years)
- loan_intent: Loan intent
- loan_grade: Loan grade
- loan_amnt: Loan amount in dollars
- loanintrate: Interest rate
- loan_status: Loan status (0 is non default 1 is default)
- loanpercentincome: Percent income
- cbpersondefaultonfile: Historical default
- cbpresoncredhistlength: Credit history length

### Xử lý data: [Data](https://github.com/minhduc01168/ET_Tri_tue_nhan_tao/blob/master/BTL_AI_Data.ipynb)
- Kiểm tra các dữ liệu bị thiếu trong bộ dữ liệu
- Thay thế các giá trị bị thiếu trong bộ dữ liệu bằng giá trị trung bình của mỗi biến 
- Loại bỏ các thuộc tính không quan trọng của dữ liệu
- Chuyển đổi các thuộc tính về dạng số 
- Loại bỏ các điểm outliers
### Triển khai các mô hình học máy với các tham số mặc định: [Initial](https://github.com/minhduc01168/ET_Tri_tue_nhan_tao/blob/master/BTL_AI_Train_Test.ipynb)
- KNN
- Decision Tree Classifier
- Random Forest Classifier
- SVM
- Naive Bayes
### Triển khai các mô hình học máy với dữ liệu được xử lý bằng SMOTE: [SMOTE](https://github.com/minhduc01168/ET_Tri_tue_nhan_tao/blob/master/BTL_AI_Train_Test_SMOTE.ipynb) 
### Triển khai các mô hình học máy sau khi sử dụng Hyperparameter tuning: [Hyperparameter tuning](https://github.com/minhduc01168/ET_Tri_tue_nhan_tao/blob/master/Hyperparameter_tuning.ipynb) 
- Tham khảo kiến thức về Hyperparameter tuning: [tại đây](https://www.geeksforgeeks.org/hyperparameter-tuning/?fbclid=IwAR1fMxGEU9pYnBtUnEZnXZjqft1CWhm9Hotk8Bc_0Witanf4B252qOIjhbw)
### Triển khai các mô hình học máy sau khi sử dụng Feature Importance: [Feature Importance](https://github.com/minhduc01168/ET_Tri_tue_nhan_tao/blob/master/Feature_importance.ipynb)
- Feature importance trong học máy để đo lường quan trọng của từng feature (đặc trưng) trong tập dữ liệu. Nó cho ta biết được từng feature có đóng góp nhiều hay ít trong quá trình huấn luyện và dự đoán của mô hình. Có nhiều cách để tính feature importance, nhưng cách thông dụng nhất là sử dụng các thuật toán Decision Tree và Random Forest.
- Kết quả sẽ trả về một mảng giá trị của các feature, trong đó mỗi giá trị tương ứng với một feature trong tập dữ liệu. 
Lưu ý rằng kết quả của tính năng quan trọng có thể khác nhau khi sử dụng các thuật toán khác nhau, và cũng có thể khác nhau khi sử dụng cùng một thuật toán nhưng với các tham số khác nhau.
### Triển khai mạng nơron nhân tạo ANN: [ANN](https://github.com/minhduc01168/ET_Tri_tue_nhan_tao/blob/master/BTL_AI_ANN_normalization.ipynb)
Kết quả: **Accuracy= 0.927**
### Đánh giá hiệu năng: Cross-validation:K-fold
### Triển khai hệ thống: website 
- Phát triển model
- Chuyển đổi model sang định dạng tensorflowjs
- Đưa lên website 

Nguồn tham khảo: [tại đây](https://github.com/daved01/tensorflowjs-web-app-demo?fbclid=IwAR1BPwtxdQwvbKYFtf-_7JV8fvq0TFQ_R5U6z4sziA5YxAR5gl8nA5gx87w)
- Deploy ứng dụng ReactJS lên Netlify hosting miễn phí. 

Nguồn tham khảo: [tại đây](https://www.youtube.com/watch?v=R65aFh-Dstw)

Website demo: [React App](https://netlify-ml-app.netlify.app/?fbclid=IwAR0iS8wRH3HZYoKV6m_VK28bNy9qz656wSv99icDuObV5WshIrwI7jHdIZE) 
### Kết quả 
**Accuracy**
|                     | KNN | Decision Tree Classifier|Random Forest Classifier|SVM  |Naive Bayes|
|---------------------|-----|-------------------------|------------------------|-----|-----------|
|Initial              |0.87 | 0.84                    | 0.92                   |0.88 |0.81       |
|SMOTE                |0.83 | 0.82                    | 0.89                   |0.79 |0.72       |
|Hyperparameter tuning|0.87 | 0.84                    | 0.92                   |0.88 |0.81       |
|Feature importance   |0.87 | 0.84                    | 0.92                   |     |           |
