import journal_csv
import book_csv
import degree_csv
import etc_csv
import pandas as pd

df1 = journal_csv.convert_to_csv()
df2 = book_csv.convert_to_csv()
df3 = degree_csv.convert_to_csv()
df4 = etc_csv.convert_to_csv()

df = pd.concat([df1, df2, df3, df4])
cols = ['제목', '저자', '학술지명', '권호사항', '발행처', '자료유형', '수록면', '발행년도', 'KDC', '초록']
df = df[cols]
df.to_csv('output.csv', sep=',')