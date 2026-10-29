"""Audited backend/version and real-platform metadata; never infer task-level real support.

Versions describe recovered upstream installation instructions on 2026-10-11,
not a claim that we installed or evaluated every environment.
"""
from copy import deepcopy
from pathlib import Path
import json

MANIFEST = json.loads((Path(__file__).resolve().parent / 'simulator_sources.json').read_text(encoding='utf8'))

def ref(key):
    return MANIFEST[key]

UPDATE='https://raw.githubusercontent.com/AgibotTech/genie_sim/main/'
TWIN_ARENA='https://raw.githubusercontent.com/RoboTwin-Platform/RoboTwin/IsaacLab-Arena/'
EMBODI='https://raw.githubusercontent.com/DexForce/EmbodiChain/main/'

def sim(engine, version, framework='', scope='公开安装配置', source='', status='固定版本'):
    return dict(engine=engine, version=version, framework=framework, scope=scope,
                source=source, version_status=status)

SUPPORT = {}
def entry(ids, sims=(), real=(), scope='未核实官方实机执行支持', transfer='未核实',
          note='', sources=(), state='有公开仿真配置'):
    for id in ids.split('|'):
        SUPPORT[id] = dict(simulators=list(sims), real_platforms=list(real),
            real_support=bool(real), real_scope=scope, sim2real=transfer,
            platform_note=note, platform_sources=list(sources), simulator_state=state)

LAB = sim('Isaac Sim', '5.0.0', 'Isaac Lab 2.2.1', 'Isaac Lab v2.2.1 移植；不是原论文运行版本',
          ref('IsaacLab_2.2.1_README'))
GYM = sim('Isaac Gym', 'Preview 4', 'IsaacGymEnvs / PhysX',
          '公开 IsaacGymEnvs 安装说明；原论文 Preview 版本未另行核实',
          'https://github.com/isaac-sim/IsaacGymEnvs/blob/main/README.md')
entry('factory', [GYM, LAB], note='Isaac Gym 与 Isaac Sim 是不同软件栈；不能把移植版当成原论文依赖。')
entry('industreal', [GYM], ['Franka Panda'],
      '论文与 IndustRealLib 实机部署', '已展示', '插装等已展示 sim2real；不表示任意新零件无需适配。',
      ['https://github.com/NVlabs/industreallib', 'https://arxiv.org/abs/2305.17110', ref('industreal_install')])
entry('forge|automate', [LAB], ['Franka'], '论文装配实机实验', '已展示',
      '此处固定版本为公开 Isaac Lab 移植配置；原论文仿真软件版本另见论文。',
      ['https://isaac-sim.github.io/IsaacLab/main/source/overview/environments',
       'https://arxiv.org/abs/2408.04587', 'https://bingjietang718.github.io/automate/'])
SUPPORT['forge']['simulators'].insert(0,sim('Isaac Gym','论文未披露 Preview 小版本','Factory / FORGE 原论文实现',
 '原论文训练后端；与 Isaac Lab 移植版区分','https://arxiv.org/html/2408.04587v1','未披露'))
SUPPORT['automate']['simulators'].insert(0,sim('Isaac Gym','Preview 4（IsaacGymEnvs 安装栈）','AutoMate 原版 / automate 分支',
 '原始公开代码；与 Isaac Lab 移植版区分','https://github.com/isaac-sim/IsaacGymEnvs/blob/automate/docs/automate.md'))
SUPPORT['forge']['platform_note']='原论文训练使用 Isaac Gym，Preview 小版本未披露；公开 Isaac Lab 移植配置使用 Isaac Sim 5.0.0。两者分别记录，力控 / 接触参数不能默认一致。'
SUPPORT['automate']['platform_note']='原始 automate 分支是 Isaac Gym / IsaacGymEnvs；公开 Isaac Lab 移植版是 Isaac Sim 5.0.0 / Isaac Lab 2.2.1。几何资产可复用不代表原版与移植版指标可直接比较。'
entry('nist', real=['按协议配置的装配机器人'], scope='真实装配任务板与评测协议',
      note='不绑定唯一机械臂型号；没有核实本条协议的官方原生仿真器。', state='未核实原生仿真器')
entry('fmb', real=['Franka'], scope='真实装配演示数据与实机评测',
      note='ManiSkill 中的 FMB 复现环境是另一个实现；不据此给原始真实数据集补填仿真版本。', state='原始资源为实机')
entry('furniture', [sim('Isaac Gym', 'Preview 4', 'FurnitureSim', source=
      'https://clvrai.github.io/furniture-bench/docs/getting_started/installing_furniture_sim.html')],
      ['Franka Panda / FR3'], 'FurnitureBench 真实采集、控制及评测', '迁移接口 / 平行环境',
      '同时有 FurnitureSim 与实机环境，不将全部家具任务标成已展示 sim2real。',
      ['https://clvrai.github.io/furniture-bench/docs/getting_started/installing_furniture_bench.html'])
entry('ramp', real=['Franka Panda'], scope='真实装配执行代码',
      note='已核实真实 ROS / Franka 工具链；README 未明确固定数字孪生的仿真器及版本。ROS Noetic 不是仿真器。',
      sources=[ref('ramp_README_md')], state='仿真器 / 版本待核对')
entry('fabrica', [sim('RedMax', '未固定发布版本', '仓库内 simulation', '几何与接触规划', ref('fabrica_cmake'), '未固定'),
      sim('Isaac Gym', 'Preview 4', '仓库内 IsaacGymEnvs', '残差策略学习', ref('fabrica_readme'))],
      ['Franka Panda'], '公开 Frankapy 实机运行入口', '已展示',
      '实际公开实机入口为单台 Panda；规划中的双臂配置不等于每个实机实验均双臂。Blender 仅为渲染器。',
      [ref('fabrica_readme')])
entry('roco', [sim('Isaac Sim', '5.1.0', 'Isaac Lab 2.3.0（子模块）', source=ref('roco_README_md'))],
      ['Galaxea R1'], '仿真与真实齿轮箱装配数据 / 流程', '迁移接口 / 平行环境',
      '此 R1 是 Galaxea 的平台；不能与宇树 R1-7A 混同。', [ref('roco_README_md')])
entry('roco-iros', real=['DexMate / Sharpa（具体型号以赛方为准）'], scope='IROS 2026 线下实机赛',
      transfer='赛制设仿真 / 真机阶段', note='FAQ 确认先仿真后线下；没有核实本届仿真器与固定版本，不能套用 AAAI 齿轮箱配置。',
      sources=[ref('roco_iros')], state='仿真器 / 版本待核对')
entry('workbench', [sim('MuJoCo', '未披露固定版本', 'LIBERO 相关环境', source=ref('workbench_project'), status='未披露')],
      ['Franka Panda / UR 系列（页面示例）'], '页面披露的部分层级实机实验',
      note='项目仍含 draft / TBD；实机覆盖有层级限制，不能推成所有任务可部署。', sources=[ref('workbench_project')])
entry('assemblybench', note='已公开依赖主要是轨迹预测与几何学习；本次未核实物理可行性仿真的引擎与版本。零件轨迹不是机械臂动作。',
      sources=[ref('assemblybench_pyproject_toml')], state='物理仿真器 / 版本待核对')
entry('ariac', [sim('Gazebo', 'Harmonic（2025 工具链）', 'ROS 2 Jazzy / ARIAC 2025',
      source='https://pages.nist.gov/ARIAC_docs/en/latest/pages/startup.html', status='版本系列')],
      note='2025 工具链与往届 Gazebo Classic / ROS 版本不同；本条是仿真赛，不标真实平台。')
entry('hail', real=['Flexiv Rizon 4'], scope='真实协作臂基准及 MR 示范采集',
      note='本次未取得完整公开仿真安装配置；不补填引擎版本。', state='未核实原生仿真器')
entry('robotwin', [sim('SAPIEN', '3.0.0b1', 'RoboTwin 2.0', source=ref('robotwin_scripts'))],
      ['COBOT-Magic 双臂'], '论文 4 项实机实验；不是全部 50 项', '已展示',
      '论文验证 Stack Bowls、Handover Block、Pick Bottle、Click Bell。任务表仅对明确对应标识的 handover_block / click_bell 下推实机标记；其他名称 / 变体待对照。其他 Isaac Lab 分支不自动算作这 50 项的已验证后端。',
      ['https://arxiv.org/html/2506.18088v1#S4.SS4'])
SUPPORT['robotwin']['simulators'].append(sim('Isaac Sim','5.1.0','IsaacLab-Arena；Isaac Lab / Arena 子模块版本需保存 commit',
 '官方 IsaacLab-Arena 分支：数据回放 / 转换与策略评测；逐任务覆盖按分支配置核对',TWIN_ARENA+'script/_install.sh'))
SUPPORT['robotwin']['platform_note']='主分支为 SAPIEN；官方 IsaacLab-Arena 分支明确提供 Isaac Sim 5.1.0 上的数据回放 / 转换与策略评测。未核实其完整 50 项覆盖，任务表暂按主分支登记。论文实机仅对明确同名 handover_block / click_bell 下推；双臂平台不等于每任务都已迁移。'
SUPPORT['robotwin']['platform_sources'].append(TWIN_ARENA+'README.md')
entry('robofactory', [sim('SAPIEN', '由 ManiSkill 依赖解析；本项目未固定', 'ManiSkill（未锁版本）',
      source=ref('robofactory_setup_py'), status='未固定')], note='setup.py 只声明 mani_skill；注释中的开发轮子版本不是实际锁定依赖。')
entry('robosuite', [sim('MuJoCo', '>=3.3.0,<3.10', 'robosuite 1.5 系列（当前分支）',
      source=ref('robosuite_setup_py'), status='版本范围')])
entry('maniskill', [sim('SAPIEN', 'Linux >=3.0.3；Windows >=3.0.0.b1；macOS >=3.0.2', 'ManiSkill 3',
      source=ref('maniskill_setup_py'), status='版本范围')], note='依赖下限随操作系统不同；需要保存实际安装结果才能复现。')
entry('rlbench', [sim('CoppeliaSim', '4.1.0', 'PyRep / RLBench 1.2.0', source=ref('rlbench_README_md'))],
      transfer='仅域随机化接口', note='官方 Sim-to-Real 小节提供视觉域随机化；未据此确认真机执行后端或任务实机验证。')
entry('calvin', [sim('PyBullet', '未固定', 'calvin_env', source=ref('calvin_env_requirements'), status='未固定')])
LIBERO = [sim('MuJoCo', '>=2.3.0；未锁精确版本', 'robosuite ==1.4.0',
          '任务环境要求 1.4.0；MuJoCo 下限来自该标签的 setup.py', ref('robosuite_140'), '版本范围')]
entry('libero-industry', [sim('MuJoCo','精确版本未核实','robosuite 1.4.0（标准评测）；1.5.2（部署环境）',source='https://github.com/IAIE-PhysicalAI/LIBERO-Industry',status='未核实')],
      ['AUBO-i5H / CTAG2F90D'], '实机动态到静态工站；双臂仍开发中', '仿真与实机联合训练评测',
      '标准 Franka 仿真与 AUBO 部署环境版本不同；论文实机只覆盖 D2S。', ['https://arxiv.org/html/2610.16782','https://github.com/IAIE-PhysicalAI/LIBERO-Industry'])
for rid, key in [('libero','libero_requirements_txt'),('liberoplus','liberoplus_requirements_txt'),('liberopro','liberopro_requirements_txt')]:
    entry(rid, LIBERO, sources=[ref(key)], note='robosuite 版本不是 MuJoCo 版本；也不套用 robosuite 1.5 的新依赖范围。')
entry('liberovpro', [sim('MuJoCo', '具体版本未披露 / 未核实', 'LIBERO 基底', '基底来自论文；未取得可核验锁文件',
      'https://arxiv.org/abs/2609.24350', '未披露')])
entry('vlabench', [sim('MuJoCo', '3.2.2', 'dm_control；mujoco-mjx ==3.2.2', source=ref('vlabench_requirements_txt'))],
      note='README 将 real-device deployment 列作 Preview；待发布功能不等于已公开真机执行能力。')
entry('bigym', [sim('MuJoCo', '3.1.5', 'BiGym', source=ref('bigym_setup_py'))])
entry('behavior', [sim('Isaac Sim', '具体版本未在已取得安装页固定', 'OmniGibson / BEHAVIOR-1K；安装页建议 v3.9.3',
      source=ref('omnigibson_install_current'), status='未固定')], note='v3.9.3 是仓库标签，不能填作 Isaac Sim 版本；比赛提交镜像需单独核对。')
entry('robocasa', [sim('MuJoCo', '3.3.1', 'robosuite / RoboCasa 当前公开仓库', source=ref('robocasa_setup_py'))],
      ['Franka Panda（DROID 配置）'], '论文 4 项真实厨房任务', '已展示（Sim-and-Real 联合训练）',
      '4 项：CloseElectricKettleLid、PickPlaceToasterOvenToCounter、PickPlaceCounterToCabinet、PlaceOnDishRack。使用真实数据联合训练，不是纯仿真训练的零样本迁移；版本为检索日公开仓库配置。',
      ['https://arxiv.org/html/2603.04356v1#S4.SS5'])
entry('robolab', [sim('Isaac Sim', '5.0.0', 'Isaac Lab 2.2.0', 'isaac50 可选配置（默认）', ref('robolab_pyproject_toml')),
      sim('Isaac Sim', '5.1.0', 'Isaac Lab 2.3.2.post1', 'isaac51 可选配置', ref('robolab_pyproject_toml'))],
      note='两套配置互斥；PhysX 接触差异会影响结果，应分环境复现。')
entry('mimicgen', [sim('MuJoCo', '2.3.2', 'robosuite 1.4.1 / 官方测试 commit', source=ref('mimicgen_deps'))],
      note='官方当前示例不支持 robosuite 1.5+；生成方法可移植不等于仓库已支持全部仿真器。')
entry('dexmimicgen', [sim('MuJoCo', '仓库未固定', 'robosuite Git 源码', '公开环境实现', ref('dexmimicgen_README_md'), '未固定'),
      sim('MuJoCo', '论文配置未核实；BiGym 当前依赖 3.1.5', 'BiGym', '项目页展示的数据分支，不能套作 robosuite 分支依赖',
      'https://dexmimicgen.github.io/', '分支版本')], ['Fourier GR1 + Inspire 灵巧手'],
      '项目展示真实实验', '已展示 Real2Sim2Real', '真实 Can Sorting 采用灵巧手；不能当成夹爪平台的直接复现结果。开放仓库以环境与数据为主。',
      ['https://dexmimicgen.github.io/', 'https://arxiv.org/abs/2410.24185'])
entry('skillmimicgen', [sim('MuJoCo', '具体版本未核实', 'robosuite 相关实验', source=ref('skillgen_project'), status='未核实')],
      ['论文实机机械臂（具体本体见实验设置）'], '项目实机策略示例', '已展示',
      '项目展示螺母装配的 zero-shot sim2real；不将所有技能标成均已迁移。', [ref('skillgen_project')])
for rid, robot in [('droid','Franka'),('bridge','WidowX'),('oxe','多种真实机器人；按子数据集区分'),
                   ('agibot','智元移动双臂；本体按数据包字段区分')]:
    entry(rid, real=[robot], scope='真实机器人采集数据', note='数据集的真实采集本体不等于提供实时部署驱动；本次未核实其原生配套仿真器。', state='真实数据；未核实原生仿真器')
entry('umi', real=['Franka / UR（适配配置依部署教程）'], scope='手持夹爪采集 + 真实机械臂部署',
      note='采集器不是机器人本体；真实平台标记依据机器人部署接口。', sources=[ref('umi_readme'),
      'https://github.com/real-stanford/universal_manipulation_interface/blob/main/umi/real_world/bimanual_umi_env.py'], state='采集 / 实机框架；未核实原生仿真器')
entry('egomimic', real=['ALOHA 双臂'], scope='人体 Aria 数据 + 真实双臂数据 / 策略评测', state='真实数据；未核实原生仿真器')
entry('egoverse', real=['Eva；ALOHA 数据转换接口'], scope='人体与真实机器人数据 / 训练接口',
      note='仓库区分 human 与 eva 本体；有机器人数据不等于全部人体轨迹可直接执行。', sources=[ref('egoverse_readme')], state='真实数据；未核实原生仿真器')
entry('ego4d|egoexo|egodex|taco|industreal-human', scope='人体采集；没有据此确认机器人执行平台',
      transfer='不适用', note='真实人体采集不标为真实机器人平台；相机 / ARKit / 渲染器不作为机器人仿真器。', state='不适用（人体数据）')
entry('duobench', [sim('MuJoCo', '未直接固定；依赖 rcs-core >=0.7.3', 'DuoBench 0.1.2 / RobotControlStack',
      source=ref('duobench_pyproject'), status='未固定')], ['Franka FR3 Duo'], '11 个仿真任务与 4 个真实任务（资源披露）',
      '迁移接口 / 平行环境', '本体固定双臂；11 项仿真不等于 11 项均有真机评测。',
      ['https://github.com/RobotControlStack/duobench'])
entry('robodojo', [sim('Isaac Sim', '5.1（补丁版本未固定）', 'Isaac Lab 2.3（补丁版本未固定）',
      source=ref('robodojo_README_md'), status='版本系列')], ['ARX X5','Piper X','Piper'],
      '42 项仿真与 18 项平台-任务实机评测', '仿真 / 实机分立评测',
      '仿真与实机任务集分开；不是逐任务配对的 sim2real 结果。', [ref('robodojo_README_md')])
entry('embodichain', [sim('DexSim Engine', '0.5.1rc1', 'EmbodiChain', source=ref('embodichain_pyproject_toml'))],
      transfer='README 宣称 Sim2Real；具体实机验证待核对',
      note='基于 DexSim，不填成 Isaac Sim 或 SAPIEN。本次未确认具体机器人部署驱动 / 实测本体，因此暂不打真实平台标记。',
      sources=[ref('embodichain_README_md')])
SUPPORT['embodichain']['simulators'][0].update(framework='EmbodiChain / DefaultPhysicsCfg；Constraint Dynamics',
 scope='default 后端；CPU / GPU 刚体、关节与原生约束',source=EMBODI+'pyproject.toml')
SUPPORT['embodichain']['simulators'].append(sim('Newton','上游版本未单独锁定；经 DexSim Engine 0.5.1rc1 集成',
 'EmbodiChain / NewtonPhysicsCfg；MJWarp、XPBD、VBD、DexUni 等求解配置',
 'newton 后端；刚体与 GPU 柔性体；求解器 / 设备 / 约束能力按官方矩阵核对',EMBODI+'docs/source/overview/sim/sim_manager/physics/newton.md','未固定'))
SUPPORT['embodichain']['platform_note']='官方公开 backend 标识为 default 与 newton，二者均经 DexSim 集成。Newton 的 MuJoCo-Warp 是求解器路径，不等于提供独立 MuJoCo 环境；相机渲染器另选。暂未核实具体实机驱动与本体，不标真实平台。'
SUPPORT['embodichain']['platform_sources'].append(EMBODI+'docs/source/overview/sim/sim_manager/physics/index.md')
EBIM = [sim('Isaac Sim', '未披露', 'EBiM', '官方任务卡列出；版本与开放包待核对', ref('ebim_protocol'), '未披露'),
        sim('MuJoCo', '未披露', 'EBiM', '官方任务卡列出；版本与开放包待核对', ref('ebim_protocol'), '未披露'),
        sim('Genesis', '未披露', 'EBiM', '总体技术栈；逐任务覆盖未确认', ref('ebim_protocol'), '未披露')]
entry('ebim', EBIM, ['Mobile FR3 Duo'], '跨实验室真实验证阶段', '赛制设迁移验证',
      '任务卡明确列出 Isaac Sim 与 MuJoCo；Genesis 在总体栈中列出，不下推为每项任务均支持。', [ref('ebim_protocol')])
GENIE = [sim('Isaac Sim', '5.1.0', 'Genie Sim 3.0', 'v3.0 公开环境', ref('geniesim_README_md'))]
entry('geniesim', GENIE+[sim('Newton', '未固定', 'Genie Sim RT Engine',
      '当前 README 声明 Newton-standalone / Isaac Sim Newton；覆盖需按场景核对', ref('geniesim_README_md'), '未固定')],
      ['AgiBot Genie G2'], '官方实机 / 迁移示例', '已展示（作者报告）',
      'Isaac Sim 6.0 仍列于 roadmap；不计入已核实 v3.0 支持版本。', [ref('geniesim_README_md')])
SUPPORT['geniesim']['simulators'][0].update(scope='Genie Sim 3.0 基础环境 / 当前独立 Benchmark 运行时')
SUPPORT['geniesim']['simulators'][1].update(framework='Genie Sim RT Engine / Newton standalone；MuJoCo-Warp、VBD、XPBD 等',
 scope='RT 的 Kit-free Newton 独立后端；不自动继承为 RoboColiseum 榜单评测后端',source=UPDATE+'source/geniesim_ros/src/ros_ws/src/genie_sim_bringup/config/launcher_newton_mjwarp.yaml')
SUPPORT['geniesim']['simulators'].append(sim('Isaac Sim','6.0（RT 实验启动配置）','Genie Sim RT Engine / Isaac Newton wrapper + MuJoCo-Warp',
 '官方 launcher 配置；刚体路径，非默认 3.0 / 榜单复现配置；README 同时仍列 roadmap',
 UPDATE+'source/geniesim_ros/src/ros_ws/src/genie_sim_bringup/config/launcher_ovrtx_isaac_newton.yaml','实验配置'))
SUPPORT['geniesim']['platform_note']='Isaac Sim PhysX、Newton standalone 与 Isaac Sim Newton wrapper 分别列出；后者有 6.0 实验 launcher，但 README 仍列 roadmap，不当作默认稳定版。RT 的 MuJoCo-Warp 是 Newton 求解器；依赖 mujoco<3.9.0 不等于独立 MuJoCo 榜单后端。Benchmark 当前直接驱动 Isaac Sim，与 RT 并行。'
SUPPORT['geniesim']['platform_sources'] += [UPDATE+'source/geniesim_benchmark/USAGE.md',UPDATE+'source/geniesim_ros/pyproject.toml']
entry('robocoliseum',GENIE,scope='四类在线榜单为仿真评测；未确认逐榜单真实执行平台',
 note='当前 geniesim_benchmark 直接驱动 Isaac Sim，与 RT Engine 的 Newton / 6.0 实验路径分立。平台另有 8 项 GenieSim-Sim2Real 对照实验；不将其自动套用为 28 项在线榜单任务均有真实验证。',
 sources=[UPDATE+'README.md',UPDATE+'source/geniesim_benchmark/USAGE.md','https://robocoliseum.ai/'])
entry('agibot-challenge25', [sim('Isaac Sim', '本届 SDK 固定版本未核实', '2025 挑战赛仿真栈',
      source='https://agibot-world.com/challenge', status='未核实')], ['智元赛事指定机器人'],
      '线上仿真 + 线下实机操作赛道', '赛制设仿真 / 真机阶段',
      '2025 届不能倒填 2026 年 Genie Sim 3.0 的 5.1.0 配置。')
entry('agibot-challenge26', GENIE, ['智元赛事指定移动双臂平台'], 'Reasoning to Action 操作赛道实机阶段',
      '赛制设仿真 / 真机阶段', '版本依据 Genie Sim 3.0；视频世界模型赛道不视为机器人执行平台。',
      ['https://www.agibot.com/article/231/detail/45.html'])
entry('lingbot-challenge26', [s for s in SUPPORT['robotwin']['simulators'] if s['engine']=='SAPIEN'], ['松灵 CobotMagic（线下规则）'],
      '线上 RoboTwin 2.0 + 线下实机赛', '赛制设仿真 / 真机阶段',
      'SAPIEN 版本来自 RoboTwin 安装要求；比赛镜像是否另锁版本未核实。',
      ['https://tianchi.aliyun.com/competition/entrance/532514/introduction'])
KUAVO = [sim('MuJoCo', '本届仿真分支未核实固定版本', 'kuavo-ros-opensource / ROS Noetic',
      source=ref('kuavo_install'), status='未核实')]
entry('kuavo-tianchi|reali-kuavo', KUAVO, ['Kuavo 4 Pro'], '仿真 / 真机部署代码及赛事实机阶段',
      '迁移接口 / 平行环境', '天池与 ICRA 使用不同仿真分支；不拿主分支或 LeRobot 版本冒充 MuJoCo 版本。',
      [ref('kuavo_baseline_readme'),ref('kuavo_install')])
entry('openlet-community', real=['赛方指定真实操作平台（本赛季型号待核对）'], scope='赛事披露的实机赛程',
      note='不以历史 Kuavo 赛题或本体替代本赛季信息；本届仿真引擎与版本尚未核实。', state='仿真器 / 版本待核对')

POLICY = [
    '版本来自官方仓库 / 安装文档；固定版本、范围、版本系列与未披露分别显示。未实跑全部外部项目。',
    '框架版本和底层仿真器版本分别记录；当前安装配置、原始论文和其他分支不会自动合并。',
    '真实平台表示有真实机器人采集、执行接口或明确的实机评测；旁边注明范围。人体数据不算机器人平台。',
    '只有原文明确展示迁移才写“已展示”；同时具备仿真与实机环境、域随机化或赛制要求不等于已证明 sim2real。',
    '任务级只继承对应子集 / 阶段的能力；RoboDojo 实机任务、Kuavo 真机阶段不填为仿真任务。',
]

def finalize(s, fallback_sources=()):
    s = deepcopy(s)
    s['simulator_names'] = list(dict.fromkeys(x['engine'] for x in s['simulators']))
    s['simulator_summary'] = '；'.join(f"{x['engine']} {x['version']}" + (f" / {x['framework']}" if x['framework'] else '') for x in s['simulators']) or s['simulator_state']
    s['real_platform_label'] = '真实平台' if s['real_support'] else ''
    s['platform_summary'] = ('真实平台：'+' / '.join(s['real_platforms'])+'；' if s['real_support'] else '')+s['real_scope']+'；sim2real：'+s['sim2real']
    s['platform_sources'] = list(dict.fromkeys(s['platform_sources']+[x['source'] for x in s['simulators'] if x['source']]+list(fallback_sources)))
    s['platform_checked'] = '2026-10-11'
    return s

def task_stage(s, real, robot='', scope='对应阶段 / 子集', simulation_only=False):
    s = deepcopy(s)
    if real:
        s['simulators'] = []
        s['simulator_state'] = '本任务定义为真机阶段；未列配对仿真环境'
        s['real_platforms'] = [robot] if robot else s['real_platforms']
        s['real_scope'] = scope
        s['sim2real'] = '本任务未确认配对迁移结果'
    else:
        s['real_platforms'] = []
        s['real_scope'] = '本任务定义为仿真阶段；未确认同任务实机覆盖'
        s['sim2real'] = '本任务未确认实机迁移'
    s['real_support'] = bool(s['real_platforms'])
    return s

def apply_platforms(records, tasks, families, competitions):
    assert set(SUPPORT)=={r['id'] for r in records}, (set(SUPPORT)-{r['id'] for r in records}, {r['id'] for r in records}-set(SUPPORT))
    for r in records:
        r.update(finalize(SUPPORT[r['id']], [l['url'] for l in r['links']]))
        # Retain all version citations in ordinary source listings and comparison.
        seen={l['url'] for l in r['links']}
        for u in r['platform_sources']:
            if u not in seen:
                r['links'].append(dict(label='平台 / 版本依据',url=u));seen.add(u)
    byid={r['id']:r for r in records}
    for f in families:
        f.update(finalize(SUPPORT[f['id']], byid[f['id']]['platform_sources']))
    eventmap={'roco26':'roco-iros','ebim26':'ebim','agibot25':'agibot-challenge25','agibot26':'agibot-challenge26',
              'lingbot26':'lingbot-challenge26','openlet26':'openlet-community','kuavo-tianchi25':'kuavo-tianchi','reali26':'reali-kuavo','robocoliseum26':'robocoliseum'}
    for e in competitions:
        if e['id'] in eventmap:
            s=SUPPORT[eventmap[e['id']]]
        else:
            robot_event=e['id'] in ['yizhi26','yizhuang25','elder25','warrior26','marathon26','humanoid25','paddle-power23','paddle-rescue23','paddle-car23']
            event_robots={'paddle-power23':['宇树 Go1（线下巡检）'], 'paddle-rescue23':['实机机器狗（型号依赛题）'],
                          'paddle-car23':['指定智能车 / EdgeBoard 平台（线下）']}
            s=dict(simulators=[],real_platforms=event_robots.get(e['id'],['按赛道 / 参赛队配置的真实机器人']) if robot_event else [],
                real_support=robot_event,real_scope='公开线下机器人赛 / 场景赛；型号依赛道' if robot_event else '未确认机器人实机执行平台',
                sim2real='未核实',platform_note='没有核实统一仿真器与版本；视频 / 算法 / 开放应用赛不默认拥有机器人执行接口。',
                platform_sources=[],simulator_state='未核实统一仿真器' if robot_event else '未核实或不适用（非机器人操作赛）')
        e.update(finalize(s,[e['url']]))
        for tr in e['tracks']:
            ts=deepcopy(s)
            if e['id'] in ['kuavo-tianchi25','reali26']:
                ts=task_stage(ts,'仿真' not in tr['name'],scope=tr['name'])
            elif e['id'] in ['agibot25','agibot26'] and ('World' in tr['name'] or '世界' in tr['name']):
                ts.update(simulators=[],real_support=False,real_platforms=[],real_scope='视频 / 世界模型赛道',sim2real='不适用',simulator_state='不适用（视频 / 模型评测）')
            tr.update(finalize(ts,[e['url']]))
    eventbyname={e['name']:e for e in competitions}
    for t in tasks:
        src=t['source']
        if src=='LIBERO': s=SUPPORT['libero']
        elif src=='RoboTwin 2.0':
            if t['name'] in ['handover_block','click_bell']:
                s=deepcopy(SUPPORT['robotwin']);s['real_scope']='论文中明确同名任务的 COBOT-Magic 实机验证'
            else:
                s=task_stage(SUPPORT['robotwin'],False)
            s=deepcopy(s);s['simulators']=[x for x in s['simulators'] if x['engine']=='SAPIEN']
            s['platform_note']='本任务按 SAPIEN 主分支注册；官方 IsaacLab-Arena 的逐任务覆盖另核对。'+s['platform_note']
        elif src.startswith('RoboDojo'):
            s=task_stage(SUPPORT['robodojo'],'实机' in src,robot=t['group'],scope='该本体的官方实机任务清单')
        else:
            e=eventbyname[src]
            tr=next(tr for tr in e['tracks'] if tr['name']==t['group'])
            s=tr
            if e['id']=='ebim26':
                s=deepcopy(tr);s['simulators']=[x for x in s['simulators'] if x['engine']!='Genesis']
                s['real_scope']='官方核心任务；实机阶段覆盖按赛方发布'
        t.update(finalize({k:s[k] for k in ['simulators','real_platforms','real_support','real_scope','sim2real','platform_note','platform_sources','simulator_state']},[t['url']]))
    assert all(r['simulator_summary'] and r['platform_sources'] for r in records+tasks+families+competitions)
