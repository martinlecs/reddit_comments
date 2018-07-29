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

    def comment_batch_analysis(self, gen):
        """
        :param gen: Comment
             Comment generator function
        :return: Dict
        """
        df = pd.DataFrame(columns=['name', 'salience', 'score', 'magnitude'])
        for comment in gen:
            if comment is None:
                break
            response = self.analyse_entity_sentiment(comment.body)
            for entity in response.entities:
                entry = {'name': entity.name, 'salience': entity.salience, 'score': entity.sentiment.score, 'magnitude': entity.sentiment.magnitude}
                df = df.append(entry, ignore_index=True)

        df = df.groupby('name').mean().reset_index()
        return df.to_dict(orient='records')




if __name__ == "__main__":

    nlp = NLP()
    text = ["The score of a document's sentiment indicates the overall emotion of a document. The magnitude of a document's sentiment indicates how much emotional content is present within the document, and this value is often proportional to the length of the document."]
    gen = (i for i in text)

    df = nlp.comment_batch_analysis(gen)
    print(df)

