import streamlit as st
import json
from urllib import request
import time
import kw


def main():
  with st.form("my_form"):
    textarea_val=st.text_area("Texts",value="物を2枚の刃で挟んで切る道具。切符などに穴をあけたり切り込みを入れたりする道具。パンチ。カニ・エビなどの節足動物の脚の、物をはさむような形に発達した部分。これをもつ脚を鉗脚という。\n体長40～60センチのものが多く、一般に耳が長く、前肢は短く、後肢は長い。上唇は縦に裂け、上あごの門歯は二対ある。品種は多く、肉は食用、毛皮は襟巻きなどにし、医学実験用・愛玩用ともする。")
    submitted = st.form_submit_button("Submit")
  if submitted:
    texts=textarea_val.splitlines()
    lines=[]
    for text in texts:
      parts=[]
      result=kw.make_keyword_list(text)
      parts.append('"'+text+'"')
      parts.append('"'+result+'"')
      line="\t".join(parts)
      lines.append(line)
    text_dst="\n".join(lines)



      
    st.text_area("Result",value=text_dst)



if __name__ == "__main__":
  main()
