from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json
from bs4 import BeautifulSoup
P=Path('source_snapshots')
urls={
 'robotwin_readme':'https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/main/README.md',
 'robotwin_tasklist':'https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/main/task_config/_task_list.yml',
 'robotwin_config':'https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/main/task_config/demo_randomized.yml',
 'robodojo_readme':'https://raw.githubusercontent.com/RoboDojo-Benchmark/RoboDojo/main/README.md',
 'embodichain_readme':'https://raw.githubusercontent.com/DexForce/EmbodiChain/main/embodichain_tasks/README.md',
 'ebim_competition':'https://ebim-benchmark.github.io/competition.html',
 'iros25':'https://www.iros25.org/Competitions.html',
 'agibot_challenge':'https://agibot-world.com/challenge',
 'agibot2026':'https://agibot-world.com/challenge2026',
 'worldmodels':'https://physical-world-models.github.io/IROS2026/',
}
def f(pair):
 n,u=pair
 try:
  r=requests.get(u,timeout=25);r.raise_for_status();(P/(n+'.txt')).write_text(r.text,encoding='utf8')
  s=BeautifulSoup(r.text,'html.parser').get_text(' ',strip=True) if '<html' in r.text.lower() else r.text
  return n,len(r.content),s[:600] if n not in ['robotwin_tasklist'] else s
 except Exception as e:return n,str(e)
with ThreadPoolExecutor(max_workers=8) as ex:
 for a in ex.map(f,urls.items()):print(a)
s=BeautifulSoup((P/'robodojo_paper.txt').read_text(encoding='utf8'),'html.parser')
for id in ['A9','S3.SS2']:
 sec=s.find(id=id)
 if sec:
  (P/(id+'.txt')).write_text(sec.get_text(' ',strip=True),encoding='utf8')
  print(id,[(h.name,h.get_text(' ',strip=True)) for h in sec.select('h3,h4,h5,h6')])
