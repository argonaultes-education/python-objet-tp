import requests

response = requests.get('https://data.education.gouv.fr/api/v2/catalog/datasets?limit=10&offset=0&timezone=UTC')

print(response)