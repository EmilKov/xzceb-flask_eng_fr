import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

def english_to_french(english_text):
    french_text_translated = language_translator.translate(
            text=english_text,model_id='en-fr'
        ).get_result()
    return french_text_translated.get('translations')[0].get('translation')

def french_to_english(french_text):
    english_text_translated = language_translator.translate(
            text=french_text,model_id='fr-en'
        ).get_result()
    return english_text_translated.get('translations')[0].get('translation')

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)