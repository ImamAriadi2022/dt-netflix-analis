import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\asus\Downloads\dt-netflix-analis\netflix_titles.csv')

# 1. Jenis film apa yang dimiliki setiap negara
country_genre = df.groupby('country')['listed_in'].apply(lambda x: ', '.join(x.unique())).reset_index()
print("Jenis film yang dimiliki setiap negara:")
print(country_genre)
country_genre.to_csv(r'C:\Users\asus\Downloads\dt-netflix-analis\country_genre.csv', index=False)

# 2. Kelompokkan per negara jenis film yang dimiliki
country_genre_grouped = df.groupby(['country', 'listed_in']).size().reset_index(name='count')
print("\nKelompokkan per negara jenis film yang dimiliki:")
print(country_genre_grouped)
country_genre_grouped.to_csv(r'C:\Users\asus\Downloads\dt-netflix-analis\country_genre_grouped.csv', index=False)

# 3. Analisis aktor yang memiliki kesamaan jenis film yang diperankan
actor_genre = df.dropna(subset=['cast']).copy()
actor_genre['cast'] = actor_genre['cast'].str.split(', ')
actor_genre = actor_genre.explode('cast')
actor_genre_grouped = actor_genre.groupby(['cast', 'listed_in']).size().reset_index(name='count')
print("\nAktor yang memiliki kesamaan jenis film yang diperankan:")
print(actor_genre_grouped)
actor_genre_grouped.to_csv(r'C:\Users\asus\Downloads\dt-netflix-analis\actor_genre_grouped.csv', index=False)

# 4. Kelompokkan jenis dan aktor per tahun
actor_year_genre = df.dropna(subset=['cast']).copy()
actor_year_genre['cast'] = actor_year_genre['cast'].str.split(', ')
actor_year_genre = actor_year_genre.explode('cast')
actor_year_genre_grouped = actor_year_genre.groupby(['release_year', 'listed_in', 'cast']).size().reset_index(name='count')
print("\nKelompokkan jenis dan aktor per tahun:")
print(actor_year_genre_grouped)
actor_year_genre_grouped.to_csv(r'C:\Users\asus\Downloads\dt-netflix-analis\actor_year_genre_grouped.csv', index=False)