# List in dictionary 

my_books = {
    'English': ['The giver','Inferno','Focus'],
    'Arabic': ['Tabari','Kathin','Gabarti']
}

# print(my_books)

# Nested dictionary

all_books = {
    'Arabic':{
        'Novel':{
        'Hanan Lashin': ['Ekadoly','Amanos'],
        'Amr A.hamed': ['Zeekola','Jartin'],
        'Hassan Gendy': ['Ebtasim','Mamsoos'],
        'Ahmed Morad': ['Ard','Azrak'],
        },

        'History': {
            'Ibn Khaldun': ['Al-Muqaddimah','Kitāb al-ʿIbar','Al-Tariff bi Ibn Khaldun'],
            'Al-Tabari': ['Tārīkh al-Rusul wa al-Mulūk','Tahdhīb al-Āthār','Al-Muntakhab min Dhayl al-Mudhayyal'],
            'Al-Maqrizi': ['Al-Mawāʿiẓ wa al-Iʿtibār','Al-Sulūk li-Maʿrifat Duwal al-Mulūk','Ighāthat al-Umma'],
        }
    }
}

print(all_books)