import streamlit as st 
import pandas as pd 
import plotly.express as px
import io
df = pd.read_csv('fifa_eda - fifa_eda.csv')
def Data_Description():
        st.title('Data Descriptaion')
        st.header('Data Head')
        st.write(df.head(10))
        col1 , col2 = st.columns(2)
        st.write(
    f"""
    <style>
        .line{{
            border: 1px solid black;
            margin: 25px 0;
        }}
    </style>
    <div class="line"></div>
    """,
    unsafe_allow_html=True,
)    
        with col1:
            st.header(' Data Info ' )
            buffer = io.StringIO()
            df.info(buf=buffer)
            s= buffer.getvalue()
            st.text(s)
        with col2:
            st.header('Data Description')
            st.write(df.describe())
        st.header('Categories Distribution')    
        Col3 , Col4 ,Col5 , Col6  = st.columns([1.5,1.5,1,1])
        with Col3 :
            st.write(df['Nationality'].value_counts())
        with Col4 :
            st.write(df['Club'].value_counts())
        with Col5 :
            st.write(df['Preferred Foot'].value_counts())
        with Col6 :
            st.write(df['Position'].value_counts())
       
            
        
        
def Numerical_Charts():
    st.title('Data Visualization')
    st.header('Numerical Graphs')
    st.sidebar.markdown('### Hisogram Charts Options')
    Hist_1 = st.sidebar.selectbox('Select Histogram Columns',['Value','Wage','Release Clause'])
    Fig_Numerical_Histogram = px.histogram(
        data_frame=df,x=Hist_1,text_auto=True,nbins=20,title=Hist_1.capitalize()+ ' ' + 'Distribution') 
    st.plotly_chart(Fig_Numerical_Histogram)
    Sc_x_Col = st.sidebar.selectbox('Select Scatter  X Columns',['Value','Wage','Release Clause'])
    Sc_Y_Col = st.sidebar.selectbox('Select Scatter Y Columns',['Value','Wage','Release Clause'])
    Fig_Numerical_Scatter = px.scatter(data_frame=df ,x=Sc_x_Col,y=Sc_Y_Col)
    st.plotly_chart(Fig_Numerical_Scatter)
 
        
        
def Categoral_Charts():
    st.title('Data Visualization')
    st.header("Categorical Graphs")
    st.sidebar.markdown("### CountPlot Chart Options")
    CountPlot_Col = st.sidebar.selectbox("Select Histogram Col" , ["Nationality","Club","Preferred Foot","Position"]  )
    CountPlot_color_option = st.sidebar.checkbox("Count Plot with color")
    st.sidebar.markdown("### BarPlot Chart Options")
    BarPlot_X_Col = st.sidebar.selectbox("Select Bar X Col" , ["Nationality","Club","Preferred Foot","Position"]  )
    BarPlot_Y_Col = st.sidebar.selectbox("Select Bar Y Col" , ["Value","Wage","Release Clause"]  )
    BarPlot_color_option = st.sidebar.checkbox("Bar Plot with color")
    if CountPlot_color_option:
        CountPlot_color_col = st.sidebar.selectbox("Choose Color Col", ["Nationality","Club","Preferred Foot","Position"] )
        st.plotly_chart(px.histogram(data_frame = df , x = CountPlot_Col ,color = CountPlot_color_col,barmode = "group",title=CountPlot_Col.capitalize() + " Distribution" , labels={CountPlot_Col : CountPlot_Col.capitalize()}))
    else:
        st.plotly_chart(px.histogram(data_frame = df , x = CountPlot_Col ,title=CountPlot_Col.capitalize() + " Distribution" , labels={CountPlot_Col : CountPlot_Col.capitalize()}))
    
    if BarPlot_color_option:
        Bar_color_col = st.sidebar.selectbox("Choose BarColor Col", ["Nationality","Club","Preferred Foot","Position"] )
        st.plotly_chart(px.bar(data_frame = df , x = BarPlot_X_Col, y = BarPlot_Y_Col ,color=Bar_color_col,hover_data=[Bar_color_col] ,title="Summation of " + BarPlot_Y_Col.capitalize()  + "grouped by " + BarPlot_X_Col.capitalize() , labels={BarPlot_X_Col : BarPlot_X_Col.capitalize() , BarPlot_Y_Col:BarPlot_Y_Col.capitalize()}))
    else:
        st.plotly_chart(px.bar(data_frame = df , x = BarPlot_X_Col, y = BarPlot_Y_Col ,title="Summation of " + BarPlot_Y_Col.capitalize()  + " grouped by " + BarPlot_X_Col.capitalize() , labels={BarPlot_X_Col : BarPlot_X_Col.capitalize() , BarPlot_Y_Col:BarPlot_Y_Col.capitalize()}))
    
    
Func_to_Names = {
    
    'Data Description' : Data_Description,
    'Numerical Charts' : Numerical_Charts,
    'Categoral Charts' : Categoral_Charts
    
    
}    


User_Choice = st.sidebar.selectbox('Select Your Page', Func_to_Names.keys())

Func_to_Names[User_Choice]()
