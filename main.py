#from pypandoc.pandoc_download import download_pandoc
#import pypandoc
#from bs4 import BeautifulSoup
import lxml
import re
import word2html
import textile
import docx2txt
def converttoHTML(filepath, filelink, types, year):
    #output = pypandoc.convert_file(filepath, 'html')

    #with open('test.html', 'w') as fp:
        #fp.write(output)
    num_of_cards = 1
    allHtml = {}
    with open('dtc.html') as fp:
        soup = BeautifulSoup(fp, "lxml")
        soup2 = soup.get_text().replace('\n', '')
        all_card_tags = soup.find_all('p')
        matches = re.findall(r'<p>.+?</p>', str(soup))
        #print(str(soup))
        #print(matches)
        for i in matches:
          if 'http' in i:
            print(i)

        #for h4 in all_card_tags:
            #try:
              #print(h4)
              #print('\n')
              #print('\n')
              #print('\n')
              #print('\n')
                #abstract = h4

                #citation = h4.find_next("p")
                #card = h4.find_next("p").find_next("p")
                #full_doc = card
                #doc_word_length = len(full_doc.text.split())
                #if doc_word_length >= 70:
                    #allHtml["card " + str(num_of_cards)] = [{"tag": str(abstract), "cite": str(citation), "cardHtml": str(abstract) + str(citation) + str(full_doc), "filepath": filelink, "dtype": types, "year": year}]
                    #num_of_cards += 1
            #except AttributeError as e:
                #print("a card was skipped because " + str(e))
                #pass
    return allHtml

def newfunc():
  text = docx2txt.process("dtc2.docx")
  #print(text)
  html = textile.textile(text)
  #print(html)
  with open('dtc.html') as fp:
    #soup = BeautifulSoup(fp, "lxml")
    #soup2 = soup.get_text().replace('\n', '')
    #all_card_tags = soup.find_all('p')
    matches = re.findall(r'<p>.+?</p>', html)
    #print(str(soup))
    #print(matches)
    for i in matches:
      if 'http' in i:
        print(i)
        x = matches.index(i)
        print(matches[x+1])
        print('\n')





newfunc()