from urllib.request import urlretrieve

urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw'
            '/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv', 'italy-covid-daywise.csv')

# for Merging.py file
urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw'
            '/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv',
            'locations.csv')
