import streamlit as st
import pandas as pd

def run_eda() :
    st.subheader('탐색적 데이터 분석')

    st.text('데이터프레임 보기 / 통계치 보기를 할 수 잇습니다.')

    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    print(df)

    radio_menu = ['데이터프레임', '통계치']

    choice_radio = st.radio('선택하세요.', radio_menu)

    if choice_radio == radio_menu[0] :
        st.dataframe(df)

    elif choice_radio == radio_menu[1] :
        st.dataframe( df.describe().head(4) )


    # 각 컬럼별로 최대/최소 값을 보여주는 화면 개발.
    # 유저가 컬럼을 선택하면, 해당 컬럼의 최대/최소 데이터를 보여주도록 하자.

    st.text('컬럼을 선택하면, 각 컬럼의 최대/최소 데이터를 보여줍니다.')
    column_list = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    st.selectbox('컬럼을 선택하기', column_list)

    