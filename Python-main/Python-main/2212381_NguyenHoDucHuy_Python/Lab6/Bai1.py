import pandas as pd
df = pd.read_csv("C:\Users\PC602\Downloads\Automobile_data.csv")

#Xuất dữ liệu đọc từ tập tin "Automobile_data.csv"
#Mặc định sẽ hiển thị 5 dòng đâu và 5 dòng cuối
print(df)

#Xuất 6 dòng đầu tiên
print (df.head(6))

#Xuất 7 dòng cuối cùng 
print (df.tail(7))