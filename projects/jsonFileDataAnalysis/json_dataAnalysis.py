import pandas as pd
import matplotlib.pyplot as plt
import json
from pandas.io.json import json_normalize
import pandasql as ps
pysql = lambda q: ps.sqldf(q, globals())


# Loading data 
df = pd.read_json('data/world_bank_projects.json')
print(df.columns)
print(df['countryshortname'][:10])
print(df.shape)

# 1: Find the 10 countries with most projects

set_countries = df['countryshortname'].unique()
print(set_countries.shape)
print(df.shape)

df_CountriesWithMostProjects = df[['countryshortname', 'project_name']].groupby(['countryshortname'], as_index=False).count().sort_values(by='project_name', ascending=False)
df_CountriesWithMostProjects.rename(columns = {'project_name':'NumOfProjects'}, inplace = True)

print("Top 10 countries with most projects:")
print(df_CountriesWithMostProjects[:10])

plt.bar(df_CountriesWithMostProjects['countryshortname'][:10], df_CountriesWithMostProjects['NumOfProjects'][:10])
plt.title("Top 10 countries with most projects with World Bank")
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig('Figure_Plot1_topTenCountries.jpg')

# 2: Find the top 10 major project themes (using column 'mjtheme_namecode')

dict_themes = {}

for row in df:
    major_project_themes = df['mjtheme_namecode']
    for list_of_themes in major_project_themes:
        for themeitem in list_of_themes:
            key = themeitem['code']
            name = themeitem['name']
            
            if key in dict_themes:
                dict_themes[key]['count']+=1
                if dict_themes[key]['name'] == '':
                    dict_themes[key]['name'] = name
            else:
                dict_themes[key]= {'count':1, 'name':name} 

print(dict_themes)  


df_majorThemes = pd.DataFrame.from_dict(dict_themes, orient='index').sort_values(by=['count'], ascending=False)

print('\nTop 10 Major Project Themes:\n')
print(df_majorThemes[:10])

plt.clf()
plt.bar(df_majorThemes['name'][:10], df_majorThemes['count'][:10])
plt.title("Top 10 Major Project Themes")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('Figure_Plot2_topTenMajorProjectThemes.jpg')

plt.clf()
plt.bar(df_majorThemes['name'], df_majorThemes['count'])
plt.title("All Major Project Themes")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('Figure_Plot3_bar_allMajorProjectThemes.jpg')

plt.clf()
fig = plt.figure(figsize=(11,11))
plt.pie(df_majorThemes['count'], labels=df_majorThemes['name'])
plt.title("All Major Project Themes")
plt.tight_layout()
plt.savefig('Figure_Plot4_pie_allMajorProjectThemes.jpg')

#3 Creating new dataframe with the missing names in df filled in for major project themes (column 'mjtheme_namecode')

df_namesFilled = pd.DataFrame()
df_namesFilled = df.copy(deep=True)

for list_of_themes in df_namesFilled['mjtheme_namecode']:
    for themeitem in list_of_themes:
        key = themeitem['code']

        if themeitem['name'] == '':
            themeitem['name'] = dict_themes[key]['name']


# Testing whether dataframe properly filled
for list_of_themes in df_namesFilled['mjtheme_namecode'][:5]:
    print(list_of_themes)
    
print("\nOriginal dataframe:\n")
for list_of_themes in df['mjtheme_namecode'][:5]:
    print(list_of_themes)

