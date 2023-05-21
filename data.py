from spacy.matcher import Matcher
import re
class CustomMatcher():
    def __init__(self, nlp):
        self.nlp = nlp
        
    # Extract the span matching the pattern
    def extract_text(self, doc, pattern,pattern_type):
        # define the matcher 
        matcher = Matcher(self.nlp.vocab)
        matcher.add(str(pattern_type), pattern)
        matches = matcher(doc)
        matched_text_list = []
        for match_id, start, end in matches:
            
        #####################################################################:> DEBITED <:#####################################################################
        
            if self.nlp.vocab.strings[match_id] == "debited1":
                text = doc[start:end]
                if text:
                    span = str(text[0])
                matched_text_list.append(span)
                
            elif self.nlp.vocab.strings[match_id] == "debited2":
                text = doc[start:end]
                if text:
                    span = str(text[1])
                matched_text_list.append(span)
                
            elif self.nlp.vocab.strings[match_id] == "debited3":
                text = doc[start:end]
                if text:
                    span = str(text[2])
                matched_text_list.append(span)
                
            elif self.nlp.vocab.strings[match_id] == "debited4":
                text = doc[start:end]
                if text:
                    span = str(text[3])
                matched_text_list.append(span)
                
            elif self.nlp.vocab.strings[match_id] == "debited5":
                text = doc[start:end]
                # print(text)
                if text:
                    span = str(text[4])
                matched_text_list.append(span)
                
            elif self.nlp.vocab.strings[match_id] == "debited6":
                text = doc[start:end]
                if text:
                    span = str(text[-1])
                    # span = re.findall(r"\d+[,.]\d+[.]\d+|\d+[.,]\d+|\d+", text)
                matched_text_list.append(span)
                
            elif self.nlp.vocab.strings[match_id] == "debited7":
                text = doc[start:end]
                if text:
                    span = text[-1]
                    # span = re.findall(r"Rs[.,:]\d+[.]\d+|Rs[.,:]\d+|INR[.,:]\d+[.]\d+|INR[.,:]\d+|\d[.,]\d+[.]\d+|\d+[,.]\d+|\d+", str(text))
                    # print('DEB7 ==>', span)
                matched_text_list.append(str(span))
                
        ######################################################################:> AVAILABLE <:#####################################################################
        
            elif self.nlp.vocab.strings[match_id] == "avl":
                text = doc[start:end]
                if text:
                    span1 = str(text[-1])
                    # print("SPAN! ==>",span1)
                matched_text_list.append(span1)
        
        #####################################################################:> CREDITED <:#######################################################################
            elif self.nlp.vocab.strings[match_id] == "credited1":
                text = doc[start:end]
                if text:
                    span = str(text[-1])
                matched_text_list.append(span)
                
            elif self.nlp.vocab.strings[match_id] == "credited2":
                text = doc[start:end]
                if text:
                    span = str(text[1])
                matched_text_list.append(span)
                
            elif self.nlp.vocab.strings[match_id] == "credited3":
                text = doc[start:end]
                if text:
                    span = str(text[0])
                matched_text_list.append(span)
                
            elif self.nlp.vocab.strings[match_id] == "credited4":
                text = doc[start:end]
                if text:
                    span = str(text[-2])
                matched_text_list.append(span)
            
            # print(matched_text_list)
        return matched_text_list
    
##############################################################################:> PATTERNS <:##################################################################################

    def get_patterns(self, patternFor, params=False):
        
        if patternFor == 'avl':
            available1 = [
                            {"TEXT" : {'IN' : ["Available", "available", "Avl", "Avlb", "Avbl", "Aval", "Avlbl", "Avail", 'Avail.bal', ".Avl", "Total", 'UPI.Available', "clr", "Clr", "New", "new", "NEW", "Cur"] }},
                            {"TEXT" : {"IN" : ['clear', "Clear", "Amt", "amount", "Amount"]}, "OP":"?"},
                            {"TEXT" : {"IN" : ['.'] },'OP' : '?'},
                            {"TEXT" : {'IN' : ["Bal", "Balance", "balance", "bal", "Bal-", "bal-" ] }, 'OP' : '?'},
                            {"TEXT" : {'IN' : ["in", 'is', ':', '.', "Rs" ]},'OP' : '?'},
                            {"TEXT" : {'IN' : ["INR", "INR:",".","Rs" ]},'OP' : '?'},
                            {"TEXT" : {"IN" : ["INR", "."]}, "OP":"?"},
                            {"TEXT" : {"REGEX": "Rs[.:]\s+\d+[.,]\d+[.]\d+|Rs[.:]\s+\d+|Rs[.:]\d+|\d+[.,]\d+[.]\d+|Bal:INR\d+[,.]\d+[.]\d+|Bal:INR\d+[,.]\d+|\d+[.,]\d+[,.]\d+[.]\d+|\d+[,.]\d+[.]\d+|\d+[.,]\d+|\d+"}}
                         ]
            
            available2 = [  {"TEXT" : {"IN" : ["BAL", "Bal", "bal"]}},
                            {"TEXT" : {"IN" : ["IS", "INR"]}},
                            {"TEXT" : {"REGEX" : "BAL-Rs[.]\d+[,.]\d+[.]\d+|BAL-Rs[.]\d+[.]\d+|Bal-Rs[.]\d+[,.]\d+[.]\d+|Bal-Rs[.]\d+[.]\d+|\d+[.]\d+"}}
                         ]
            
            available3 = [  {"TEXT" : {"IN" : ["BAL", "Bal", "bal"] }},
                            {"TEXT" : {"IN" : ["IS", "INR", "is"]  }},
                            {"TEXT" : {"REGEX" : "Rs[.]\d+[,.]\d+[.]\d+|Rs[.,]\d+[.,]\d+"}}
                         ]
            available4 = [  {"TEXT" : {"IN" : ["Current", "current"] }},
                            {"TEXT" : {"IN" : ["Balance", "Bal"] }},
                            {"TEXT" : {"IN" : ["IS", "is"]  }},
                            {"TEXT" : {"REGEX" : "INR\d+[,.]\d+[.]\d+|INR\d+[.,]\d+|INR\d+"}}
                         ]
            pattern = [ available1, available2, available3, available4 ]
            return pattern

        elif patternFor == 'credited1':
            credited1 = [{"TEXT" : {"IN" : [ "Credited", "credited", "Received", "received" ]} }, 
                         {"TEXT" : {"IN" : ["for", "with", "by"]}, "OP" : "?"},
                         {"TEXT" : {"IN" : ["INR", "Rs"]}, "OP" : "?" },
                         {"TEXT" : {"IN" : [".", ",", ":"]}, "OP":"?"},
                         {"TEXT" : {"REGEX": "Rs[.,:]\d+[.]\d+|Rs[.:,]\d+|Rs[.,:]\d+|\d+[,.]\d+[.]\d+|\d+[,.]\d+|\d+"}}
                        ]
            pattern1 = [credited1]
            return pattern1
        
        elif patternFor=='credited2':
            credited2 = [{"TEXT" : {"IN": ["INR", "RS", "Rs", "rs"]}}, 
                         {"TEXT" : {"REGEX": "\d+[.,]\d+[.]\d+|\d+[.,]\d+|\d+"}},
                         {"TEXT" : {"IN" :[ "has","was", "Was" ]}, "OP":"?"},
                         {"TEXT" : "been", "OP":"?"},
                         {"TEXT" :{"IN" : [ "CREDITED", "Credited", "credited", "settled", "Settled", "SETTLED" ]}}
                        ]
            pattern2 = [credited2]
            return pattern2
            
        elif patternFor=='credited3':
            credited3 = [{"TEXT" : {"REGEX": "Rs[\.,:]\d+[.]\d+|Rs[\.,:]\d+"}},
                         {"TEXT" : "for"},
                         {"TEXT" : {"REGEX": "\w+[-]\d+"}},
                         {"TEXT" : "credited"}
                        ]

            credited4 = [{"TEXT"  : {"REGEX": "INR[\.:]\d+[.]\d+|INR[\.:]\d+"}},
                         {"TEXT"  : {"IN" : ["credited", "Credited"]}}, 
                         {"TEXT"  : "to"}
                       ]

            credited5 = [{"TEXT"  : {"REGEX": "Rs[\.:]\d+[.]\d+|Rs[\.:]\d+"}},
                         {"TEXT"  : {"IN" : ["credited", "Credited"]}}, 
                         {"TEXT"  : "to"}
                       ]

            credited6 = [{"TEXT"  : {"REGEX": "Rs[\.:]\d+[.]\d+|Rs[\.:]\d+"}},
                          {"TEXT" : "has"},
                          {"TEXT" : "been"},
                          {"TEXT"  : {"IN" : ["credited", "Credited"]}}]
            
            credited7 = [{"TEXT"  : {"REGEX": "Rs[\.,:]\d+[.]\d+|Rs[\.,:]\d+|Rs[.,]\d+"}},
                         {"TEXT"  : {"IN" : ["IS", "is", "Is"]}, "OP":"?"},
                         {"TEXT"  :  {"IN" : [ "credited", 'Credited', "CREDITED" ]}},
                         {"TEXT"  : {"IN" : ["to", "To", "TO"]}, "OP":"?"}
                         ]

            pattern3 = [ credited3, credited4, credited6, credited7 ]
            return pattern3
        
        elif patternFor == 'credited4':
            credited4 = [
                         {"TEXT"  : {"IN" : ["Rs"] }},
                         {"TEXT"  : {"IN" : ["."]}},
                         {"TEXT"  : {"REGEX": "\d+[.,]\d+[.]\d+|\d+[.,]\d+|\d+"}},
                         {"TEXT"  : {"IN" : ["credited", "Credited"]}}
                        ]
            pattern4 = [ credited4 ]
            return pattern4
        
        elif patternFor == 'debited1':

            debited1 = [
                        {"TEXT" : {"REGEX": "Rs[.,:]\d+[.]\d+|Rs[.,:]\d+|Rs[.]\d+[.]\d+|Rs[.]\d+|INR[.,:]\d+[.]\d+|INR[.,:]\d+|\d[.,]\d+[.]\d+|\d+[,.]\d+"}},
                        {"TEXT" : {"IN" : [ "debited", "Debited", "paid", "Paid", "PAID", "Transferred", "transferred", "debited@SBI"] }}, 
                        {"TEXT" : {"IN" : [ "from", "From", "FROM", "Through", "THROUGH", "Thru", "thru" , "to"]}, "OP": "?" }
                       ]
            debited2 = [
                        {"TEXT" : {"REGEX": "Rs[.,:]\d+[.]\d+|Rs[.,:]\d+|INR[.,:]\d+[.]\d+|INR[.,:]\d+|\d[.,]\d+[.]\d+|\d+[,.]\d+"}},
                        {"TEXT" : {"IN" : [ "IS", "Is", "is" ] }},
                        {"TEXT" : {"IN" : [ "debited", "Debited", "DEBITED"] }},
                        {"TEXT" : {"IN" : [ "from", "From", "FROM", "to" ] }, "OP":"?"}
                       ]
            debited3 = [
                        {"TEXT" : {"REGEX" : "\d+[,.]\d+[.]\d+|\d+[.,]\d+"}},
                        {"TEXT" : {"IN" : ["is", "IS"]}},
                        {"TEXT" : {"IN" : [ "Debited","DEBITED"]}}
                       ]
            debited4 = [
                        {"TEXT" : {"REGEX": "Rs[.,:]\d+[.]\d+|Rs[.,:]\d+|Rs[.]\d+[.]\d+|Rs[.]\d+|INR[.,:]\d+[.]\d+|INR[.,:]\d+|\d[.,]\d+[.]\d+|\d+[,.]\d+"}},
                        {"TEXT" : {"IN" : [ "has"] }}, 
                        {"TEXT" : {"IN" : [ "been"] }},
                        {"TEXT" : {"IN" : [ "debited"] }}
                       ]
            
            debited1 = [ debited1, debited2, debited3, debited4 ]
            return debited1
        
        elif patternFor == 'debited2':
            debited2 = [
                        {"TEXT" : {"IN" : ["INR", "Rs", "rs" ]}}, 
                        {"TEXT" : {"REGEX": "\d+[,.]\d+[.]\d+|\d+[.]\d+|\d+"}},
                        {"TEXT" : "has", "OP":"?"},
                        {"TEXT" : "been", "OP":"?"},
                        {"TEXT" : {"IN" : ["debited", "DEBITED", "Debited" ]}}
                        ]
            debited3 = [{"TEXT" : {"IN" : [ "INR", "Rs" ]}},
                        {"TEXT" : {"REGEX" : "\d+[,.]\d+[.]\d+|\d+[.,]\d+"}},
                        {"TEXT" : {"IN" : ["is", "IS", "Paid", "PAID", "paid", "was", 'Was' ]}, "OP":"?"},
                        {"TEXT" : {"IN" : [ "debited", "Debited","DEBITED", "by", "BY", "By"]}}
                       ]
            
            debited2 = [ debited2, debited3 ]
            return debited2
        
        elif patternFor == 'debited3':    
            
            debited3 = [
                        {"TEXT" : {"IN" : ["Rs"] }},
                        {"TEXT" : {"IN" : ["."]}, "OP" : "?" },
                        {"TEXT" : {"REGEX" : "\d+[,.]\d+[.]\d+|\d+[.,]\d+"}},
                        {"TEXT" : {"IN" : ["is", "IS"]}},
                        {"TEXT" : {"IN" : ["Debited", "debited" ]}}
                       ]
            debited3 = [debited3]
            return debited3
        
        elif patternFor == 'debited4': 
        
            debited4 = [
                        {"TEXT" : "Amount"},
                        {"TEXT" : "of"},
                        {"TEXT" : "Rs"},
                        {"TEXT" : {"REGEX" : "\d+[,.]\d+[.]\d+|\d+[.,]\d+|\d+"}},
                        {"TEXT" : "is"},
                        {"TEXT" : {"IN" : ["Debited", "debited" ]}}
                       ]
            debited4A = [
                        {"TEXT" : "Rs"},
                        {"TEXT" : "."},
                        {"TEXT" : "INR"},
                        {"TEXT" : {"REGEX" : "\d+[,.]\d+[.]\d+|\d+[.,]\d+|\d+"}},
                        {"TEXT" : "has"},
                        {"TEXT" : "been"},
                        {"TEXT" : {"IN" : ["Debited", "debited" ]}}
                       ]
            
            debited4B = [
                        {"TEXT" : "Cash"},
                        {"TEXT" : "withdrawal"},
                        {"TEXT" : "of"},
                        {"TEXT" : {"REGEX" : "Rs\d+[,.]\d+[.]\d+|Rs\d+[.,]\d+|Rs\d+"}}
                       ]
            debited4 = [ debited4, debited4A, debited4B ]
            return debited4
        
        elif patternFor == 'debited5': 
        
            debited5 = [
                        {"TEXT" : "Amount"},
                        {"TEXT" : "of"},
                        {"TEXT" : "Rs"},
                        {"TEXT" : {"IN" : ["."]}},
                        {"TEXT" : {"REGEX" : "\d+[,.]\d+[.]\d+|\d+[.,]\d+|\d+"}},
                        {"TEXT" : "is"},
                        {"TEXT" : {"IN" : ["Debited", "debited" ]}}
                       ]
            debited5 = [ debited5 ]
            return debited5
        
        elif patternFor == 'debited6':
            debited6 = [{"TEXT" : "has"},
                        {"TEXT" : "been"},
                        {"TEXT" : {"IN" : [ "Debited","DEBITED"]}},
                        {"TEXT" : {"IN" : ["with"]}, "OP":"?"},
                        {"TEXT" : {"IN" : ["rs", "Rs", "INR" ]}, "OP" : "?" },
                        {"TEXT" : {"REGEX" : "\d+[,.]\d+[.]\d+|\d+[.,]\d+"}}
                       ]
            debited6 = [ debited6 ]
            return debited6
        
        elif patternFor == 'debited7':
            debited7 = [
                        {"TEXT" : {'IN' : ["Debited", "debited", "DEBITED"] }}, 
                        {"TEXT" : {"IN" : ["by", "with", "for", "Rs" ]}, "OP" : "?" }, 
                        {"TEXT" : {"IN" : ["INR", "Rs"]}, "OP" : "?"},
                        {"TEXT" : {"IN" : [".", ",", ":", "-" ]}, "OP" : "?"},
                        {"TEXT" : {"REGEX": "Rs[.,:]\d+[.]\d+|Rs[.,:]\d+|INR[.,:]\d+[.]\d+|INR[.,:]\d+|\d[.,]\d+[.]\d+|\d+[,.]\d+|\d+"}}
                       ]
            debited7 = [ debited7 ]
            return debited7
