"""Public competition sources; no login, registration, or submissions."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json
from bs4 import BeautifulSoup
P=Path('source_snapshots');P.mkdir(exist_ok=True)
URLS={
 'lingbot26':'https://tianchi.aliyun.com/competition/entrance/532514/introduction?_lang=zh_CN',
 'openlet26':'https://tianchi.aliyun.com/competition/entrance/532515/introduction?_lang=zh_CN',
 'tianchi_events26':'https://tianchi.aliyun.com/competition/activeList?_lang=zh_CN',
 'qwen_challenge':'https://tianchi.aliyun.com/specials/promotion/Qwen',
 'ernie25':'https://baiduernieai.devpost.com/',
 'paddle_robot25':'https://aistudio.baidu.com/competition/detail/1421',
 'paddle_power23':'https://ai.baidu.com/support/news?action=detail&id=3013',
 'kdc_datasets':'https://kdc-doc.netlify.app/tianchi/cn/pages/datasets',
 'kdc_registration':'https://kdc-doc.netlify.app/tianchi/cn/pages/registration',
 'reali_datasets':'https://huggingface.co/datasets/LejuRobotics/kuavo_data_challenge_icra/raw/main/README.md',
 'kuavo_tianchi_tasks':'https://kdc-doc.netlify.app/tianchi/cn/pages/tasks',
 'reali_tasks':'https://kdc-doc.netlify.app/icra/en/pages/tasks',
 'ernie25_rules':'https://baiduernieai.devpost.com/rules',
 'paddle_rescue23':'https://segmentfault.com/a/1190000043422298',
 'openlet_community':'https://openlet.openatom.tech/',
 'paddle_factory_pdf':'https://www.up-tech.com/uploads/soft/220324/1-220324141I8.pdf',
}
def f(item):
 n,u=item
 try:
  r=requests.get(u,timeout=25);r.raise_for_status()
  if u.endswith('.pdf'):(P/(n+'.pdf')).write_bytes(r.content);t='PDF'
  else:
   (P/(n+'.html')).write_text(r.text,encoding='utf8')
   t=BeautifulSoup(r.text,'html.parser').get_text(' ',strip=True)
   (P/(n+'.text')).write_text(t,encoding='utf8')
  return dict(name=n,url=u,bytes=len(r.content),checked='2026-10-11',text_preview=t[:160])
 except Exception as e:return dict(name=n,url=u,error=str(e))
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=8) as pool:result=list(pool.map(f,URLS.items()))
 (P/'ecosystem_manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps(result,ensure_ascii=False,indent=2))
