"""Snapshot official public metadata for the backend/RoboColiseum update."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json
ROOT=Path(__file__).resolve().parent/'source_snapshots'/'backend_update'
ROOT.mkdir(parents=True,exist_ok=True)
URLS={
 'genie_readme':'https://raw.githubusercontent.com/AgibotTech/genie_sim/main/README.md',
 'genie_tree':'https://api.github.com/repos/AgibotTech/genie_sim/git/trees/main?recursive=1',
 'embodi_readme':'https://raw.githubusercontent.com/DexForce/EmbodiChain/main/README.md',
 'embodi_pyproject':'https://raw.githubusercontent.com/DexForce/EmbodiChain/main/pyproject.toml',
 'embodi_tree':'https://api.github.com/repos/DexForce/EmbodiChain/git/trees/main?recursive=1',
 'embodi_backends':'https://dexforce.github.io/EmbodiChain/main/api_reference/embodichain/embodichain.lab.sim.html',
 'robotwin_branches':'https://api.github.com/repos/RoboTwin-Platform/RoboTwin/branches?per_page=100',
 'robotwin_readme':'https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/main/README.md',
 'forge_original':'https://raw.githubusercontent.com/isaac-sim/IsaacGymEnvs/forge/docs/forge.md',
 'automate_original':'https://raw.githubusercontent.com/isaac-sim/IsaacGymEnvs/automate/docs/automate.md',
 'coliseum_site':'https://robocoliseum.ai/',
 'genie_benchmark_usage':'https://raw.githubusercontent.com/AgibotTech/genie_sim/main/source/geniesim_benchmark/USAGE.md',
 'coliseum_data_script':'https://raw.githubusercontent.com/AgibotTech/genie_sim/main/source/geniesim_benchmark/skills/robocoliseum/challenge-download-datasets/scripts/download_dataset.sh',
 'genie_ros_pyproject':'https://raw.githubusercontent.com/AgibotTech/genie_sim/main/source/geniesim_ros/pyproject.toml',
 'genie_newton_launcher':'https://raw.githubusercontent.com/AgibotTech/genie_sim/main/source/geniesim_ros/src/ros_ws/src/genie_sim_bringup/config/launcher_newton_mjwarp.yaml',
 'genie_isaac_newton_launcher':'https://raw.githubusercontent.com/AgibotTech/genie_sim/main/source/geniesim_ros/src/ros_ws/src/genie_sim_bringup/config/launcher_ovrtx_isaac_newton.yaml',
 'embodi_physics':'https://raw.githubusercontent.com/DexForce/EmbodiChain/main/docs/source/overview/sim/sim_manager/physics/index.md',
 'embodi_newton':'https://raw.githubusercontent.com/DexForce/EmbodiChain/main/docs/source/overview/sim/sim_manager/physics/newton.md',
 'robotwin_isaac_readme':'https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/IsaacLab-Arena/README.md',
 'robotwin_isaac_tree':'https://api.github.com/repos/RoboTwin-Platform/RoboTwin/git/trees/IsaacLab-Arena?recursive=1',
 'forge_readme':'https://raw.githubusercontent.com/NVIDIA-Omniverse/IsaacGymEnvs/forge/README.md',
}
def get(item):
 key,url=item
 try:
  r=requests.get(url,timeout=40);r.raise_for_status()
  (ROOT/(key+'.txt')).write_text(r.text,encoding='utf8')
  return dict(key=key,url=url,status=r.status_code,bytes=len(r.content))
 except Exception as e:return dict(key=key,url=url,error=str(e))
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=8) as pool:result=list(pool.map(get,URLS.items()))
 (ROOT/'manifest.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf8')
 print(json.dumps(result,ensure_ascii=True))
