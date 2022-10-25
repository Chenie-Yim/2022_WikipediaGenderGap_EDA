from turtle import color
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly import graph_objects as go
import altair as alt
from PIL import Image
import hiplot as hip
from streamlit_option_menu import option_menu
import tkinter as Tk

# streamlit run mid.py

# ===== HEADER
st.set_page_config(page_title='Wikipedia, Mind the Gender Gap')
header = st.container()
with header:
    st.title('Monitoring the Gender Gap in the Spanish Wikipedia')
    st.text('Gender Inequality in New Media?')

# ===== SIDEBAR MENU (HORIZONTAL)
selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={"nav-link-selected":{"background-color": "green"},},
)

# ===== LOAD DATA
df = pd.read_csv('MidProject-Gender Gap in Spanish WP Data Set.csv')

if selected == "Home":
    st.subheader(":low_brightness:Purpose of this project")
    st.write("""
    This project focuses on the analysis of everyday gender bias.

    Today, even though we are familiar with the concept of the gender gap, gender discrimination, and so on,
    we are hardly aware of the gender gap in digital sources.
    The gender bias on Wikipedia is one example. """)

    st.write("""
    According to the research on 'students' use of Wikipedia as an academic resource',
    about 87% of students use Wikipedia for their academic work. 
    """)

    st.write("""
    As a widely used educational source, Wikipedia looks quite objective and seems to have no reason to be unequal at all.
    However, surprisingly, Wikipedia is not equal material and failed to reach gender equality
    even though they took a self-plan to increase women-contributors.
    """)

    st.subheader(":low_brightness:Gender Gap on Wikipedia")
    st.write("""Wikipedia's Gender gap, as known as Gender Bias on Wikipedia supposes two problems in Wikipedia; \n
    1) the contributors of Wikipedia are mainly men, \n
    2) women-related topics are not well-covered.""")
    
    st.write("""With this concept, I analyzed the contributors' gender in the Spanish Wikipedia to answer these questions: \n
    1) Is Wikipedia a gender-equal source in terms of participants? \n
    2) Is Wikipedia gender-equal in terms of content?""")
    st.write("""This project has significant meaning since pointing out gender bias can help us be aware of unfairness and inequality in society and we can one step forward to make more equal opportunities for both genders.""")

    st.subheader(":low_brightness:Sub")
    st.write("""The analysis on Wikipedia gender gap will propose a new finding on unrevealed bias of content resources and wake us up to be aware of uneven playing field. Through this project, 
    I wish these kinds of project can be extended to the awareness of bias in code(programming) as we know the majority of technical filed is mainly men.""")
    
if selected == "Projects":
    # ===== PLOT MENU (HORIZONTAL)
    plot1 = st.container()
    plot2 = st.container()
    plot3 = st.container()
    plot4 = st.container()
    plot5 = st.container()
    plot6 = st.container()
    plot7 = st.container()
    
    st.dataframe(data = df) # DATA

    # ===== PLOT 1: BAR CHART (Count Plot) - Total number of contributors (women vs. men)
    with plot1:
        st.subheader(":one:Total Number of Contributors By Gender")
        #source = {"Gender": ["Female", "Male", "Unknown"], 
        #    "Number": [df[df["gender"] == 2].count()["gender"], 
        #                df[df["gender"] == 1].count()["gender"], 
        #                df[df["gender"] == 0].count()["gender"]]}
        #data1=pd.DataFrame(source)
        #data1=data1.set_index("Gender")
        #st.bar_chart(data1, use_container_width=True)
        
        fig1 = plt.figure(figsize=(10, 4))
        sns.set_style("darkgrid", {"axes.facecolor": ".2"})
        sns.countplot(x="gender", data=df, palette=['gray','lightblue','violet'])
        st.pyplot(fig1)
        st.write("""Q1. How many women are among the active editors in the Spanish Wikipedia?""")
        st.caption(""":point_right: The column named as unknown includes both female and male, but they did not reveal their identity (gender) for public. 
        Among the groups who revealed their identity for public, men accounts for about 85% and women account for about 15%. 
        That is, the number of female contributors is 5 times lower than that of men.""")

    # ===== PLOT 2: LINE CHART - active percentage
    with plot2:
        st.subheader(":two:Gender Difference in Activity Duration")
        st.caption(":point_right: dd")
        df['activepercent'] = df['NActDays']/df['NDays']*100
        
        labels_plot2 = ['Women + Men','Women Only', 'Men Only']
        fig2_yaxis = st.radio("""Multiline Chart with """, labels_plot2)
        

        if fig2_yaxis == "Women + Men":
            df['activepercent'] = df['NActDays']/df['NDays']*100
            df_all = df.where(df['gender'] != 0).dropna()

            line1 = alt.Chart(df_all).mark_line(interpolate='basis').encode(
                x='NDays:Q',
                y='activepercent:Q',
                color='gender:N'
            )

            nearest1 = alt.selection(type='single', nearest=True, on='mouseover', fields=['NDays'], empty='none')

            selectors1 = alt.Chart(df_all).mark_point().encode(
                x='NDays:Q',
                opacity=alt.value(0),
            ).add_selection(nearest1)

            points1 = line1.mark_point().encode(
                opacity=alt.condition(nearest1, alt.value(1), alt.value(0)))

            text1 = line1.mark_text(align='left', dx=5, dy=-5).encode(
                text=alt.condition(nearest1, 'activepercent:Q', alt.value(' ')))

            rules1 = alt.Chart(df_all).mark_rule(color='gray').encode(
                x='NDays:Q',
            ).transform_filter(nearest1)


            lines1 = line1.mark_line().encode(
                size=alt.condition(~nearest1, alt.value(1), alt.value(3))).interactive()

            fig11 = alt.layer(
                lines1, selectors1, points1, rules1, text1
            ).properties(width=750, height=300)
            fig11

        # ====== WOMEN
        elif fig2_yaxis == "Women Only":
            df['activepercent'] = df['NActDays']/df['NDays']*100
            df_women = df.where(df['gender']==2).dropna()

            line2 = alt.Chart(df_women).mark_line(interpolate='basis').encode(
                x='NDays:Q',
                y='activepercent:Q',
                color=alt.value("#c43a36"),
            )

            nearest2 = alt.selection(type='single', nearest=True, on='mouseover', fields=['NDays'], empty='none')

            selectors2 = alt.Chart(df_women).mark_point().encode(
                x='NDays:Q',
                opacity=alt.value(0),
            ).add_selection(nearest2)

            points2 = line2.mark_point().encode(
                opacity=alt.condition(nearest2, alt.value(1), alt.value(0)))

            text2 = line2.mark_text(align='left', dx=5, dy=-5).encode(
                text=alt.condition(nearest2, 'activepercent:Q', alt.value(' ')))

            rules2 = alt.Chart(df_women).mark_rule(color='gray').encode(
                x='NDays:Q',
            ).transform_filter(nearest2)

            lines2 = line2.mark_line().encode(
                size=alt.condition(~nearest2, alt.value(1), alt.value(3))).interactive()

            fig2 = alt.layer(
                lines2, selectors2, points2, rules2, text2
            ).properties(width=750, height=300)
            fig2
        
        # ====== MEN
        elif fig2_yaxis == "Men Only":
            df_men = df.where(df['gender']==1).dropna()

            line3 = alt.Chart(df_men).mark_line(interpolate='basis').encode(
                x='NDays:Q',
                y='activepercent:Q',
                color=alt.value("#147252")
            )

            nearest3 = alt.selection(type='single', nearest=True, on='mouseover', fields=['NDays'], empty='none')

            selectors3 = alt.Chart(df_men).mark_point().encode(
                x='NDays:Q',
                opacity=alt.value(0),
            ).add_selection(nearest3)

            points3 = line3.mark_point().encode(
                opacity=alt.condition(nearest3, alt.value(1), alt.value(0)))

            text3 = line3.mark_text(align='left', dx=5, dy=-5).encode(
                text=alt.condition(nearest3, 'activepercent:Q', alt.value(' ')))

            rules3 = alt.Chart(df_men).mark_rule(color='gray').encode(
                x='NDays:Q',
            ).transform_filter(nearest3)

            lines3 = line3.mark_line().encode(
                size=alt.condition(~nearest3, alt.value(1), alt.value(3))).interactive()

            fig3 = alt.layer(
                lines3, selectors3, points3, rules3, text3
            ).properties(width=750, height=300)
            fig3

        fig2_1 = plt.figure(figsize=(6,2))
        sns.kdeplot(data=df, x='NDays', hue='gender',
            fill=True, multiple='stack', common_norm=False, common_grid=True, palette="icefire") # cumulative=True, 
        st.pyplot(fig2_1)

        fig2_2 = plt.figure(figsize=(6,2))
        sns.kdeplot(data=df, x='activepercent', hue='gender',
            fill=True, multiple='stack', common_norm=False, common_grid=True, palette="icefire") # cumulative=True, 
        st.pyplot(fig2_2)

        st.write("""Q2. Do women and men continue as ediotrs for similar periods of time?""")
        st.caption(":point_right: Female vs. Male")


    # ===== PLOT 3: Funnel Plot: number of edits (women vs. men) - Namespace
    with plot3:
        st.subheader(":three:Gender Difference in Editing Practices (Median)")
        labels_plot3 = ['General Pages','Namespaces', 'Pages Related to Women']
        fig3_yaxis = st.radio("""Stacked Funnel Plot on Editing Practices""", labels_plot3)
        
        if fig3_yaxis == "General Pages":
            fig3_1 = go.Figure()
            fig3_1.add_trace(go.Funnel(
                name='Female',
                x=[df[df["gender"] == 2].median()["NPages"], df[df["gender"] == 2].median()["NPcreated"]],
                y=["Pages", "Pages Created"],
                textinfo="value+percent initial",
                textposition="inside"))
            fig3_1.add_trace(go.Funnel(
                name='Male',
                x=[df[df["gender"] == 1].median()["NPages"], df[df["gender"] == 1].median()["NPcreated"]],
                y=["Pages", "Pages Created"],
                textinfo="value+percent initial",
                textposition="inside"))
            fig3_1.add_trace(go.Funnel(
                name='Unknown',
                x=[df[df["gender"] == 0].median()["NPages"], df[df["gender"] == 0].median()["NPcreated"]],
                y=["Pages", "Pages Created"],
                textinfo="value+percent initial",
                textposition="inside"))
            st.plotly_chart(fig3_1, use_container_width=True)
            st.caption(":point_right: dd")

        elif fig3_yaxis == "Namespaces":
            fig3_2 = go.Figure()
            fig3_2.add_trace(go.Funnel(
                name='Female',
                x=[df[df["gender"] == 2].median()["ns_content"], df[df["gender"] == 2].median()["ns_talk"], df[df["gender"] == 2].median()["ns_wikipedia"]
                    ],
                y=["Content", "Talk", "Wikipedia"],
                textinfo="value+percent initial",
                textposition="inside"))
            fig3_2.add_trace(go.Funnel(
                name='Male',
                x=[df[df["gender"] == 1].median()["ns_content"], df[df["gender"] == 1].median()["ns_talk"], df[df["gender"] == 1].median()["ns_wikipedia"]],
                y=["Content", "Talk", "Wikipedia"],
                textinfo="value+percent initial",
                textposition="inside"))

            fig3_2.add_trace(go.Funnel(
                name='Unknown',
                x=[df[df["gender"] == 0].median()["ns_content"], df[df["gender"] == 0].median()["ns_talk"], df[df["gender"] == 0].median()["ns_wikipedia"]],
                y=["Content", "Talk", "Wikipedia"],
                textinfo="value+percent initial",
                textposition="inside"))
            st.plotly_chart(fig3_2, use_container_width=True)
            
            st.caption(":point_right: dd")

        elif fig3_yaxis == "Pages Related to Women":
            st.write("3) Participation in Pages Related to Gender Issues")

            fig3_3= go.Figure()
            fig3_3.add_trace(go.Funnel(
                name='Female',
                x=[df[df["gender"] == 2].mean()["pagesWomen"], df[df["gender"] == 2].mean()["wikiprojWomen"]],
                y=["Pages", "WikiProjects"], 
                textinfo="value+percent initial"))

            fig3_3.add_trace(go.Funnel(
                name='Male',
                x=[df[df["gender"] == 1].mean()["pagesWomen"], df[df["gender"] == 1].mean()["wikiprojWomen"]],
                y=["Pages", "WikiProjects"], 
                textinfo="value+percent initial",
                textposition="inside"))

            fig3_3.add_trace(go.Funnel(
                name='Unknown',
                x=[df[df["gender"] == 0].mean()["pagesWomen"], df[df["gender"] == 0].mean()["wikiprojWomen"]],
                y=["Pages", "WikiProjects"], 
                textinfo="value+percent initial",
                textposition="inside"))

            st.plotly_chart(fig3_3, use_container_width=True)
            st.caption(":point_right: dd")
            st.caption(":link:https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Women")

        
        
    # ===== PLOT 4: number of different pages (women vs. men) - content 
    with plot4:
        st.subheader(':four:Regression Analysis on Activity vs. Duration')

        # ==== SIDEBAR
        labels = ['# of Pages Edited','# of Pages Created', '# Pages Realted to Women', '# of WikiProject Related Women']
        fig4_yaxis = st.radio("""Regression Plot for Duration vs. Activity""", labels)
        
        y = ""
        if fig4_yaxis == "# of Pages Edited":
            y = "NPages"
        elif fig4_yaxis == "# of Pages Created":
            y = "NPcreated"
        elif fig4_yaxis == "# Pages Realted to Women":
            y = "pagesWomen"
        elif fig4_yaxis == "# of WikiProject Related Women":
            y = "wikiprojWomen"
        fig4 = sns.lmplot(data=df, x="NActDays", y=y, hue="gender", palette="icefire")
        st.pyplot(fig4)

        st.caption(":point_right: dd")
        st.caption("*A Wikipedia namespace is a set of Wikipedia pages whose names begin with a particular reserved word recognized by the MediaWiki software.")

    # ===== SELECT 5 - STREAMLIT SELECTION - Lifespan, % of active days, Edits per active day, % of dropout
    #st.header("Comparison - Activity : Select parameter")
    #activity_options = ['something']
    #activity_selected = st.selectbox("Which parameter would you like to see?")
    # ===== PLOT 5: LINE CHART, BAR CHART - Lifespan, % of active days, Edits per active day
    with plot5:
        st.subheader(":five:")

    with plot6:
        st.subheader(":six: Detail: Gender Difference in Editing Practices")
        hiplot_options = st.multiselect('Select Namespace Activity', ['Content', 'Talk', 'Wikipedia', 'User', 'User Talk'])
        df_hiplot = pd.DataFrame()
        for options in hiplot_options:
            if options == 'Content':
                df_hiplot['Content'] = df['ns_content']
            elif options == 'Talk':
                df_hiplot['Talk'] = df['ns_talk']
            elif options == 'Wikipedia':
                df_hiplot['Wikipedia'] = df['ns_wikipedia']
            elif options == 'User':
                df_hiplot['User'] = df['ns_user']
            elif options == 'User Talk':
                df_hiplot['User Talk'] = df['ns_userTalk']
        df_hiplot['Gender'] = df['gender']        

        hip.Experiment.from_dataframe(df_hiplot).display_st()
        st.caption(":point_right: dd")

if selected == "Contact":
    st.subheader(":open_mouth: For more information:")
    st.write(":open_hands:If you require any further information, please feel free to reach out to me!:open_hands:")
    st.write(":email: chaeyeon.yim95@gmail.com")
    st.write(":email: yimchaey@msu.edu")