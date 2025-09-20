import streamlit as st
import random
#from PyMultiDictionary import MultiDictionary
#dictionary = MultiDictionary()
#import enchant
#d = enchant.Dict("en_US")
#from PyDictionary import PyDictionary
import nltk
from nltk.corpus import words

# One-time setup
nltk.download('words')
word_set = set(words.words())

def is_english_word(word):
    return word.lower() in word_set

#dictionary = PyDictionary()

def reset_state():
    st.session_state.word = random.choice(st.session_state.word_list)
    print(st.session_state.word)
    st.session_state.attempt_count = 1
    st.session_state.match = [[0 for _ in range(5)] for _ in range(6)]
    st.session_state.textInputList = ["","","","","",""]
    st.session_state.word_chosen=""
    st.session_state.status = False

def init_state():
    WORDLE_WORDS = [
    "about","above","actor","admit","adopt","adult","after","again","agent","agree",
    "ahead","alarm","album","alert","alike","alive","allow","alone","along","aloud",
    "alter","angel","anger","angry","apart","apple","apply","arena","argue","arise",
    "array","aside","asset","audio","avoid","award","aware","badly","baker","bases",
    "basic","basis","beach","beard","beast","began","begin","begun","being","below",
    "bench","billy","birth","black","blame","blank","blind","block","blood","board",
    "boost","booth","bound","brain","brand","bread","break","breed","brief","bring",
    "broad","broke","brown","build","built","buyer","cable","calls","calm","camel",
    "camps","canal","candy","carry","catch","cause","cease","chain","chair","chalk",
    "champ","chant","chaos","charm","chart","chase","cheap","check","cheek","cheer",
    "chess","chest","chief","child","china","choir","chose","civil","claim","class",
    "clean","clear","clerk","click","climb","clock","close","cloth","cloud","coach",
    "coast","could","count","court","cover","craft","crash","crazy","cream","crime",
    "cross","crowd","crown","curve","cycle","daily","dance","dated","dates","dealt",
    "death","debut","delay","depth","dirty","doubt","dozen","draft","drama","drawn",
    "dream","dress","drill","drink","drive","drove","dying","eager","early","earth",
    "eight","elite","empty","enemy","enjoy","enter","entry","equal","error","errie","event",
    "every","exact","exist","extra","faith","false","fault","favor","fears","fence",
    "fewer","field","fifth","fifty","fight","final","first","fixed","flash","fleet",
    "floor","fluid","focus","force","forth","forty","found","frame","frank","fraud",
    "fresh","front","fruit","fully","funny","giant","given","glass","globe","going",
    "goods","grace","grade","grand","grant","grass","great","green","greet","gross",
    "group","grown","guard","guess","guest","guide","habit","happy","harsh","heart",
    "heavy","hence","hills","hobby","holds","holes","honor","horse","hotel","house",
    "human","humor","ideal","ideas","image","imply","index","inner","input","issue",
    "jeans","jelly","jolly","judge","juice","knife","known","label","labor","large",
    "later","laugh","layer","learn","lease","least","leave","legal","level","light",
    "limit","lives","local","logic","loose","lucky","lunch","major","maker","march",
    "match","maybe","mayor","meant","media","metal","might","minor","minus","mixed",
    "model","money","month","moral","motor","mount","mouse","mouth","movie","music",
    "needs","never","newly","night","noise","north","noted","novel","nurse","occur",
    "ocean","offer","often","order","other","ought","paint","panel","paper","party",
    "peace","phase","phone","photo","piece","pilot","pitch","place","plain","plane",
    "plant","plate","point","pound","power","press","price","pride","prime","print",
    "prior","prize","proof","proud","prove","puppy","queen","quick","quiet","quite","radio",
    "raise","range","rapid","ratio","reach","react","ready","refer","right","rival",
    "river","roads","rocks","roman","rough","round","route","royal","rural","scale",
    "scene","scope","score","sense","serve","seven","shall","shape","share","sharp",
    "sheet","shelf","shell","shift","shine","shirt","shock","shoot","short","shown",
    "shows","sides","sight","since","skill","sleep","slide","small","smart","smile",
    "smith","smoke","solid","solve","sorry","sound","south","space","spare","speak",
    "speed","spend","spent","split","spoke","sport","staff","stage","stand","start",
    "state","steam","steel","stick","still","stock","stone","stood","store","storm",
    "story","strip","stuck","study","stuff","style","sugar","suite","super","sweet",
    "table","taken","taste","teach","teeth","terms","thank","their","theme","there",
    "these","thick","thing","think","third","those","three","threw","throw","tight",
    "times","tired","title","today","topic","total","touch","tough","tower","track",
    "trade","train","treat","trend","trial","tried","tries","truck","truly","trust",
    "truth","twice","under","union","unity","until","upper","upset","urban","usage",
    "usual","valid","value","video","visit","vital","voice","waste","watch","water",
    "wears","weeks","weird","where","which","while","white","whole","whose","woman",
    "women","world","worry","worse","worst","worth","would","wound","write","wrong",
    "wrote","young","youth"
    ]
    if "word_list" not in st.session_state:
        st.session_state.word_list = WORDLE_WORDS

    if "word" not in st.session_state:
        st.session_state.word = random.choice(WORDLE_WORDS)
        print(st.session_state.word)

    if "attempt_count" not in st.session_state:
        st.session_state.attempt_count = 1    

    if "match" not in st.session_state:
        st.session_state.match = [[0 for _ in range(5)] for _ in range(6)]
        print(st.session_state.match)

    if "textInputList" not in st.session_state:
        st.session_state.textInputList = ["","","","","",""]

    if"status" not in st.session_state:
        st.session_state.status = False    


def check_answer():
    word_index = "word_"+str(st.session_state.attempt_count)
    word_chosen = st.session_state[word_index].lower()
    if not word_chosen or len(word_chosen) <5:
        return
    
    if not is_english_word(word_chosen):
        st.error("Word does not exist in English")
        return
    
    
    st.session_state.textInputList[st.session_state.attempt_count-1]=word_chosen
    word = st.session_state.word
    print(word_chosen)
    match = [0,0,0,0,0]
    for i in range(5):
        if word_chosen[i] == st.session_state.word[i]:
            match[i] = 2
            word = word[:i]+" "+word[i+1:]
        #elif word_chosen[i] in st.session_state.word:
        #    match[i] = 1
    for i in range(5):
        if match[i]!=2:
            if word_chosen[i] in word:
                match[i] = 1
                word = word.replace(word_chosen[i]," ",1)   
    print(match)
    st.session_state.match[st.session_state.attempt_count-1] = match
    st.session_state.attempt_count+=1
    if sum(match) == 10:
        st.success("Hurray! You won")
        st.session_state.status = True
        st.balloons() 

    


def main():
    init_state()
    if st.button("Reset Game"):
        reset_state()
    col1, col2, col3 = st.columns(3)

    with col1:
        st.text_input("Word 1", value = st.session_state.textInputList[0],key="word_1", max_chars=5, on_change=check_answer, disabled=(st.session_state.attempt_count !=1 or st.session_state.status==True))
        st.text_input("Word 2", value = st.session_state.textInputList[1],key="word_2", max_chars=5, on_change=check_answer, disabled=(st.session_state.attempt_count !=2 or st.session_state.status==True))
        st.text_input("Word 3", value = st.session_state.textInputList[2],key="word_3",max_chars=5, on_change=check_answer, disabled=(st.session_state.attempt_count !=3 or st.session_state.status==True))
        st.text_input("Word 4", value = st.session_state.textInputList[3],key="word_4",max_chars=5, on_change=check_answer, disabled=(st.session_state.attempt_count !=4 or st.session_state.status==True))
        st.text_input("Word 5", value = st.session_state.textInputList[4],key="word_5",max_chars=5, on_change=check_answer, disabled=(st.session_state.attempt_count !=5 or st.session_state.status==True))
        st.text_input("Word 6", value = st.session_state.textInputList[5],key="word_6",max_chars=5, on_change=check_answer, disabled=(st.session_state.attempt_count !=6 or st.session_state.status==True))

    with col3:
        cols = st.columns(5)
        if st.session_state.attempt_count>6:
            st.badge("Game Over! You Lose", color="red")   
        for row in range (6):
            i = 0
            
            for col in cols:
                with col:
                    if st.session_state.match[row][i] == 2: 
                        
                        st.write(st.session_state.textInputList[row][i]) 
                        st.button("",key=str(row)+str(i),type="secondary",width=80,icon="🟩")  
                    elif st.session_state.match[row][i] == 1:
                        st.write(st.session_state.textInputList[row][i])
                        st.button("",key=str(row)+str(i),type="secondary",width=80,icon="🟨")
                    else:
                        if st.session_state.textInputList[row]!="":
                            st.write(st.session_state.textInputList[row][i])
                        else:
                            st.write("")    
                        st.button("",key=str(row)+str(i),type="secondary",width=80,icon="⬜")       
                i+=1

if __name__ == "__main__":
    main()
