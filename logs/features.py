import requests

url = "https://api.spotify.com/v1/audio-features/3C5in0EVdoGepp5bA6lhlE"

headers = {
    'accept': "application/json",
    'authorization': "Bearer BQDvvO52nQOfH659LD542SDfVIwSlz52VAmbi8s0cbtrw8YbnSBjzTlhKdy7auzfH0q9sWVLBoAsFAVuBu2_1HipOs3gnv_3OQOGKOzJvtgSCnB9PyGIg8swoliTrwNRr_fPAvzu4IxL_M-16nAjyHQmckSlrdSAn8IHiDzNyDumoCNFywccI0EoF5plfdfMhDP62WriJvJgNT7pgh59skYsS8MbIuEygo561XwlNl3KYXX0NH7iEMghStCjzY15JPLT_Pvy4ARj7MXtZ68q-8N-HZhN4wISIaSOVNjt8Us14S_UBDVEINAnOGXZ_kOKA6c3cW44jmvR",
    'cache-control': "no-cache",
    'postman-token': "e939f3ee-77d6-ac3d-33d8-8fa55f2b3848"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)