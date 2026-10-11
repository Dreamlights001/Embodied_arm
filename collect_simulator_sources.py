"""Public upstream installation/configuration snapshots for simulator versions."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json,re
P=Path('source_snapshots/simulators');P.mkdir(parents=True,exist_ok=True)
REPOS={
 'furniture':'clvrai/furniture-bench', 'ramp':'applied-ai-lab/ramp',
 'roco':'rocochallenge/gearboxAssembly','assemblybench':'merlresearch/AssemblyBench',
 'robotwin':'RoboTwin-Platform/RoboTwin','robofactory':'MARS-EAI/RoboFactory',
 'robosuite':'ARISE-Initiative/robosuite','maniskill':'haosulab/ManiSkill',
 'rlbench':'stepjam/RLBench','calvin':'mees/calvin','libero':'Lifelong-Robot-Learning/LIBERO',
 'liberoplus':'sylvestf/LIBERO-plus','liberopro':'Zxy-MLlab/LIBERO-PRO',
 'vlabench':'OpenMOSS/VLABench','bigym':'chernyadev/bigym',
 'behavior':'StanfordVL/BEHAVIOR-1K','robocasa':'robocasa/robocasa',
 'robolab':'NVLabs/RoboLab','mimicgen':'NVlabs/mimicgen','dexmimicgen':'NVlabs/dexmimicgen',
 'robodojo':'RoboDojo-Benchmark/RoboDojo','embodichain':'DexForce/EmbodiChain',
 'geniesim':'AgibotTech/genie_sim',
}
FILES=['README.md','requirements.txt','pyproject.toml','setup.py','environment.yml']
EXTRA={
 'IsaacLab_2.2.1_README':'https://raw.githubusercontent.com/isaac-sim/IsaacLab/v2.2.1/README.md',
 'IsaacLab_2.2_install':'https://isaac-sim.github.io/IsaacLab/v2.2.1/source/setup/installation/binaries_installation.html',
 'kuavo_sim_setup':'https://kdc-doc.netlify.app/tianchi/cn/pages/setup',
 'reali_sim_setup':'https://kdc-doc.netlify.app/icra/en/pages/setup',
 'fabrica_project':'https://fabrica.csail.mit.edu/',
 'duobench_project':'https://duobench.github.io/',
 'workbench_project':'https://workbenchmark.github.io/',
 'ebim_protocol':'https://ebim-benchmark.github.io/competition.html',
 'roco_iros':'https://rocochallenge.github.io/RoCo-IROS2026/faq.html',
 'ariac_install':'https://pages.nist.gov/ARIAC_docs/en/stable/getting_started/installation.html',
}
def f(item):
 key,urls=item
 for url in urls:
  try:
   r=requests.get(url,timeout=18)
   if r.status_code!=200:continue
   (P/(key+'.txt')).write_text(r.text,encoding='utf8')
   found=[l.strip()[:280] for l in r.text.splitlines() if re.search(r'mujoco|sapien|isaac|bullet|coppelia|pyrep|gazebo|physx|robosuite|real.robot|sim.to.real',l,re.I)]
   return dict(key=key,url=url,bytes=len(r.content),version_lines=found[:30])
  except requests.RequestException:pass
 return dict(key=key,error='No public file recovered')
if __name__=='__main__':
 todo=[(k+'_'+file.replace('.','_'),[f'https://raw.githubusercontent.com/{repo}/{branch}/{file}' for branch in ['main','master']]) for k,repo in REPOS.items() for file in FILES]
 todo += [(k,[u]) for k,u in EXTRA.items()]
 with ThreadPoolExecutor(max_workers=12) as pool:out=list(pool.map(f,todo))
 (P/'manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps([x for x in out if x.get('version_lines')],ensure_ascii=False,indent=2))
