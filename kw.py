
import json
from urllib import request
import time
import itertools


def main():
  text="日本の音楽ユニット。中田ヤスタカがプロデュースする広島県出身の3人組テクノポップユニットである。女性アイドルグループとしては珍しく長い下積みを経て、2007年から2008年にかけてブレイク。以降も長く人気を保つ女性アイドルグループである。独特の音楽性やダンス、舞台演出等に特徴がある。"
  result=make_keyword_list(text)
  print(result)

def make_keyword_list(text,min_score=50,num_lines=3,num_words=3):
  # キーワードw個を最大l組作る。
  # min_score scoreがこれ以上のものを対象とする。
  # num_lines 組数
  # num_words 個数

  str_json = get_json(text)

  obj=json.loads(str_json)
  phrases=obj["result"]["phrases"]
  phrases=[x for x in phrases if x["score"]>=min_score]
  
  print(phrases)
  cs=list(itertools.combinations(phrases,num_words))
  print(cs)
  recs=[]
  for c in cs:
    s=0
    for x in c:
      s+=x["score"]
    recs.append({"sum":s,"data":c})
  recs = sorted(recs, key = lambda x : x["sum"], reverse=True)
  print(recs)

  recs=recs[0:num_lines]
  # word,word,word\nword,word,wordという文字列を生成。
  # rec={'sum': 248, 'data': ({'score': 100, 'text': '中田ヤスタカ'}, {'score': 79, 'text': '長い下積み'}, {'score': 69, 'text': 'ブレイク'})}
  lines = []
  for rec in recs[0:num_lines]:
    parts = []
    for w in rec["data"][0:num_words]:
      parts.append(w["text"])
    lines.append(",".join(parts))
  result = "\n".join(lines)
  return result


def get_json(text):
  URL = "https://jlp.yahooapis.jp/KeyphraseService/V2/extract"
  appid="dj00aiZpPW9mUXI0NFRYZktLMCZzPWNvbnN1bWVyc2VjcmV0Jng9YTA-"
  headers = {
    "Content-Type": "application/json",
    "User-Agent": f"Yahoo AppID: {appid}",
  }
  param_dic = {
    "id": int(time.time()%1000*1000),
    "jsonrpc" : "2.0",
    "method" : "jlp.keyphraseservice.extract",
    "params" : {
      "q" : text
    }
  }
  params = json.dumps(param_dic).encode()
  req = request.Request(URL, params, headers)
  with request.urlopen(req) as res:
    body = res.read()
  return body.decode()

if __name__ == "__main__":
  main()
