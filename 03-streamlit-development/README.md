# Streamlit Development Learning Path

Build interactive web applications for data visualization and AI model deployment with minimal code.

## Learning Progression

### 📍 Level 1: Fundamentals (Week 1)
- Streamlit Basics
- Layout and Components
- Data Display (Tables, Charts)
- User Input (Widgets)
- Running and Deploying Apps

### 📍 Level 2: Intermediate (Week 2-3)
- State Management
- Caching and Performance
- Custom Styling and Theming
- File Upload and Processing
- Multiple Pages (Multipage Apps)

### 📍 Level 3: Advanced (Week 3-4)
- Session State Deep Dive
- Custom Components
- Authentication & Authorization
- Database Integration
- Production Deployment Strategies

## 📚 Topics Covered

### Fundamentals
1. **Getting Started**
   - Installation and setup
   - Your first app
   - Running with `streamlit run`
   - Understanding the execution model

2. **Core Components**
   - Text elements (title, header, subheader, write)
   - Input widgets (button, text_input, slider, selectbox)
   - Data display (dataframe, table, metric, chart)
   - Columns and containers

3. **Data Visualization**
   - st.line_chart, st.bar_chart
   - st.area_chart, st.scatter_chart
   - Plotly integration
   - Altair charts
   - Map visualization

### Intermediate
4. **Advanced Widgets**
   - File uploaders
   - Date and time pickers
   - Multiselect
   - Radio buttons
   - Checkboxes
   - Forms

5. **State Management**
   - Session state basics
   - Handling form state
   - Persisting data across reruns
   - Callback functions

6. **Performance**
   - @st.cache_data decorator
   - @st.cache_resource decorator
   - When and how to use caching
   - Avoiding common pitfalls

7. **Multi-page Apps**
   - Pages directory structure
   - Navigation between pages
   - Shared state across pages
   - Page configuration

### Advanced
8. **Custom Styling**
   - Markdown and HTML
   - CSS styling
   - Custom themes
   - st.set_page_config options

9. **Database Integration**
   - SQLite integration
   - PostgreSQL connection
   - Query caching
   - Data persistence

10. **Deployment**
    - Streamlit Cloud
    - Docker containerization
    - AWS/GCP/Azure deployment
    - Environment variables and secrets

## 🎓 Projects

### Project 1: Simple Data Explorer
**Level:** Beginner  
**Skills:** File upload, data display, basic filtering  
Upload CSV files and explore with interactive visualizations.

### Project 2: Stock Price Dashboard
**Level:** Intermediate  
**Skills:** APIs, caching, multiple visualizations, state  
Fetch and visualize stock prices with real-time updates.

### Project 3: ML Model Interface
**Level:** Intermediate-Advanced  
**Skills:** Model loading, predictions, form handling  
Create an interface for your trained ML models.

### Project 4: Multi-page Analytics App
**Level:** Advanced  
**Skills:** Multiple pages, database, authentication  
Build a complete analytics platform with different views.

### Project 5: Real-time Monitoring Dashboard
**Level:** Advanced  
**Skills:** Streaming data, live updates, WebSocket handling  
Monitor system metrics or data streams in real-time.

## 💻 Tech Stack

### Core
- **Streamlit** - Web framework
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Plotly/Altair** - Advanced visualization

### Extensions
- **Streamlit-authenticator** - Authentication
- **st_pages** - Enhanced multipage support
- **streamlit-aggrid** - Interactive tables
- **Streamlit Components** - Custom components

### Data & Databases
- **SQLAlchemy** - ORM and database toolkit
- **SQLite** - Embedded database
- **PostgreSQL** - Production database

## 💡 Learning Tips

1. **Build as you learn** - Create small projects immediately
2. **Focus on the data story** - Good visualization > flashy design
3. **Master state management** - It's key to interactive apps
4. **Cache wisely** - Understand what should be cached
5. **Test locally first** - Always test before deploying
6. **Use multipage apps** - Organize complex applications

## 📖 Resources

### Documentation
- [Streamlit Official Docs](https://docs.streamlit.io/)
- [Streamlit Components](https://streamlit.io/components)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

### Galleries & Examples
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Community Cloud Examples](https://discuss.streamlit.io/)
- [Awesome Streamlit](https://github.com/MarcSkovMadsen/awesome-streamlit)

### Tutorials
- [Streamlit University](https://discuss.streamlit.io/t/streamlit-university/)
- [Create Web Apps with Streamlit](https://www.datacamp.com/courses/create-web-apps-with-streamlit)

### Deployment
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud/)
- [Docker Deployment Guide](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)

## 🚀 Next Steps

After completing this path:
1. Combine with **Advanced SQL** for data pipelines
2. Integrate **AI Models** for predictions and analysis
3. Build complete systems in **Integrated Projects**

---

**Ready to start?** Navigate to `fundamentals/` and build your first Streamlit app!
