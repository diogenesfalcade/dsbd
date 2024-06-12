from pypdf import PdfReader
import pdfplumber
from functools import partial
from deep_translator import GoogleTranslator
from nltk.tokenize import sent_tokenize
from fpdf import FPDF
from tqdm import tqdm
import sys

inputFile = sys.argv[1]

def not_within_bboxes(obj, bboxes):
    """Check if the object is in any of the table's bbox."""
    def obj_in_bbox(_bbox):
        """See https://github.com/jsvine/pdfplumber/blob/stable/pdfplumber/table.py#L404"""
        v_mid = (obj["top"] + obj["bottom"]) / 2
        h_mid = (obj["x0"] + obj["x1"]) / 2
        x0, top, x1, bottom = _bbox
        return (h_mid >= x0) and (h_mid < x1) and (v_mid >= top) and (v_mid < bottom)
    return not any(obj_in_bbox(__bbox) for __bbox in bboxes)

def extract(page):
    """Extract PDF text.

    Filter out tables and delete in-paragraph line-breaks.
    """
    # Filter-out tables
    if page.find_tables() != []:
        # Get the bounding boxes of the tables on the page.
        # Adapted From https://github.com/jsvine/pdfplumber/issues/242#issuecomment-668448246
        bboxes = [table.bbox for table in page.find_tables()]
        
        bbox_not_within_bboxes = partial(not_within_bboxes, bboxes=bboxes) 

        # Filter-out tables from page
        page = page.filter(bbox_not_within_bboxes)

    # Extract Text
    extracted = page.extract_text()

    # Delete in-paragraph line breaks
    extracted = extracted.replace(".\n", "**/m" # keep paragraph breaks
                        ).replace(". \n", "**/m" # keep paragraph breaks
                        ).replace("\n", "" # delete in-paragraph breaks (i.e. all remaining \n)
                        ).replace("**/m", ".\n\n") # restore paragraph breaks
    
    return extracted

def translate_extracted(Extracted):
    """Wrapper for Google Translate with upload workaround.
    
    Collects chuncks of senteces below limit to translate.
    """
    # Set-up and wrap translation client
    translate = GoogleTranslator(source='en', target='pt').translate

    # Split input text into a list of sentences
    sentences = sent_tokenize(Extracted)

    # Initialize containers
    translated_text = ''
    source_text_chunk = ''

    # collect chuncks of sentences below limit and translate them individually
    for sentence in sentences:
        # if chunck together with current sentence is below limit, add the sentence
        if ((len(sentence.encode('utf-8')) + len(source_text_chunk.encode('utf-8')) < 5000)):
            source_text_chunk += ' ' + sentence
        
        # else translate chunck and start new one with current sentence
        else:
            translated_text += ' ' + translate(source_text_chunk)

            # if current sentence smaller than 5000 chars, start new chunck
            if (len(sentence.encode('utf-8')) < 5000):
                source_text_chunk = sentence

            # else, replace sentence with notification message
            else:    
                message = "<<Omitted Word longer than 5000bytes>>"
                translated_text += ' ' + translate(message)

                # Re-set text container to empty
                source_text_chunk = ''

    # Translate the final chunk of input text, if there is any valid text left to translate
    if translate(source_text_chunk) != None:
        translated_text += ' ' + translate(source_text_chunk)
    
    return translated_text

# Open PDF
with pdfplumber.open(inputFile) as pdf:
    # Initialize FPDF file to write on
    fpdf = FPDF()
    fpdf.set_font("Helvetica", size = 7)
    
    # Treat each page individually
    for page in tqdm(pdf.pages[:30], desc="Processing Pages", unit="page"):
        # Extract Page
        extracted = extract(page)

        # Translate Page
        if extracted != "":
            # Translate paragraphs individually to keep breaks
            paragraphs = extracted.split("\n\n")
            translated = "\n\n".join(
                [translate_extracted(paragraph) for paragraph in paragraphs]
                )
        else:
            translated = extracted

        # Write Page
        fpdf.add_page()
        fpdf.multi_cell(w=0,
                        h=5,
                        txt= translated.encode("latin-1",
                                               errors = "replace"
                                      ).decode("latin-1")
                        )
    
    # Save all FPDF pages
    fpdf.output("output/file_translated.pdf")