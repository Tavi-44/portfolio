import streamlit as st


page = st.sidebar.radio(
    "Navigation",
    ["Home","About Me","Projects","Contact"]
)
if page == "Home":
    st.title("Tanmay Virkar - Data Analyst")
    st.subheader("@tavi.likes.to.code")
    st.image("portfolio.png", use_container_width=True)

elif page == "About Me":
    st.title('About Me')
    st.write('Hi, I am Tanmay, a beginner Data Analyst passionate about Python and data visualization. I have experience in python and I can easily work with data using some popular liberies of python like Pandas,Numpy,Matplotlib,Seaborn,Plotly,and i can create interactive dashboards using streamlit. I have completed 10+ CSV data cleaning projects and created interective dashboards to help visualize insights for better decision making. I focus on accuracy, timely delivery, and clear communication to ensure client satisfaction Feel free to message me to discuss your data projects — I am ready to start immediately!')
    st.write("Completed 10th grade and currently looking for result and self learning python")

elif page == "Projects":
    st.title('My Projects')
    tab1, tab2 = st.tabs(["🎬 Netflix Analysis", "🌱 Crop Recommendation"])

    with tab1:
        st.subheader("Netflix Data Visualization")
        st.write("Netflix dataset ka use karke trends aur content distribution analyze kiya hai.")
        
    
        st.image("netflix.png", caption="Netflix Dashboard Overview", use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image("netflix (2).png", use_container_width=True)
        with col2:
            st.image("netflix (3).png", use_container_width=True)
            
        st.image("netflix (4).png", caption="Content Insights", use_container_width=True)

    with tab2:
        st.subheader("Crop Recommendation System")
        st.write("Data cleaning aur visualization ke zariye sahi crop suggest karne ka model.")
        
        st.image("crop.png", caption="Data Exploration", use_container_width=True)
        
        col3, col4 = st.columns(2)
        with col3:
            st.image("crop (2).png", use_container_width=True)
        with col4:
            st.image("crop (3).png", use_container_width=True)

    st.divider()
    st.link_button("View Source Code on GitHub", "https://github.com/Tavi-44/Data-analysis-projects.git")

elif page == "Contact":
    st.title("My Contact")
    st.subheader("Instagram: tavi.likes.to.code")
    st.subheader('Phone Number: 9630982626')
    st.subheader('Github: https://github.com/Tavi-44/Data-analysis-projects.git')
    