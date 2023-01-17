# Bài tập lớn: Phân tích rủi ro tín dụng qua phương pháp học máy

Scoping
Bài tập lớn: thuộc bài toán phân loại
Input: Dữ liệu về khách hàng từ các ngân hàng
Output: Trả về trạng thái cho vay đối với khách hàng đó

### The dataset
Bộ dữ liệu sẽ được sử dụng được tìm thấy trên [Kaggle](https://www.kaggle.com/datasets/laotse/credit-risk-dataset?resource=download) và nó chứa dữ liệu cho 32.581 người vay và 11 biến (tuổi, thu nhập hàng năm, quyền sở hữu nhà, thời gian làm việc, ý định vay, mức vay, số tiền vay, Lãi suất, tình trạng vay, phần trăm thu nhập, vỡ nợ lịch sử, lịch sử tín dụng) liên quan đến mỗi người vay.

Mô tả:
* person_age: Age in years
* person_income: Annual Income in dollars
* personhomeownership: Home ownership
* personemplength: Employment length (in years)
* loan_intent: Loan intent
* loan_grade: Loan grade
* loan_amnt: Loan amount in dollars
* loanintrate: Interest rate
* loan_status: Loan status (0 is non default 1 is default)
* loanpercentincome: Percent income
* cbpersondefaultonfile: Historical default
* cbpresoncredhistlength: Credit history length
