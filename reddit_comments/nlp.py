from google.cloud import language
import pandas as pd


class NLP:

    def __init__(self):
        self.__client = language.LanguageServiceClient()

    def _create_document(self, content, lang='en', type=language.enums.Document.Type.PLAIN_TEXT):
        return language.types.Document(content=content, language=lang, type=type)

    def analyse_entities(self, document):
        return self.__client.analyze_entities(document=self._create_document(document), encoding_type='UTF32')

    def analyse_entity_sentiment(self, document):
        return self.__client.analyze_entity_sentiment(document=self._create_document(document), encoding_type='UTF32')


if __name__ == "__main__":

    nlp = NLP()
    text = "The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document."
    response = nlp.analyse_entity_sentiment(text)

    for entity in response.entities:
        print('=' * 20)
        print('         name: {0}'.format(entity.name))
        print('     metadata: {0}'.format(entity.metadata))
        print('     salience: {0}'.format(entity.salience))
        print('     score: {0}'.format(entity.sentiment.score))
        print('     magnitude: {0}'.format(entity.sentiment.magnitude))

    #TODO: return results as a DataFrame
