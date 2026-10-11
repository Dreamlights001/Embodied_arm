"""Recover primary dataset release pages; only public text, never dataset payloads."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from bs4 import BeautifulSoup
import json,re,requests
ROOT=Path('source_snapshots/datasets');ROOT.mkdir(exist_ok=True)
URLS={
 'fmb_dataset':'https://functional-manipulation-benchmark.github.io/dataset/index.html',
 'automate_data':'https://raw.githubusercontent.com/isaac-sim/IsaacGymEnvs/automate/docs/automate.md',
 'maniskill_demos':'https://maniskill.readthedocs.io/en/latest/user_guide/datasets/demos.html',
 'robocasa_datasets':'https://raw.githubusercontent.com/robocasa/robocasa/main/docs/datasets/using_datasets.md',
 'mimicgen_registry':'https://raw.githubusercontent.com/NVlabs/mimicgen/main/mimicgen/__init__.py',
 'roco_download':'https://raw.githubusercontent.com/rocochallenge/roco_dataset_devkit/main/scripts/download_dataset.py',
 'libero_download':'https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/utils/download_utils.py',
 'libero_hf':'https://huggingface.co/api/datasets/yifengzhu-hf/LIBERO-datasets/tree/main',
 'libero_registry':'https://raw.githubusercontent.com/Lifelong-Robot-Learning/LIBERO/master/libero/libero/benchmark/__init__.py',
 'fmb':'https://functional-manipulation-benchmark.github.io/',
 'furniture':'https://clvrai.github.io/furniture-bench/docs/tutorials/dataset.html',
 'automate':'https://bingjietang718.github.io/automate/',
 'roco':'https://raw.githubusercontent.com/rocochallenge/roco_dataset_devkit/main/README.md',
 'maniskill':'https://maniskill.readthedocs.io/en/latest/user_guide/datasets/datasets.html',
 'calvin':'https://raw.githubusercontent.com/mees/calvin/main/dataset/README.md',
 'behavior':'https://raw.githubusercontent.com/StanfordVL/BEHAVIOR-1K/main/docs/challenge/data.md',
 'behavior_datasets':'https://raw.githubusercontent.com/StanfordVL/BEHAVIOR-1K/main/docs/challenge/datasets.md',
 'robocasa':'https://robocasa.ai/docs/use_cases/downloading_datasets.html',
 'robotwin':'https://robotwin-platform.github.io/doc/usage/datasets.html',
 'robodojo':'https://robodojo-benchmark.com/doc/usage/install-and-download/',
 'duobench':'https://raw.githubusercontent.com/RobotControlStack/duobench/master/README.md',
 'mimicgen':'https://raw.githubusercontent.com/NVlabs/mimicgen/main/docs/tutorials/datasets.md',
 'skillgen':'https://skillgen.github.io/',
 'agibot':'https://raw.githubusercontent.com/OpenDriveLab/AgiBot-World/main/README.md',
 'openlet':'https://openlet.openatom.tech/',
 'reali':'https://huggingface.co/datasets/LejuRobotics/kuavo_data_challenge_icra/raw/main/README.md',
}
def fetch(item):
 key,url=item
 try:
  r=requests.get(url,timeout=18)
  if r.status_code!=200:return dict(key=key,url=url,status=r.status_code)
  (ROOT/(key+'.txt')).write_text(r.text,encoding='utf8')
  if 'text/html' in r.headers.get('content-type',''):
   bs=BeautifulSoup(r.text,'html.parser');body=bs.select_one('main,article,.wy-nav-content,.content') or bs
   content=body.get_text(' ',strip=True)
   links=[dict(label=a.get_text(' ',strip=True)[:100],url=a.get('href')) for a in body.find_all('a',href=True)
          if re.search(r'huggingface|drive.google|download|dataset|box.com|zenodo|modelscope',str(a),re.I)]
  else:
   content=r.text
   links=[dict(label=m.group(1),url=m.group(2)) for m in re.finditer(r'\[([^\]]+)\]\((https?://[^\s)]+)\)',content)]
  excerpts=[content[max(0,m.start()-50):m.start()+270] for m in re.finditer('dataset|download|demonstration|libero_10|LIBERO.long',content,re.I)][:12]
  return dict(key=key,url=url,status=200,links=links[:35],excerpts=excerpts)
 except requests.RequestException as e:return dict(key=key,url=url,error=type(e).__name__)
with ThreadPoolExecutor(max_workers=10) as pool: data=list(pool.map(fetch,URLS.items()))
(ROOT/'manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(data,ensure_ascii=True,indent=2))
