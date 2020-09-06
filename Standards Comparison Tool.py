
import easygui
import os

import csv
from tkinter import *
from tkinter import messagebox
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from collections import Counter
from dataclasses import dataclass
from PIL import ImageTk, Image

firstFile = "";
secondFile = "";

a = False;
b = a;




def Click1():
        global firstFile;
        global secondFile;
        global a;
        global b;
        global Button3;
        global confirmLabel;
        global Button1;
        firstFile = easygui.fileopenbox(msg='Please select the first CSV file to be compared.',
                    title='Select CSV file',default=r'c:\Users\%username%\*.csv',
                    filetypes='*.csv');
        if(firstFile is not None):
                
                while(firstFile == secondFile):
                        print("The file located at " + firstFile + " was specified twice. Please select a different file");
                        secondFile = easygui.fileopenbox(msg='Please select the first CSV file to be compared.',
                            title='Select CSV file',default=r'c:\Users\%username%\*.csv',
                            filetypes='*.csv');
                a = True;
                if(a == b and a == True):
                        Button3["state"]=NORMAL;
                        head1, tail1 = os.path.split(firstFile);
                        head2,tail2 = os.path.split(secondFile);
                        ConfirmLabel.config(text="Comparing files : " + tail1 + " and " + tail2);

def Click2():
        global secondFile;
        global firstFile;
        global a;
        global b;
        global Button3;
        global ConfirmLabel;
        secondFile = easygui.fileopenbox(msg='Please select the first CSV file to be compared.',
                    title='Select CSV file',default=r'c:\Users\%username%\*.csv',
                    filetypes='*.csv');
        if(secondFile is not None):
                while(firstFile == secondFile):
                        print("The file located at " + firstFile + " was specified twice. Please select a different file");
                        secondFile = easygui.fileopenbox(msg='Please select the first CSV file to be compared.',
                            title='Select CSV file',default=r'c:\Users\%username%\*.csv',
                            filetypes='*.csv');
                b = True;
                if(a == b and a == True):
                        Button3["state"]=NORMAL;
                        head1, tail1 = os.path.split(firstFile);
                        head2,tail2 = os.path.split(secondFile);
                        ConfirmLabel.config(text="Comparing files : " + tail1 + " and " + tail2);
def Click3():



        global firstFile;
        global secondFile;
        global root;

        
        @dataclass
        class standards:
                year: str
                desc: str
                lineNum: int
                std: str
                GUID: str
                pGUID: str

        stand1 = [];
        stand2 = [];

        #START code for keeping track of word changes

        mostAddeds = "";
        mostRemoveds = "";
        mostAdded = 0;
        mostRemoved = 0;

        #Declare strings to store values from csv in
        tString1 = "";
        tString2 = "";

        #Exclude header row
        i = 0;

        ##print("Select the first file to be compared.");
        ##firstFile = easygui.fileopenbox(msg='Please select the first CSV file to be compared.',
        ##                    title='Select CSV file',default=r'c:\Users\%username%\*.csv',
        ##                    filetypes='*.csv');
        ##print("The first file selected was: " + firstFile);
        ##print("Select the second file to be compared.");
        ##secondFile = easygui.fileopenbox(msg='Please select the first CSV file to be compared.',
        ##                    title='Select CSV file',default=r'c:\Users\%username%\*.csv',
        ##                    filetypes='*.csv');
        ##while(firstFile == secondFile):
        ##        print("The file located at " + firstFile + " was specified twice. Please select a different file");
        ##        secondFile = easygui.fileopenbox(msg='Please select the first CSV file to be compared.',
        ##                    title='Select CSV file',default=r'c:\Users\%username%\*.csv',
        ##                    filetypes='*.csv');
        ##print("The second file selected was: " + secondFile);

        #Open both files and begin storing values in t string by appending each new row's description with a space
        with open(firstFile, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                    if(i != 0):
                        #print(row[16]);
                        tString1 += " " + row[12];
                        state1 = row[0];
                        grade1 = row[4];
                        year1 = row[3];
                        stand1.append(standards(row[3], row[12], i, row[8], row[14], row[15]));
                    i += 1;

        i = 0;
        with open(secondFile, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                    if(i != 0):
                        #print(row[14]);
                        tString2 += " " + row[12];
                        state2 = row[0];
                        grade2 = row[4];
                        year2 = row[3];
                        stand2.append(standards(row[3], row[12], i, row[8], row[14], row[15]));
                    i += 1;
        tList1 = tString1.split();
        tList2 = tString2.split();

        #Declare variable to track changes
        totChange = 0;

        contents = ['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'not', 'word', 'but', 'what', 'some', 'we', 'can', 'out', 'other', 'were', 'all', 'there', 'when', 'up', 'use', 'your', 'how', 'said', 'an', 'each', 'she', 'which', 'do', 'their', 'time', 'if', 'will', 'way', 'about', 'many', 'then', 'them', 'write', 'would', 'like', 'so', 'these', 'her', 'long', 'make', 'thing', 'see', 'him', 'two', 'has', 'look', 'more', 'day', 'could', 'go', 'come', 'did', 'number', 'sound', 'no', 'most', 'people', 'my', 'over', 'know', 'water', 'than', 'call', 'first', 'who', 'may', 'down', 'side', 'been', 'now', 'find', 'any', 'new', 'work', 'part', 'take', 'get', 'place', 'made', 'live', 'where', 'after', 'back', 'little', 'only', 'round', 'man', 'year', 'came', 'show', 'every', 'good', 'me', 'give', 'our', 'under', 'name', 'very', 'through', 'just', 'form', 'sentence', 'great', 'think', 'say', 'help', 'low', 'line', 'differ', 'turn', 'cause', 'much', 'mean', 'before', 'move', 'right', 'boy', 'old', 'too', 'same', 'tell', 'does', 'set', 'three', 'want', 'air', 'well', 'also', 'play', 'small', 'end', 'put', 'home', 'read', 'hand', 'port', 'large', 'spell', 'add', 'even', 'land', 'here', 'must', 'big', 'high', 'such', 'follow', 'act', 'why', 'ask', 'men', 'change', 'went', 'light', 'kind', 'off', 'need', 'house', 'picture', 'try', 'us', 'again', 'animal', 'point', 'mother', 'world', 'near', 'build', 'self', 'earth', 'father', 'head', 'stand', 'own', 'page', 'should', 'country', 'found', 'answer', 'school', 'grow', 'study', 'still', 'learn', 'plant', 'cover', 'food', 'sun', 'four', 'between', 'state', 'keep', 'eye', 'never', 'last', 'let', 'thought', 'city', 'tree', 'cross', 'farm', 'hard', 'start', 'might', 'story', 'saw', 'far', 'sea', 'draw', 'left', 'late', 'run', "don't", 'while', 'press', 'close', 'night', 'real', 'life', 'few', 'north', 'open', 'seem', 'together', 'next', 'white', 'children', 'begin', 'got', 'walk', 'example', 'ease', 'paper', 'group', 'always', 'music', 'those', 'both', 'mark', 'often', 'letter', 'until', 'mile', 'river', 'car', 'feet', 'care', 'second', 'book', 'carry', 'took', 'science', 'eat', 'room', 'friend', 'began', 'idea', 'fish', 'mountain', 'stop', 'once', 'base', 'hear', 'horse', 'cut', 'sure', 'watch', 'color', 'face', 'wood', 'main', 'enough', 'plain', 'girl', 'usual', 'young', 'ready', 'above', 'ever', 'red', 'list', 'though', 'feel', 'talk', 'bird', 'soon', 'body', 'dog', 'family', 'direct', 'pose', 'leave', 'song', 'measure', 'door', 'product', 'black', 'short', 'numeral', 'class', 'wind', 'question', 'happen', 'complete', 'ship', 'area', 'half', 'rock', 'order', 'fire', 'south', 'problem', 'piece', 'told', 'knew', 'pass', 'since', 'top', 'whole', 'king', 'space', 'heard', 'best', 'hour', 'better', 'true', 'during', 'hundred', 'five', 'remember', 'step', 'early', 'hold', 'west', 'ground', 'interest', 'reach', 'fast', 'verb', 'sing', 'listen', 'six', 'table', 'travel', 'less', 'morning', 'ten', 'simple', 'several', 'vowel', 'toward', 'war', 'lay', 'against', 'pattern', 'slow', 'center', 'love', 'person', 'money', 'serve', 'appear', 'road', 'map', 'rain', 'rule', 'govern', 'pull', 'cold', 'notice', 'voice', 'unit', 'power', 'town', 'fine', 'certain', 'fly', 'fall', 'lead', 'cry', 'dark', 'machine', 'note', 'wait', 'plan', 'figure', 'star', 'box', 'noun', 'field', 'rest', 'correct', 'able', 'pound', 'done', 'beauty', 'drive', 'stood', 'contain', 'front', 'teach', 'week', 'final', 'gave', 'green', 'oh', 'quick', 'develop', 'ocean', 'warm', 'free', 'minute', 'strong', 'special', 'mind', 'behind', 'clear', 'tail', 'produce', 'fact', 'street', 'inch', 'multiply', 'nothing', 'course', 'stay', 'wheel', 'full', 'force', 'blue', 'object', 'decide', 'surface', 'deep', 'moon', 'island', 'foot', 'system', 'busy', 'test', 'record', 'boat', 'common', 'gold', 'possible', 'plane', 'stead', 'dry', 'wonder', 'laugh', 'thousand', 'ago', 'ran', 'check', 'game', 'shape', 'equate', 'hot', 'miss', 'brought', 'heat', 'snow', 'tire', 'bring', 'yes', 'distant', 'fill', 'east', 'paint', 'language', 'among', 'grand', 'ball', 'yet', 'wave', 'drop', 'heart', 'am', 'present', 'heavy', 'dance', 'engine', 'position', 'arm', 'wide', 'sail', 'material', 'size', 'vary', 'settle', 'speak', 'weight', 'general', 'ice', 'matter', 'circle', 'pair', 'include', 'divide', 'syllable', 'felt', 'perhaps', 'pick', 'sudden', 'count', 'square', 'reason', 'length', 'represent', 'art', 'subject', 'region', 'energy', 'hunt', 'probable', 'bed', 'brother', 'egg', 'ride', 'cell', 'believe', 'fraction', 'forest', 'sit', 'race', 'window', 'store', 'summer', 'train', 'sleep', 'prove', 'lone', 'leg', 'exercise', 'wall', 'catch', 'mount', 'wish', 'sky', 'board', 'joy', 'winter', 'sat', 'written', 'wild', 'instrument', 'kept', 'glass', 'grass', 'cow', 'job', 'edge', 'sign', 'visit', 'past', 'soft', 'fun', 'bright', 'gas', 'weather', 'month', 'million', 'bear', 'finish', 'happy', 'hope', 'flower', 'clothe', 'strange', 'gone', 'jump', 'baby', 'eight', 'village', 'meet', 'root', 'buy', 'raise', 'solve', 'metal', 'whether', 'push', 'seven', 'paragraph', 'third', 'shall', 'held', 'hair', 'describe', 'cook', 'floor', 'either', 'result', 'burn', 'hill', 'safe', 'cat', 'century', 'consider', 'type', 'law', 'bit', 'coast', 'copy', 'phrase', 'silent', 'tall', 'sand', 'soil', 'roll', 'temperature', 'finger', 'industry', 'value', 'fight', 'lie', 'beat', 'excite', 'natural', 'view', 'sense', 'ear', 'else', 'quite', 'broke', 'case', 'middle', 'kill', 'son', 'lake', 'moment', 'scale', 'loud', 'spring', 'observe', 'child', 'straight', 'consonant', 'nation', 'dictionary', 'milk', 'speed', 'method', 'organ', 'pay', 'age', 'section', 'dress', 'cloud', 'surprise', 'quiet', 'stone', 'tiny', 'climb', 'cool', 'design', 'poor', 'lot', 'experiment', 'bottom', 'key', 'iron', 'single', 'stick', 'flat', 'twenty', 'skin', 'smile', 'crease', 'hole', 'trade', 'melody', 'trip', 'office', 'receive', 'row', 'mouth', 'exact', 'symbol', 'die', 'least', 'trouble', 'shout', 'except', 'wrote', 'seed', 'tone', 'join', 'suggest', 'clean', 'break', 'lady', 'yard', 'rise', 'bad', 'blow', 'oil', 'blood', 'touch', 'grew', 'cent', 'mix', 'team', 'wire', 'cost', 'lost', 'brown', 'wear', 'garden', 'equal', 'sent', 'choose', 'fell', 'fit', 'flow', 'fair', 'bank', 'collect', 'save', 'control', 'decimal', 'gentle', 'woman', 'captain', 'practice', 'separate', 'difficult', 'doctor', 'please', 'protect', 'noon', 'whose', 'locate', 'ring', 'character', 'insect', 'caught', 'period', 'indicate', 'radio', 'spoke', 'atom', 'human', 'history', 'effect', 'electric', 'expect', 'crop', 'modern', 'element', 'hit', 'student', 'corner', 'party', 'supply', 'bone', 'rail', 'imagine', 'provide', 'agree', 'thus', 'capital', "won't", 'chair', 'danger', 'fruit', 'rich', 'thick', 'soldier', 'process', 'operate', 'guess', 'necessary', 'sharp', 'wing', 'create', 'neighbor', 'wash', 'bat', 'rather', 'crowd', 'corn', 'compare', 'poem', 'string', 'bell', 'depend', 'meat', 'rub', 'tube', 'famous', 'dollar', 'stream', 'fear', 'sight', 'thin', 'triangle', 'planet', 'hurry', 'chief', 'colony', 'clock', 'mine', 'tie', 'enter', 'major', 'fresh', 'search', 'send', 'yellow', 'gun', 'allow', 'print', 'dead', 'spot', 'desert', 'suit', 'current', 'lift', 'rose', 'continue', 'block', 'chart', 'hat', 'sell', 'success', 'company', 'subtract', 'event', 'particular', 'deal', 'swim', 'term', 'opposite', 'wife', 'shoe', 'shoulder', 'spread', 'arrange', 'camp', 'invent', 'cotton', 'born', 'determine', 'quart', 'nine', 'truck', 'noise', 'level', 'chance', 'gather', 'shop', 'stretch', 'throw', 'shine', 'property', 'column', 'molecule', 'select', 'wrong', 'gray', 'repeat', 'require', 'broad', 'prepare', 'salt', 'nose', 'plural', 'anger', 'claim', 'continent', 'oxygen', 'sugar', 'death', 'pretty', 'skill', 'women', 'season', 'solution', 'magnet', 'silver', 'thank', 'branch', 'match', 'suffix', 'especially', 'fig', 'afraid', 'huge', 'sister', 'steel', 'discuss', 'forward', 'similar', 'guide', 'experience', 'score', 'apple', 'bought', 'led', 'pitch', 'coat', 'mass', 'card', 'band', 'rope', 'slip', 'win', 'dream', 'evening', 'condition', 'feed', 'tool', 'total', 'basic', 'smell', 'valley', 'nor', 'double', 'seat', 'arrive', 'master', 'track', 'parent', 'shore', 'division', 'sheet', 'substance', 'favor', 'connect', 'post', 'spend', 'chord', 'fat', 'glad', 'original', 'share', 'station', 'dad', 'bread', 'charge', 'proper', 'bar', 'offer', 'segment', 'slave', 'duck', 'instant', 'market', 'degree', 'populate', 'chick', 'dear', 'enemy', 'reply', 'drink', 'occur', 'support', 'speech', 'nature', 'range', 'steam', 'motion', 'path', 'liquid', 'log', 'meant', 'quotient', 'teeth', 'shell', 'neck'];

        #Remove punctuation, and then remove blank items from list
        for i, s in enumerate(tList1):
                if(tList1[i] in contents):
                    tList1[i] = "";
                tList1[i]=tList1[i].replace('.','');
                tList1[i]=tList1[i].replace(',','');
                tList1[i]=tList1[i].replace('(','');
                tList1[i]=tList1[i].replace(')','');
                tList1[i]=tList1[i].replace(';','');

        for i, s in enumerate(tList2):
                if(tList2[i] in contents):
                    tList2[i] = "";
                tList2[i]=tList2[i].replace('.','');
                tList2[i]=tList2[i].replace(',','');
                tList2[i]=tList2[i].replace('(','');
                tList2[i]=tList2[i].replace(')','');
                tList2[i]=tList2[i].replace(';','');

        while '' in tList1 : tList1.remove('');
        while '' in tList2 : tList2.remove('');


        #Generate dictionary
        comp1 = Counter(tList1);
        #print(comp1);
        comp2 = Counter(tList2);


        #Rebuild the lists as two strings
        tString1 = " ".join(tList1);
        tString2 = " ".join(tList2);

        #Iterate through the first list
        for word1 in comp1:
           #Iterate through second list, start integer to count the number of iterations
           i = 1;
           for word2 in comp2:
                #print(word1);
                if(word1.lower() == word2.lower() and (word1 or word2) != ""): break;
                elif(i == len(comp2)):
                    if(abs(comp1[word1]) > mostRemoved and word1 != ""):
                        mostRemoved = abs(comp1[word1]);
                        mostRemoveds = word1;
                #Track iterations
                i +=1;

        #Iterate through the second list
        for word2 in comp2:
            i = 1;
            #Identical words are already accounted for, so stop code if same word is found
            for word1 in  comp1:
                if(word2.lower() == word1.lower() and (word1 or word2) != ""): break;
                if(i == len(comp1)):
                    if(abs(comp2[word2]) > mostAdded and word2 != ""):
                        mostAdded = abs(comp2[word2]);
                        mostAddeds = word2;
                i += 1;
        i = 0;


##        print("Comparing: ");
##        print(state1 + ", " + grade1 + ", " + year1);
##        print(state2 + ", " + grade2 + ", " + year2);
##        print("Aligned by: " +  "{:.2f}".format(fuzz.ratio(tString1.lower(),tString2.lower()))+"%");
##        print("The word added the most times (" + str(mostAdded) + ") was: " + mostAddeds);
##        print("The word removed the most times (" + str(mostAdded) + ") was: " + mostRemoveds);
##        print("----------------------------------------------------------------");

        prList = [];


        ##Start writing out

        # State, Doc, Year, Grade, 2020 GUID, 2020 Parent GUID, 2020 Stand Desc, 2014 Stand Desc, 2014 GUID, 2014 Parent GUID
        
        with open(state1 + " " + year1 + " " + grade1 + " " + " vs " + state2 + " " + year2 + " " + grade2 + ".csv", 'w', encoding='utf-8') as csvfile:
                i = 0;
                wr =csv.writer(csvfile, lineterminator='', delimiter=',');

                wr.writerow(["Comparing: " + state1 + ", " + grade1 + ", " + year1 + " to " + state2 + ", " + grade2 + ", " + year2]);
                wr.writerow(['\n']);
                wr.writerow(["Aligned by: " +  "{:.2f}".format(fuzz.ratio(tString1.lower(),tString2.lower()))+"%"]);
                wr.writerow(['\n']);
                wr.writerow(["The word added the most times (" + str(mostAdded) + ") was: " + mostAddeds]);
                wr.writerow(['\n']);
                wr.writerow(["The word removed the most times (" + str(mostAdded) + ") was: " + mostRemoveds]);
                wr.writerow(['\n']);
                
                while i < len(stand1) and  i < len(stand2):
                        if(stand1[i].desc == stand2[i].desc):
                                wr.writerow([stand1[i].year + "'s " + stand1[i].std + " is aligned with " + stand2[i].year + "'s " + stand2[i].std + " on line " + str(stand1[i].lineNum) + "."]);
                                wr.writerow(['\n']);
                        elif(fuzz.ratio(stand1[i].desc.lower(), stand2[i].desc.lower()) >= 80):
                                prList.append(stand1[i].year + "'s " + stand1[i].std + " is mostly similar to " + stand2[i].year + "'s " + stand2[i].std + " on line " + str(stand1[i].lineNum) + ".");
                        i += 1;

                i = 0;

                while i < len(prList):
                        wr.writerow([prList[i]]);
                        wr.writerow(['\n']);
                        i += 1;

                while i < len(stand1) and i < len(stand2):
                        if(stand1[i].std != stand2[i].std):
                                wr.writerow([stand1[i].year + "'s " + stand1[i].std + " was changed to " + stand2[i].std + " in " + stand2[i].year]);
                                wr.writerow(['\n']);
                        i += 1;
                i = 0;
                #Generate header row
                wr.writerow(['\n']);
                wr.writerow(['\n']);
                wr.writerow(['\n']);
                wr.writerow(["State", "Grade", year1 + " GUID", year1 + " Parent GUID", year1 + " Standard ", year1 + " Description", year2 + " Description", year2 + " Standard ", year2 + " GUID", year2 + " Parent GUID"]);
                if len(stand1) >= len(stand2):
                        while i < len(stand1):
                                if(i >= len(stand2)):
                                        wr.writerow(['\n']);
                                        wr.writerow([state1, grade1, stand1[i].GUID, stand1[i].pGUID, stand1[i].std, stand1[i].desc, "N/A", "N/A", "N/A", "N/A", "N/A"]);
                                else:
                                        wr.writerow(['\n']);
                                        wr.writerow([state1, grade1, stand1[i].GUID, stand1[i].pGUID, stand1[i].std, stand1[i].desc, stand2[i].desc, stand2[i].std, stand2[i].GUID, stand2[i].pGUID]);
                                i += 1;


                else:
                        while i < len(stand2):
                                if(i >= len(stand1)):
                                        wr.writerow(['\n']);
                                        wr.writerow([state1, grade1, "N/A", "N/A", "N.A", "N/A", stand2[i].desc, stand2[i].std, stand2[i].GUID, stand2[i].pGUID]);
                                else:
                                        wr.writerow(['\n']);
                                        wr.writerow([state1, grade1, stand1[i].GUID, stand1[i].pGUID, stand1[i].std, stand1[i].desc, stand2[i].desc, stand2[i].std, stand2[i].GUID, stand2[i].pGUID]);
                                i += 1;

        messagebox.showinfo(title="Report Complete", message="Your report has successfully been created at " + os.getcwd() + "\\" + state1 + " " + year1 + " " + grade1 + " " + " vs " + state2 + " " + year2 + " " + grade2 + ".csv. ");


root = Tk();
photo = """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"""
img = PhotoImage(data=photo);

iconphoto = """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"""
iconimg = PhotoImage(data=iconphoto);
root.iconphoto(True, iconimg);
panel = Label(root, image=img)
panel.grid(row=9,column=0);
root.title('Standards Comparison Tool');


Label2 = Label(root, text="Created by: Joshua Whitaker");
Label3 = Label(root, text="Supervised by: Kenya Wallach");
fillLabel = Label(root, text="");


#Label1 = Label(root, text="Select your files below, and then click the 'Generate Report' button to generate a report.");
Button1 = Button(root, text="Select your first file.", command=Click1);
Button2 = Button(root, text="Select your second file.", command=Click2);
Button3 = Button(root, text="Generate report.", command=Click3, state=DISABLED);

ConfirmLabel = Label(root);
ConfirmLabel.grid(row=5,column=0);

fillLabel.grid(row=6,column=0);
Label3.grid(row=8, column=0);
Label2.grid(row=7, column=0);
#Label1.grid(row=0, column=0);
Button1.grid(row=2,column=0);
Button1.config(height=4, width=30);
Button2.grid(row=3,column=0);
Button2.config(height=4, width=30);
Button3.grid(row=4,column=0);
Button3.config(height=4,width=30);


root.mainloop();

