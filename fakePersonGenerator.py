import requests
import countryCodeDecoder # type: ignore

def getRandomNames() -> dict:
    response = requests.get(randomUserUrl)
    randomUserData = response.json()
    return randomUserData['results'][0]["name"]

def appendNameToUrl(url: str, name: str) -> str:
    '''
    appends the second parameter to the first, used to generate the correct query for the gender and nationality APIs

    Parameters
    ----------
    url: str
    name (first or last): str

    Returns
    --------
    string containing the concatenated url
    '''
    url += name
    return url

def guessGender(firstName: str) -> str:
    '''
    Guesses the gender of the given first name using genderize.io API

    Paramater
    ---------
    the first name of the person

    Returns
    --------
    string contaning either 'male' or 'female'
    '''
    url = appendNameToUrl('https://api.genderize.io/?name=', firstName)
    response = requests.get(url)
    genderGuessData = response.json()
    return genderGuessData['gender']

def guessEthnicity(lastName: str) -> str:
    '''
    Guesses the ethnicity of a given last name using nationalize.io API

    Parameter
    ---------
    last name of the person

    Returns
    -------
    the country code of the country they are from
    '''
    url = appendNameToUrl('https://api.nationalize.io/?name=', lastName)
    response = requests.get(url)
    ethnicityGuessData = response.json()
    return ethnicityGuessData['country'][0]['country_id']

def decodeCountryID(id: str) -> str:
    '''
    Decodes the given country code using the country code decoder

    Parameter
    ---------
    2 character country code 
    ex: US

    Returns
    -------
    The full name of the country
    '''
    decoder = countryCodeDecoder.decoderDict
    return decoder[id]

def main():
    randomNames = getRandomNames() #gets table of random names
    firstName: str = randomNames['first']
    lastName: str = randomNames['last']
    gender: str = guessGender(firstName)
    ethnicity: str = decodeCountryID(guessEthnicity(lastName)) #decodes country code from last name
    print(f'{firstName} {lastName} is a {gender} from {ethnicity}')

if __name__ == '__main__':
    main()
