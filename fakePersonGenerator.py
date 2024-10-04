import requests
import countryCodeDecoder # type: ignore

randomUserUrl = 'https://randomuser.me/api/'
genderUrl = 'https://api.genderize.io/?name='
ethnicityUrl = 'https://api.nationalize.io/?name='

def getRandomNames() -> dict:
    response = requests.get(randomUserUrl)
    randomUserData = response.json()
    return randomUserData['results'][0]["name"]

def appendNameToUrl(url: str, name: str) -> str:
    url += name
    return url

def guessGender(firstName: str) -> str:
    url = appendNameToUrl(genderUrl, firstName)
    response = requests.get(url)
    genderGuessData = response.json()
    return genderGuessData['gender']

def guessEthnicity(lastName: str) -> str:
    url = appendNameToUrl(ethnicityUrl, lastName)
    response = requests.get(url)
    ethnicityGuessData = response.json()
    return ethnicityGuessData['country'][0]['country_id']

def decodeCountryID(id: str) -> str:
    decoder = countryCodeDecoder.decoderDict
    return decoder[id]

def main():
    randomNames = getRandomNames()
    firstName: str = randomNames['first']
    lastName: str = randomNames['last']
    gender: str = guessGender(firstName)
    ethnicity: str = decodeCountryID(guessEthnicity(lastName))
    print(f'{firstName} {lastName} is a {gender} from {ethnicity}')

if __name__ == '__main__':
    main()
