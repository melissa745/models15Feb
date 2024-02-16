import fitz  # PyMuPDF
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import nltk

class ProcesadorPDFSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Inicialización de cualquier atributo de estado necesario
        return cls._instance

    def leer_pdf(self, ruta_pdf):
        """Lee el texto de un archivo PDF."""
        texto_del_pdf = ""
        try:
            with fitz.open(ruta_pdf) as doc:
                texto_del_pdf = "".join([pagina.get_text() for pagina in doc])
        except Exception as e:
            print(f"Error al leer el archivo PDF: {e}")
            texto_del_pdf = ""  # Cambio aquí para devolver una cadena vacía en lugar de None
        return texto_del_pdf
    

    def generar_resumen(self, texto, sentences_count=2):
        """Genera un resumen del texto proporcionado."""
        if not texto:
            return "No hay texto para resumir."
        
        parser = PlaintextParser.from_string(texto, Tokenizer("english"))
        summarizer = TextRankSummarizer()
        summary = summarizer(parser.document, sentences_count)
        return " ".join(str(sentence) for sentence in summary)

    def extraer_respuestas(self, texto_pdf, preguntas):
        """Extrae respuestas a las preguntas dadas del texto del PDF."""
        if not texto_pdf:
            return ["El documento está vacío o no se pudo leer."]
        
        oraciones = nltk.sent_tokenize(texto_pdf)
        respuestas = {}
        for pregunta in preguntas:
            respuestas[pregunta] = next(
                (oracion for oracion in oraciones if pregunta.lower() in oracion.lower()), 
                "No se encontró respuesta."
            )
        return respuestas
