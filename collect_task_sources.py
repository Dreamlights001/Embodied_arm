"""Download public first-party task manifests for a dated, reproducible inventory."""
import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
ROOT=Path(__file__).resolve().parent
DEST=ROOT/'source_snapshots'
DEST.mkdir(exist_ok=True)
URLS={
 'robodojo_paper':'https://arxiv.org/html/2607.04434v1',
 'robodojo_tree':'https://api.github.com/repos/RoboDojo-Benchmark/RoboDojo/git/trees/main?recursive=1',
 'robotwin_tree':'https://api.github.com/repos/RoboTwin-Platform/RoboTwin/git/trees/main?recursive=1',
 'libero_tasks':'https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/libero_suite_task_map.py',
 'rlbench_tree':'https://api.github.com/repos/stepjam/RLBench/git/trees/master?recursive=1',
 'embodichain_tree':'https://api.github.com/repos/DexForce/EmbodiChain/git/trees/main?recursive=1',
 'ebim_competition':'https://ebim-benchmark.github.io/competition/',
 'worldarena':'https://iros2026challenge.world-arena.ai/',
 'yizhi':'https://kw.beijing.gov.cn/xwdt/kcyx/kcyxkchd/202606/t20260629_4733719.html',
}
def fetch(pair):
 name,url=pair
 try:
  r=requests.get(url,timeout=40);r.raise_for_status()
  (DEST/(name+('.json' if '_tree' in name else '.txt'))).write_text(r.text,encoding='utf-8')
  return dict(name=name,url=url,status=r.status_code,bytes=len(r.content),checked='2026-10-11')
 except Exception as e:return dict(name=name,url=url,error=str(e))
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(fetch,URLS.items()))
 (DEST/'manifest.json').write_text(json.dumps(results,indent=2,ensure_ascii=False),encoding='utf-8')
 print(json.dumps(results,ensure_ascii=False,indent=2))
