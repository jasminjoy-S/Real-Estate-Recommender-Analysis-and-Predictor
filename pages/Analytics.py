import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

st.set_page_config(page_title="Analytics")
st.title('Analytics')

new_df = pd.read_csv('datasets/data_for_viz.csv')
feature_text = pickle.load(open('datasets/feature_text_for_wordcloud.pkl','rb'))

# viz 1 : scatter_mapbox
group_df = new_df.groupby('sector').mean(numeric_only=True)[['price','price_per_sqft','built_up_area','latitude','longitude']]
st.header('Geomap showing Sector wise Price Per Sqft')
fig = px.scatter_mapbox(group_df,lat='latitude', lon='longitude',
                        size='built_up_area', color='price_per_sqft',
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                        mapbox_style="open-street-map",text=group_df.index)
st.plotly_chart(fig,use_container_width=True)

#viz2 : wordcloud
st.header('Wordcloud of Features')
# add a dropdown for sector and show the wordcloud of selected sector
wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig = plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)

#viz 3: scatter plot
st.header("Area vs Price")

property_type = st.selectbox('Select property type : ',['flat','house'])
if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type']=='house'],x='built_up_area',y='price',color='bedRoom',title='Area vs Price')
    st.plotly_chart(fig1,use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type']=='flat'],x='built_up_area',y='price',color='bedRoom',title='Area vs Price')
    st.plotly_chart(fig1,use_container_width=True)

#viz 4 : Bedroom pie chart
st.header('Pie chart - Bedrooms')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,"overall")

selected_sector = st.selectbox('Select sector', sector_options)
if selected_sector == "overall":
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig2,use_container_width=True)

# viz 4 : Price range
st.header('Side by Side comparison of BHK')
st.markdown("The boxplot showcases the price range of 1,2,3 and 4 BHK flat/house")
fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom',y='price',title='BHK Price Range')
st.plotly_chart(fig3,use_container_width=True)

#viz 5 : Hist plot for property type
st.header('Histogram of Property Type')
fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)