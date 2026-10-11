from collect_simulator_sources import f,P
from concurrent.futures import ThreadPoolExecutor
import json
URLS={
'calvin_env_requirements':'https://raw.githubusercontent.com/mees/calvin_env/main/requirements.txt',
'omnigibson_install_current':'https://raw.githubusercontent.com/StanfordVL/BEHAVIOR-1K/main/docs/getting_started/installation.md',
'omnigibson_setup':'https://raw.githubusercontent.com/StanfordVL/BEHAVIOR-1K/v3.9.3/setup.sh',
'kuavo_ros_readme':'https://raw.githubusercontent.com/LejuRobotics/kuavo-ros-opensource/opensource/kuavo-data-challenge/README.md',
'kuavo_baseline_readme':'https://raw.githubusercontent.com/LejuRobotics/kuavo_data_challenge/main/README.md',
'mimicgen_deps':'https://raw.githubusercontent.com/NVlabs/mimicgen/main/docs/introduction/installation.md',
'fabrica_cmake':'https://raw.githubusercontent.com/yunshengtian/Fabrica/main/simulation/CMakeLists.txt',
'ariac_startup':'https://pages.nist.gov/ARIAC_docs/en/stable/getting_started/startup.html',
'robotwin_scripts':'https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/main/scripts/requirements.txt',
'calvin_env_setup':'https://raw.githubusercontent.com/mees/calvin_env/main/setup.py',
'robosuite_140':'https://raw.githubusercontent.com/ARISE-Initiative/robosuite/v1.4.0/setup.py',
'mimicgen_install':'https://raw.githubusercontent.com/NVlabs/mimicgen/main/docs/tutorials/getting_started.md',
'fabrica_readme':'https://raw.githubusercontent.com/yunshengtian/Fabrica/main/README.md',
'fabrica_sim':'https://raw.githubusercontent.com/yunshengtian/Fabrica/main/simulation/setup.py',
'duobench_pyproject':'https://raw.githubusercontent.com/RobotControlStack/duobench/master/pyproject.toml',
'omnigibson_pyproject':'https://raw.githubusercontent.com/StanfordVL/BEHAVIOR-1K/main/OmniGibson/pyproject.toml',
'omnigibson_install':'https://raw.githubusercontent.com/StanfordVL/BEHAVIOR-1K/main/docs/getting_started/install.md',
'industreal_install':'https://raw.githubusercontent.com/isaac-sim/IsaacGymEnvs/main/docs/industreal.md',
'factory_install':'https://raw.githubusercontent.com/isaac-sim/IsaacGymEnvs/main/docs/factory.md',
'umi_readme':'https://raw.githubusercontent.com/real-stanford/universal_manipulation_interface/main/README.md',
'egoverse_readme':'https://raw.githubusercontent.com/GaTech-RL2/EgoVerse/main/README.md',
'kuavo_datasets':'https://kdc-doc.netlify.app/tianchi/cn/pages/datasets',
'kuavo_install':'https://kdc-doc.netlify.app/tianchi/cn/pages/installation',
'skillgen_project':'https://skillgen.github.io/',
'embodichain_install':'https://dexforce.github.io/EmbodiChain/main/quick_start/install.html',
'rlbench_domainrandom':'https://raw.githubusercontent.com/stepjam/RLBench/master/examples/domain_randomization.py',
}
with ThreadPoolExecutor(max_workers=10) as p: out=list(p.map(f,[(k,[u]) for k,u in URLS.items()]))
(P/'extra_manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(out,ensure_ascii=False,indent=2))
