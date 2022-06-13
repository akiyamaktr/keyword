import streamlit as st
import kw

def main():
  st.title("Keyword")  
  with st.form("my_form"):
    textarea_val=st.text_area("Texts",value="")
    submitted = st.form_submit_button("Submit")
  if submitted:
    texts=textarea_val.splitlines()
    lines=[]
    for text in texts:
      parts=[]
      result=kw.make_keyword_list(text, score=0)
      parts.append('"'+text+'"')
      parts.append('"'+result+'"')
      line="\t".join(parts)
      lines.append(line)
    text_dst="\n".join(lines)

    st.text_area("Result",value=text_dst)

if __name__ == "__main__":
  main()
