import pandas as pd
import glob

def convert_to_csv():
    print('converting journal excel to csv')
    df_list = list()

    for f in glob.glob('./journal_kr/*.xls'):

        df = pd.read_excel(f)
        print(f, 'opened...')

        author = pd.Series()
        title = pd.Series()
        year = pd.Series()
        doc_type = pd.Series()
        abstract = pd.Series()
        kdc = pd.Series()
        where = pd.Series()
        page = pd.Series()
        name = pd.Series()
        about1 = pd.Series()

        title.set_value(0, list(df.columns.values)[1])

        i = 0
        cnt = -1
        a = 0

        for i in range(len(df.index)):
            doc_type.set_value(i, '국내 학술지')

        while i < len(df.index):
            if df.T.iloc[0][i] == '제목':
                title.set_value(i+1, df.T.iloc[1][i])
            if df.T.iloc[0][i] == '저자':
                author.set_value(cnt+1, df.T.iloc[1][i])
                a = 0
                cnt += 1
            if df.T.iloc[0][i] == '발행년도':
                year.set_value(cnt, df.T.iloc[1][i])
            if df.T.iloc[0][i] == '초록' and a == 0:
                abstract.set_value(cnt, df.T.iloc[1][i])
                a = 1
            if df.T.iloc[0][i] == '학술지명':
                name.set_value(cnt, df.T.iloc[1][i])
            if df.T.iloc[0][i] == '수록면':
                page.set_value(cnt, df.T.iloc[1][i])
            if df.T.iloc[0][i] == '권호사항':
                about.set_value(cnt, df.T.iloc[1][i])
            if df.T.iloc[0][i] == '발행처':
                where.set_value(cnt, df.T.iloc[1][i])
            if df.T.iloc[0][i] == 'KDC':
                kdc.set_value(cnt, df.T.iloc[1][i])
            if df.T.iloc[0][i] == '자료유형':
                doc_type.set_value(cnt, df.T.iloc[1][i])

            i += 1

        print(f, 'categorizing finished...')

        title = title.reset_index(drop=True)
        new_df = pd.DataFrame({'제목': title, '저자': author, '학술지명': name, '권호사항': about1, '발행처': where, '자료유형': doc_type, '수록면': page, '발행년도': year, 'KDC': kdc, '초록': abstract})
        print('df of ' + f + ' complete')
        df_list.append(new_df)
        print('apppending to full list')
    print('done')
    full_df = pd.concat(df_list)
    return full_df
    #full_df.to_csv('journal_kr.csv', sep=',', na_rep='NaN', encoding = 'utf-8')