import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Instagram Engagement Time Optimizer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM STYLING
# ============================================================================
st.markdown("""
<style>
    .main-header {
        font-size: 3em;
        font-weight: bold;
        text-align: center;
        color: #E1306C;
        margin-bottom: 1rem;
    }
    .subheader-custom {
        font-size: 1.5em;
        color: #405DE6;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .recommendation-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# CACHE DATA LOADING
# ============================================================================
@st.cache_data
def load_data():
    """Load and preprocess Instagram Analytics dataset."""
    data = pd.read_csv('Instagram_Analytics.csv')
    
    # Convert upload_date to datetime
    data['upload_date'] = pd.to_datetime(data['upload_date'])
    
    # Extract temporal features
    data['posting_hour'] = data['upload_date'].dt.hour
    data['day_of_week'] = data['upload_date'].dt.day_name()
    data['month'] = data['upload_date'].dt.month
    data['day_of_week_num'] = data['upload_date'].dt.dayofweek
    
    # Calculate engagement score
    data['engagement_score'] = data['likes'] + data['comments'] + data['shares'] + data['saves']
    
    return data

# ============================================================================
# LOAD DATA
# ============================================================================
try:
    data = load_data()
    data_loaded = True
except FileNotFoundError:
    data_loaded = False
    st.error("❌ Error: Instagram_Analytics.csv not found. Please ensure the CSV file is in the same directory as this app.")

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================
st.sidebar.markdown("---")
st.sidebar.markdown("### 📱 Navigation")
page = st.sidebar.radio(
    "Select a Section:",
    [
        "🏠 Homepage",
        "📊 Dataset Overview",
        "📈 Engagement Analysis",
        "🔥 Engagement Heatmap",
        "🎯 Recommendation Tool",
        "ℹ️ About"
    ]
)
st.sidebar.markdown("---")

# ============================================================================
# PAGE 1: HOMEPAGE
# ============================================================================
if page == "🏠 Homepage":
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<p class="main-header">📊 Instagram Engagement<br>Time Optimizer</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 What is This?")
        st.write("""
        The **Instagram Engagement Time Optimizer** is a data-driven analytics tool 
        designed to help content creators and businesses maximize their Instagram engagement.
        
        By analyzing historical engagement patterns across different posting times, 
        content types, and categories, this tool identifies the optimal times to post 
        for maximum reach and engagement.
        """)
    
    with col2:
        st.markdown("### 🚀 Key Benefits")
        st.write("""
        ✅ **Maximize Engagement** – Post at times when your audience is most active
        
        ✅ **Optimize Content** – Understand which content types perform best
        
        ✅ **Data-Driven Decisions** – Base your strategy on real engagement data
        
        ✅ **Category & Type Filters** – Get recommendations tailored to your niche
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 How It Works")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-container">
            <h4 style="color: #E1306C;">📥 Load Data</h4>
            <p>Analyze 30,000+ Instagram posts</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-container">
            <h4 style="color: #405DE6;">🔍 Process</h4>
            <p>Extract timing and engagement metrics</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-container">
            <h4 style="color: #5B51D8;">📊 Analyze</h4>
            <p>Visualize engagement patterns</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-container">
            <h4 style="color: #833AB4;">🎯 Recommend</h4>
            <p>Get personalized posting recommendations</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🌟 Start Your Analysis")
    st.write("Navigate using the sidebar to explore different sections and get personalized recommendations!")

# ============================================================================
# PAGE 2: DATASET OVERVIEW
# ============================================================================
elif page == "📊 Dataset Overview":
    st.markdown("## 📊 Dataset Overview")
    st.markdown("---")
    
    if data_loaded:
        # Dataset Statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Posts", f"{len(data):,}")
        
        with col2:
            st.metric("Date Range Days", (data['upload_date'].max() - data['upload_date'].min()).days)
        
        with col3:
            st.metric("Content Categories", data['content_category'].nunique())
        
        with col4:
            st.metric("Media Types", data['media_type'].nunique())
        
        st.markdown("---")
        
        # Data Preview
        st.markdown("### 👀 Data Sample")
        st.dataframe(data.head(10), use_container_width=True)
        
        st.markdown("---")
        
        # Column Information
        st.markdown("### 📋 Column Descriptions")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("""
            **Post Information:**
            - `post_id` – Unique post identifier
            - `upload_date` – When the post was published
            - `media_type` – Type of content (Reel, Photo, Video, Carousel)
            - `content_category` – Category (Technology, Beauty, Fitness, etc.)
            
            **Engagement Metrics:**
            - `likes` – Number of likes
            - `comments` – Number of comments
            - `shares` – Number of shares
            - `saves` – Number of saves
            - `engagement_score` – Sum of all engagement metrics
            """)
        
        with col2:
            st.write("""
            **Reach Metrics:**
            - `reach` – Unique accounts reached
            - `impressions` – Total content views
            - `engagement_rate` – Engagement rate (%)
            
            **Content Features:**
            - `caption_length` – Number of characters in caption
            - `hashtags_count` – Number of hashtags used
            - `followers_gained` – New followers from post
            - `traffic_source` – Where clicks came from
            """)
        
        st.markdown("---")
        
        # Data Types
        st.markdown("### 🔍 Data Structure")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**Numeric Columns:**")
            numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
            for col in numeric_cols[:5]:
                st.write(f"• {col}")
        
        with col2:
            st.write("**String Columns:**")
            str_cols = data.select_dtypes(include='object').columns.tolist()
            for col in str_cols[:5]:
                st.write(f"• {col}")
        
        with col3:
            st.write("**Datetime Columns:**")
            st.write("• upload_date")
            st.write("• posting_hour (extracted)")
            st.write("• day_of_week (extracted)")
        
        st.markdown("---")
        
        # Summary Statistics
        st.markdown("### 📊 Summary Statistics")
        st.dataframe(data.describe(), use_container_width=True)
    
    else:
        st.error("Please load the dataset first.")

# ============================================================================
# PAGE 3: ENGAGEMENT ANALYSIS
# ============================================================================
elif page == "📈 Engagement Analysis":
    st.markdown("## 📈 Engagement Analysis Dashboard")
    st.markdown("---")
    
    if data_loaded:
        # Configure visualization style
        plt.style.use('seaborn-v0_8-darkgrid')
        sns.set_palette("husl")
        
        # 1. Average Engagement by Posting Hour
        st.markdown("### 1️⃣ Average Engagement by Posting Hour")
        
        hourly_engagement = data.groupby('posting_hour')['engagement_score'].agg(['mean', 'count']).reset_index()
        hourly_engagement.columns = ['Hour', 'Avg_Engagement', 'Post_Count']
        
        fig, ax = plt.subplots(figsize=(14, 5))
        colors = plt.cm.viridis(hourly_engagement['Avg_Engagement'] / hourly_engagement['Avg_Engagement'].max())
        bars = ax.bar(hourly_engagement['Hour'], hourly_engagement['Avg_Engagement'], color=colors, edgecolor='black', linewidth=0.7)
        ax.set_xlabel('Posting Hour (24-hour format)', fontsize=11, fontweight='bold')
        ax.set_ylabel('Average Engagement Score', fontsize=11, fontweight='bold')
        ax.set_title('Best Times to Post Throughout the Day', fontsize=12, fontweight='bold')
        ax.set_xticks(range(0, 24))
        ax.grid(True, alpha=0.3, axis='y')
        st.pyplot(fig)
        
        st.markdown("---")
        
        # 2. Average Engagement by Day of Week
        st.markdown("### 2️⃣ Average Engagement by Day of Week")
        
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        daily_engagement = data.groupby('day_of_week')['engagement_score'].agg(['mean', 'count']).reset_index()
        daily_engagement.columns = ['Day', 'Avg_Engagement', 'Post_Count']
        daily_engagement['Day'] = pd.Categorical(daily_engagement['Day'], categories=day_order, ordered=True)
        daily_engagement = daily_engagement.sort_values('Day')
        
        fig, ax = plt.subplots(figsize=(12, 5))
        colors = plt.cm.Set2(np.linspace(0, 1, len(daily_engagement)))
        bars = ax.bar(range(len(daily_engagement)), daily_engagement['Avg_Engagement'], color=colors, edgecolor='black', linewidth=0.7)
        ax.set_xlabel('Day of Week', fontsize=11, fontweight='bold')
        ax.set_ylabel('Average Engagement Score', fontsize=11, fontweight='bold')
        ax.set_title('Best Days for Posting', fontsize=12, fontweight='bold')
        ax.set_xticks(range(len(daily_engagement)))
        ax.set_xticklabels(daily_engagement['Day'], rotation=45, ha='right')
        ax.grid(True, alpha=0.3, axis='y')
        st.pyplot(fig)
        
        st.markdown("---")
        
        # 3. Engagement Distribution
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 3️⃣ Engagement Distribution (Histogram)")
            fig, ax = plt.subplots(figsize=(11, 5))
            ax.hist(data['engagement_score'], bins=50, color='skyblue', edgecolor='black', alpha=0.7)
            ax.axvline(data['engagement_score'].mean(), color='red', linestyle='--', linewidth=2, label=f"Mean: {data['engagement_score'].mean():.0f}")
            ax.axvline(data['engagement_score'].median(), color='green', linestyle='--', linewidth=2, label=f"Median: {data['engagement_score'].median():.0f}")
            ax.set_xlabel('Engagement Score', fontsize=10, fontweight='bold')
            ax.set_ylabel('Frequency', fontsize=10, fontweight='bold')
            ax.legend()
            ax.grid(True, alpha=0.3, axis='y')
            st.pyplot(fig)
        
        with col2:
            st.markdown("### 3️⃣ Engagement Distribution (Box Plot)")
            fig, ax = plt.subplots(figsize=(11, 5))
            bp = ax.boxplot(data['engagement_score'], vert=True, patch_artist=True)
            bp['boxes'][0].set_facecolor('lightblue')
            bp['boxes'][0].set_edgecolor('black')
            bp['boxes'][0].set_linewidth(1.5)
            ax.set_ylabel('Engagement Score', fontsize=10, fontweight='bold')
            ax.set_title('Engagement Score Distribution', fontsize=11, fontweight='bold')
            ax.grid(True, alpha=0.3, axis='y')
            st.pyplot(fig)
        
        st.markdown("---")
        
        # 4. Engagement by Content Category
        st.markdown("### 4️⃣ Engagement by Content Category")
        
        category_engagement = data.groupby('content_category')['engagement_score'].agg(['mean', 'count']).reset_index()
        category_engagement.columns = ['Category', 'Avg_Engagement', 'Post_Count']
        category_engagement = category_engagement.sort_values('Avg_Engagement', ascending=False)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        colors = plt.cm.RdYlGn(np.linspace(0.3, 0.9, len(category_engagement)))
        bars = ax.barh(category_engagement['Category'], category_engagement['Avg_Engagement'], color=colors, edgecolor='black', linewidth=0.7)
        ax.set_xlabel('Average Engagement Score', fontsize=11, fontweight='bold')
        ax.set_title('Which Content Categories Perform Best?', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='x')
        st.pyplot(fig)
        
        st.markdown("---")
        
        # 5. Engagement vs Hashtag Count
        st.markdown("### 5️⃣ Engagement vs Hashtag Count")
        
        fig, ax = plt.subplots(figsize=(12, 5))
        scatter = ax.scatter(data['hashtags_count'], data['engagement_score'], alpha=0.3, s=20, c=data['posting_hour'], cmap='twilight')
        
        # Add trend line
        z = np.polyfit(data['hashtags_count'], data['engagement_score'], 2)
        p = np.poly1d(z)
        x_trend = np.linspace(data['hashtags_count'].min(), data['hashtags_count'].max(), 100)
        ax.plot(x_trend, p(x_trend), "r--", linewidth=2.5, label='Trend')
        
        ax.set_xlabel('Hashtag Count', fontsize=11, fontweight='bold')
        ax.set_ylabel('Engagement Score', fontsize=11, fontweight='bold')
        ax.set_title('Does Using More Hashtags Increase Engagement?', fontsize=12, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Posting Hour', fontweight='bold')
        st.pyplot(fig)
        
        # Correlation info
        hashtag_corr = data['hashtags_count'].corr(data['engagement_score'])
        if hashtag_corr > 0:
            st.success(f"✅ **Positive correlation ({hashtag_corr:.3f})**: More hashtags tend to increase engagement!")
        else:
            st.info(f"ℹ️ **Negative correlation ({hashtag_corr:.3f})**: Use fewer, more targeted hashtags for better engagement.")
    
    else:
        st.error("Please load the dataset first.")

# ============================================================================
# PAGE 4: ENGAGEMENT HEATMAP
# ============================================================================
elif page == "🔥 Engagement Heatmap":
    st.markdown("## 🔥 Engagement Heatmap: Hour × Day Analysis")
    st.markdown("---")
    
    if data_loaded:
        # Create pivot table
        day_hour_engagement = data.pivot_table(
            values='engagement_score',
            index='posting_hour',
            columns='day_of_week_num',
            aggfunc='mean'
        )
        
        # Reorder columns
        day_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_hour_engagement.columns = [day_labels[i] for i in day_hour_engagement.columns]
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=(14, 10))
        sns.heatmap(
            day_hour_engagement,
            annot=True,
            fmt='.0f',
            cmap='YlOrRd',
            cbar_kws={'label': 'Average Engagement Score'},
            linewidths=0.5,
            linecolor='gray',
            ax=ax
        )
        ax.set_title('Engagement Patterns: Best Times to Post', fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel('Day of Week', fontsize=12, fontweight='bold')
        ax.set_ylabel('Posting Hour (24-hour format)', fontsize=12, fontweight='bold')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)
        
        st.markdown("---")
        
        # Top Combinations
        st.markdown("### 🏆 Top 10 Posting Time Combinations")
        
        heatmap_flat = day_hour_engagement.stack().reset_index()
        heatmap_flat.columns = ['Hour', 'Day', 'Avg_Engagement']
        heatmap_flat = heatmap_flat.sort_values('Avg_Engagement', ascending=False).head(10)
        heatmap_flat['Posting Time'] = heatmap_flat['Hour'].astype(str) + ':00 on ' + heatmap_flat['Day']
        heatmap_flat['Avg Engagement'] = heatmap_flat['Avg_Engagement'].astype(int)
        
        st.dataframe(
            heatmap_flat[['Posting Time', 'Avg Engagement']].reset_index(drop=True),
            use_container_width=True
        )
        
        st.markdown("---")
        
        # Insights
        st.markdown("### 💡 Heatmap Insights")
        col1, col2, col3 = st.columns(3)
        
        best_time = heatmap_flat.iloc[0]
        worst_time = heatmap_flat.iloc[-1]
        
        with col1:
            st.markdown("""
            <div class="metric-container">
                <h4>🎯 Best Time</h4>
                <p>{}</p>
                <p style="color: green; font-weight: bold;">{:.0f} engagement</p>
            </div>
            """.format(best_time['Posting Time'], best_time['Avg_Engagement']), unsafe_allow_html=True)
        
        with col2:
            avg_engagement = heatmap_flat['Avg_Engagement'].mean()
            st.markdown(f"""
            <div class="metric-container">
                <h4>📊 Average</h4>
                <p>Across all times</p>
                <p style="color: #405DE6; font-weight: bold;">{avg_engagement:.0f} engagement</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-container">
                <h4>⚠️ Lowest Time</h4>
                <p>{}</p>
                <p style="color: red; font-weight: bold;">{:.0f} engagement</p>
            </div>
            """.format(worst_time['Posting Time'], worst_time['Avg_Engagement']), unsafe_allow_html=True)
    
    else:
        st.error("Please load the dataset first.")

# ============================================================================
# PAGE 5: RECOMMENDATION TOOL
# ============================================================================
elif page == "🎯 Recommendation Tool":
    st.markdown("## 🎯 Get Your Personalized Recommendations")
    st.markdown("---")
    
    if data_loaded:
        # Add filters in sidebar
        st.sidebar.markdown("### 🎛️ Filter Options")
        
        st.sidebar.write("**Select filters to customize your recommendations:**")
        
        # Category filter
        all_categories = ['All Categories'] + sorted(data['content_category'].unique().tolist())
        selected_category = st.sidebar.selectbox(
            "📁 Content Category:",
            all_categories,
            help="Choose a specific content category or 'All Categories' for overall recommendations"
        )
        
        # Media type filter
        all_media_types = ['All Media Types'] + sorted(data['media_type'].unique().tolist())
        selected_media = st.sidebar.selectbox(
            "📱 Media Type:",
            all_media_types,
            help="Choose Reel, Photo, Video, Carousel, or all types"
        )
        
        st.sidebar.markdown("---")
        
        # Filter data
        filtered_data = data.copy()
        
        if selected_category != 'All Categories':
            filtered_data = filtered_data[filtered_data['content_category'] == selected_category]
        
        if selected_media != 'All Media Types':
            filtered_data = filtered_data[filtered_data['media_type'] == selected_media]
        
        # Display filters applied
        st.markdown("### 📋 Applied Filters")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if selected_category == 'All Categories':
                st.metric("Category Filter", "All Categories", "-")
            else:
                st.metric("Category Filter", selected_category, "Applied")
        
        with col2:
            if selected_media == 'All Media Types':
                st.metric("Media Type Filter", "All Types", "-")
            else:
                st.metric("Media Type Filter", selected_media, "Applied")
        
        with col3:
            st.metric("Data Points Analyzed", f"{len(filtered_data):,}", f"out of {len(data):,}")
        
        st.markdown("---")
        
        # Calculate recommendations
        if len(filtered_data) > 0:
            # Best hour
            hourly_avg = filtered_data.groupby('posting_hour')['engagement_score'].mean()
            best_hour = hourly_avg.idxmax()
            best_hour_score = hourly_avg.max()
            
            # Best day
            daily_avg = filtered_data.groupby('day_of_week')['engagement_score'].mean()
            best_day = daily_avg.idxmax()
            best_day_score = daily_avg.max()
            
            # Top 3 hours
            top_3_hours = hourly_avg.nlargest(3)
            
            # Top 3 days
            top_3_days = daily_avg.nlargest(3)
            
            # Display Results
            st.markdown("### 🏆 Your Personalized Recommendations")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                <div class="recommendation-box">
                    <h3>⏰ Best Posting Hour</h3>
                    <h2>{best_hour}:00</h2>
                    <p style="font-size: 1.1em;">Avg Engagement: <strong>{best_hour_score:,.0f}</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="recommendation-box">
                    <h3>📅 Best Posting Day</h3>
                    <h2>{best_day}</h2>
                    <p style="font-size: 1.1em;">Avg Engagement: <strong>{best_day_score:,.0f}</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Top 3 Posting Hours
            st.markdown("### ⭐ Top 3 Recommended Posting Hours")
            col1, col2, col3 = st.columns(3)
            
            for idx, (hour, engagement) in enumerate(top_3_hours.items()):
                with [col1, col2, col3][idx]:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                color: white; padding: 1.5rem; border-radius: 0.5rem; 
                                text-align: center; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                        <p style="font-size: 0.9em; margin: 0;">#{idx+1} Recommended</p>
                        <h3 style="margin: 0.5rem 0;">{hour}:00</h3>
                        <p style="margin: 0;">Engagement: {engagement:,.0f}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Top 3 Posting Days
            st.markdown("### ⭐ Top 3 Recommended Posting Days")
            
            days_data = []
            for idx, (day, engagement) in enumerate(top_3_days.items()):
                days_data.append({
                    'Rank': f"#{idx+1}",
                    'Day': day,
                    'Average Engagement': f"{engagement:,.0f}"
                })
            
            st.dataframe(pd.DataFrame(days_data), use_container_width=True, hide_index=True)
            
            st.markdown("---")
            
            # Additional Insights
            st.markdown("### 📊 Additional Insights")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                avg_engagement = filtered_data['engagement_score'].mean()
                st.metric("Avg Engagement", f"{avg_engagement:,.0f}")
            
            with col2:
                max_engagement = filtered_data['engagement_score'].max()
                st.metric("Max Engagement", f"{max_engagement:,.0f}")
            
            with col3:
                min_engagement = filtered_data['engagement_score'].min()
                st.metric("Min Engagement", f"{min_engagement:,.0f}")
            
            with col4:
                std_engagement = filtered_data['engagement_score'].std()
                st.metric("Std Deviation", f"{std_engagement:,.0f}")
            
            st.markdown("---")
            
            # Action Items
            st.markdown("### 🎯 Action Items")
            st.write(f"""
            Based on the analysis of {len(filtered_data):,} posts:
            
            1. **Schedule Posts at {best_hour}:00** on {best_day} for maximum reach
            2. **Avoid posting at {hourly_avg.idxmin()}:00** when engagement is lowest
            3. **Plan your content calendar** around peak days: {', '.join(top_3_days.index.tolist())}
            4. **Test and iterate** - Monitor your engagement and adjust accordingly
            5. **Consistency matters** - Maintain a regular posting schedule
            """)
        
        else:
            st.warning("❌ No data found for the selected filters. Please adjust your selections.")
    
    else:
        st.error("Please load the dataset first.")

# ============================================================================
# PAGE 6: ABOUT
# ============================================================================
elif page == "ℹ️ About":
    st.markdown("## ℹ️ About This Application")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📖 Project Overview")
        st.write("""
        The **Instagram Engagement Time Optimizer** is a comprehensive analytics tool 
        designed to help content creators and Instagram marketers make data-driven 
        decisions about their posting strategy.
        
        **Key Capabilities:**
        - Analyze 30,000+ Instagram posts
        - Identify optimal posting times (hour & day)
        - Compare performance across content types
        - Filter by category and media type
        - Get personalized recommendations
        """)
    
    with col2:
        st.markdown("### 🛠️ Technology Stack")
        st.write("""
        **Frontend:**
        - Streamlit for interactive web interface
        
        **Data Analysis:**
        - Pandas for data manipulation
        - NumPy for numerical operations
        
        **Visualization:**
        - Matplotlib for charts
        - Seaborn for statistical visualization
        
        **Deployment:**
        - Streamlit Community Cloud
        - Render
        - HuggingFace Spaces
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Dataset Information")
    if data_loaded:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Posts", f"{len(data):,}")
        with col2:
            st.metric("Date Range", f"{(data['upload_date'].max() - data['upload_date'].min()).days} days")
        with col3:
            st.metric("Categories", data['content_category'].nunique())
        
        st.markdown("**Data Features:**")
        st.write(f"""
        - **Engagement Metrics:** Likes, Comments, Shares, Saves
        - **Reach Metrics:** Impressions, Reach, Engagement Rate
        - **Content Data:** Caption length, Hashtag count, Media type
        - **Temporal Data:** Upload date, Hour, Day of week, Month
        """)
    
    st.markdown("---")
    
    st.markdown("### 🚀 How to Deploy")
    st.write("""
    **Streamlit Community Cloud:**
    1. Push your repository to GitHub
    2. Sign up at https://streamlit.io/cloud
    3. Connect your GitHub repo
    4. Click "Deploy"
    
    **Render:**
    1. Push your repository to GitHub
    2. Create a new Web Service on Render
    3. Use this build command: `pip install -r requirements.txt`
    4. Use this start command: `streamlit run app.py`
    
    **HuggingFace Spaces:**
    1. Create a new Space
    2. Select Streamlit as the SDK
    3. Upload your files
    4. The app will deploy automatically
    """)
    
    st.markdown("---")
    
    st.markdown("### 📝 Requirements")
    st.write("""
    - Python 3.8+
    - pandas
    - numpy
    - matplotlib
    - seaborn
    - streamlit
    
    See `requirements.txt` for exact versions.
    """)
    
    st.markdown("---")
    
    st.markdown("### 👨‍💻 Author")
    st.write("Created for Instagram content creators and digital marketers")
    st.write("March 2026")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.85em;">
    <p>📊 Instagram Engagement Time Optimizer | Powered by Streamlit</p>
    <p>Data-driven insights for Instagram success 🚀</p>
</div>
""", unsafe_allow_html=True)
