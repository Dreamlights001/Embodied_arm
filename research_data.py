"""Curated research snapshot, 2026-10-11. Run build_dashboard.py to embed offline."""
import json

RECORDS = []
def add(id, name, year, venue, roles, arms, atomic, horizon, operation, manufacturing,
        env, scale, tasks, value, limits, status, links, data="", generation=""):
    RECORDS.append(dict(id=id, name=name, year=year, venue=venue, roles=roles.split('|'),
        arms=arms.split('|'), atomic=atomic.split('|'), horizon=horizon.split('|'),
        operation=operation.split('|'), manufacturing=manufacturing, env=env,
        scale=scale, tasks=tasks, value=value, limits=limits, status=status,
        links=[dict(label=k,url=v) for k,v in links], data=data, generation=generation,
        checked="2026-10-11"))

add('nist','NIST Assembly Task Boards',2020,'RA-L / NIST','Benchmark','配置可变','A2|A3','原子/短程','直接操作|工具操作','智能制造',
 '实物任务板','3 类任务板（2020 论文）','销孔、螺纹、卡扣、齿轮、连接器、皮带与布线。',
 '最适合定义可复现的装配原子技能及质量指标；保留 CAD、容差、物料和夹具版本。',
 '任务板不是训练数据集；长程工序依赖和失败恢复需要另行编排。','设计与协议公开',
 [('论文','https://www.nist.gov/publications/benchmarking-protocols-evaluating-small-parts-robotic-assembly-systems'),('CAD / 指标','https://www.nist.gov/el/intelligent-systems-division-73500/robotic-grasping-and-manipulation-assembly/assembly')])
add('fmb','FMB',2024,'IJRR','Benchmark|Dataset','单臂','A2|A3','原子/短程|长程','直接操作','智能制造',
 '真实 Franka + 3D 打印件','22,550 条轨迹','抓取、翻转、重抓与多阶段插装。',
 '用可打印零件测试形状泛化，适合单臂“搬运→定向→装配”的研究起点。',
 '原平台是 Franka；换成现有协作臂需重采动作、适配夹爪并标定。','数据 / CAD / 代码入口公开',
 [('论文','https://arxiv.org/abs/2401.08553'),('项目 / 数据','https://functional-manipulation-benchmark.github.io/')],
 '多视角 RGB、机器人状态/动作等；实际字段以数据说明为准。')
add('furniture','FurnitureBench',2023,'RSS 2023；IJRR 2025','Benchmark|Dataset','单臂','A2|A3','长程','直接操作','智能制造',
 '真实 + 仿真 Franka','5,100 成功示范 / 219.6 小时','家具组件连接与装配，分初始状态随机化等级。',
 '适合评估完整装配成功率及中间进度，借鉴分步成功判据。',
 '是受控家具装配；不能等同工业螺钉扭矩达标或精密齿轮啮合。','代码与数据公开',
 [('论文','https://arxiv.org/abs/2305.12821'),('项目','https://clvrai.github.io/furniture-bench/'),('数据','https://clvrai.github.io/furniture-bench/docs/tutorials/dataset.html')],
 '实机示范、视觉与状态动作。')
add('ramp','RAMP',2023,'RA-L（2024 卷期）','Benchmark','单臂','A2|A3','长程','直接操作','智能制造',
 '实物 + 数字孪生','梁件与销连接装配套件','按目标结构组合梁件、销紧固，含规划与执行。',
 '低成本构建装配工站；适合研究工序依赖、诊断与恢复。',
 'AprilTag 可简化感知但应设独立赛道；旧 ROS 依赖有迁移成本。','设计与基线代码公开',
 [('论文','https://arxiv.org/abs/2305.09644'),('GitHub','https://github.com/applied-ai-lab/ramp')])
add('factory','Factory',2022,'RSS','Benchmark|Platform','单臂','A3','原子/短程','直接操作','智能制造',
 'Isaac 仿真','接触丰富装配环境','螺母螺栓、销孔等接触仿真和控制。',
 '适合力控与接触模型研究；是 IndustReal / FORGE 相关环境基础。',
 '环境套件/方法资源；不宜把仿真插入成功直接解释为实机生产可靠性。','Isaac Lab 中有对应环境',
 [('论文','https://arxiv.org/abs/2205.03532'),('环境文档','https://isaac-sim.github.io/IsaacLab/v2.2.1/source/overview/environments')])
add('industreal','IndustReal（机器人）',2023,'RSS','Benchmark|Platform','单臂','A3','原子/短程|长程','直接操作','智能制造',
 'Isaac Gym + 真实 Franka','插装 sim-to-real 工具链','接触丰富插装与感知初始化装配。',
 '适合“视觉粗定位 + 接触闭环”的精密装配路线。',
 '仿真策略和实机库分开；必须匹配控制器、接触参数与实物尺寸。','仿真环境 / 实机库公开',
 [('论文','https://arxiv.org/abs/2305.17110'),('GitHub','https://github.com/NVlabs/industreallib'),('仿真文档','https://github.com/isaac-sim/IsaacGymEnvs/blob/main/docs/industreal.md')])
add('forge','FORGE',2024,'预印本 2024；RA-L 2025','Benchmark|Platform','单臂','A3','原子/短程|长程','直接操作','智能制造',
 '仿真 + 实机','力阈值条件化装配','螺纹、插入、齿轮啮合与多阶段行星齿轮系统。',
 '研究允许接触力下的探索与成功检测，制造意义强。',
 '需要有效力反馈/控制能力；夹爪电流不能直接替代标定后的腕部六维力。','论文 / Isaac Lab 环境公开',
 [('论文','https://arxiv.org/abs/2408.04587'),('环境','https://isaac-sim.github.io/IsaacLab/v2.2.1/source/overview/environments')])
add('automate','AutoMate',2024,'CoRL','Benchmark|Dataset|Generator','单臂','A3','原子/短程','直接操作','智能制造',
 '仿真 + 实机','100 组装配几何','多种几何件的接触插装；拆卸轨迹用于学习。',
 '适合按 CAD 几何划分训练/测试，研究跨零件泛化。',
 '覆盖插装几何，不覆盖完整生产订单；逆拆卸轨迹也不自动解决紧固工艺。','项目 / Isaac Lab 环境公开',
 [('项目','https://bingjietang718.github.io/automate/'),('环境','https://isaac-sim.github.io/IsaacLab/v2.2.1/source/overview/environments')],
 '装配几何与仿真轨迹。','逆向拆卸与策略学习；输出几何装配数据/技能，不自动生成制造工序规范。')
add('fabrica','Fabrica',2025,'预印本','Benchmark|Platform','双臂','A3','长程','直接操作','智能制造',
 '仿真 + 实机双臂','多零件装配评测套件','一臂持件/支撑，另一臂装配；顺序、抓取、运动联合规划。',
 '最贴近双臂主动夹具；适合 CAD 约束规划 + 局部学习控制。',
 '自动夹具和离线规划亦是系统组成；论文中步骤成功率不能当整机装配成功率。','论文与项目页可访问；代码完备性未验证',
 [('论文','https://arxiv.org/abs/2506.05168'),('项目','https://fabrica.csail.mit.edu/')])
add('roco','RoCo · AAAI 2026',2026,'AAAI 挑战报告','Benchmark|Dataset','双臂','A3','长程','直接操作','智能制造',
 'Isaac Sim / Lab + Galaxea R1','行星齿轮箱装配','行星轮、太阳轮、齿圈逐阶段安装，含失败恢复。',
 '双臂长程制造优先参考：按工序计分，比较恢复数据对实机部署的贡献。',
 '平台与夹爪差异需重采；人机协作背景不等于每个 episode 都实时含人。','仿真仓库 / dataset devkit 公开',
 [('论文','https://arxiv.org/abs/2603.15469'),('GitHub','https://github.com/rocochallenge/gearboxAssembly'),('数据工具','https://github.com/rocochallenge/roco_dataset_devkit'),('AAAI 版本','https://rocochallenge.github.io/RoCo-AAAI2026/')],
 '实机遥操作、阶段标注；devkit 提供读取入口。')
add('roco-iros','RoCo · IROS 2026',2026,'挑战协议 / 官方页面','Benchmark','配置可变','A2|A3','原子/短程|长程','直接操作|工具操作','智能制造',
 '仿真 + 现场平台','工业任务板 / 积木装配两赛道','连接器、布线、拧螺丝、电池装配；积木结构组装。',
 '最新制造任务目录：用于扩展工具与柔性件实验。',
 '与 AAAI 齿轮箱版分开统计；各赛道本体/接口不同，本次未核实完整发布包与最终赛果。','官方协议可读；完整数据开放状态待核实',
 [('官方页面','https://rocochallenge.github.io/RoCo-IROS2026/'),('FAQ','https://rocochallenge.github.io/RoCo-IROS2026/faq.html')])
add('workbench','WorkBenchMark',2026,'RoboCup Symposium / 预印本','Benchmark','单臂','A2|A3','原子/短程|长程','直接操作','智能制造',
 'MuJoCo + 实机 Panda / UR 类','400 任务 / 4 层；40 个实机任务设计','Duplo 积木组合，装配依赖与稳定性约束逐层加深。',
 '可低成本复刻；将规划难度与接触难度分别调节。',
 '官网仍含 draft / TBD：仿真入口与许可有待确认，实机 Tier 4 标作未来验证；不要认作完整成熟发布。','论文 / 项目公开；发布细节部分待定',
 [('论文','https://arxiv.org/abs/2606.19358'),('官方项目','https://workbenchmark.github.io/')])
add('assemblybench','AssemblyBench',2026,'CVPR','Benchmark|Dataset|Generator','无指定机器人','不适用','长程','不适用','智能制造',
 'CAD 零件 + 物理仿真','2,789 工业对象','图文装配说明、零件模型、顺序和零件 6-DoF 装配轨迹。',
 '用于说明书到装配序列/轨迹；适合为高层规划生成约束和训练样本。',
 '零件轨迹不等于机械臂关节动作；缺少夹爪可达性/持件约束时不能直接执行。','代码 / 数据下载 / 生成入口公开',
 [('论文','https://arxiv.org/abs/2605.12845'),('GitHub','https://github.com/merlresearch/AssemblyBench')],
 '合成图文说明、CAD、零件位姿轨迹；非实机控制动作。','从装配几何和轨迹生成结构化数据；需再做抓取与机器人运动可行性校验。')
add('ariac','ARIAC · 2025 版',2025,'NIST 竞赛 / 官方文档','Benchmark|Platform','多机器人','A1|A2','长程','直接操作','智能制造',
 'ROS / Gazebo 工业仓储','订单驱动 kitting / assembly','搬运、配料、装配及动态订单环境。',
 '借鉴订单、工件缺陷与扰动规则，构造“来料→配套→装配→交付”。',
 '工作站有多个不同角色机器人，不能简化成两只桌面臂；本条锁定已查阅 2025 版。','2025 文档公开',
 [('官方文档','https://pages.nist.gov/ARIAC_docs/en/stable/index.html')])
add('hail','HAIL',2026,'Journal of Manufacturing Systems','Benchmark|Dataset|Collection','单臂','A2|A3','原子/短程|长程','直接操作|工具操作','智能制造',
 '真实 Flexiv Rizon 4 + MR 示教','8 任务 / 5 类；论文每任务 50 示范','精密插装、工具使用、柔性件等，拆解 meta-actions。',
 '与夹爪协作臂匹配；借鉴分阶段故障分析、ACT / DP 对照和实时推理设置。',
 '论文平台有力/阻抗能力，现有机械臂未必等价；本次未找到可确认的官方完整代码/数据仓库。','出版论文可读；开放数据状态待核实',
 [('出版论文','https://www.sciencedirect.com/science/article/pii/S0278612526001081')],
 '多视角 RGB、机器人本体状态、末端轨迹；论文级数据描述。')
add('robotwin','RoboTwin 2.0',2025,'首发 2025；ICML 2026','Benchmark|Dataset|Generator','双臂','A1|A2|A3','原子/短程|长程','直接操作|工具操作','可迁移',
 'SAPIEN / 多本体仿真','50 双臂任务 / 5 本体（任务文档）','交接、双臂搬运、堆叠、锤击、盖章、扫描等。',
 '双臂基线首选之一；可提取交接、工具与同步执行子集。',
 '并非工业精密装配基准；任务在双臂平台上运行也不意味着每项都必须双臂。','官方代码 / 任务文档公开',
 [('论文','https://arxiv.org/abs/2506.18088'),('GitHub','https://github.com/RoboTwin-Platform/RoboTwin'),('任务','https://robotwin-platform.github.io/doc/tasks/')],
 '自动合成示范、视觉、机器人状态/动作。','专家程序生成 + 本体适配 + 域随机化；增加工业工件需要资产、抓取点、接触和判据。')
add('robofactory','RoboFactory',2025,'ICCV','Benchmark|Generator','多机器人','A1|A2','原子/短程|长程','直接操作','可迁移',
 'ManiSkill 仿真','多智能体组合约束任务','协同搬运、约束组合与多机器人操作。',
 '借鉴工站角色分配、共享资源和组合约束。',
 '名称含 Factory 不代表完整工业生产工艺；多智能体实验与一台双臂机器人要分开。','代码与自动采集框架公开',
 [('GitHub','https://github.com/MARS-EAI/RoboFactory')],
 '脚本采集仿真视觉/状态/动作。','约束任务与自动示范收集；适合协作协议，需自建工业验收标准。')
add('robosuite','robosuite',2020,'仿真平台 / 持续更新','Benchmark|Platform','单臂|双臂','A1|A2|A3','原子/短程|长程','直接操作','可迁移',
 'MuJoCo','模块化操作环境','NutAssembly、双臂 Peg-in-Hole、交接、ToolHang。',
 '快速原型：单臂插装对比双臂持孔件；适合控制和本体消融。',
 'ToolHang 是挂起工具，不是用工具加工；螺母套销不等于螺纹紧固。','官方环境文档公开',
 [('环境','https://robosuite.ai/docs/modules/environments.html'),('API','https://robosuite.ai/docs/source/robosuite.environments.manipulation.html')])
add('maniskill','ManiSkill 3',2025,'仿真平台 / 持续更新','Benchmark|Dataset|Platform','单臂|双臂','A1|A2|A3','原子/短程|长程','直接操作|工具操作','可迁移',
 'SAPIEN / GPU 仿真','多任务与多本体','AssemblingKits、PegInsertionSide、FMB 仿真、PokeCube 等。',
 '适合多样化原子技能、并行训练与工业几何件原型。',
 '每个环境支持本体不同；示例 PegInsertionSide 的 3 mm 间隙不能代表精密工业插装。','任务源码与文档公开',
 [('任务 API','https://maniskill.readthedocs.io/en/latest/api/mani_skill/index.html'),('插装参数','https://maniskill.readthedocs.io/en/latest/api/mani_skill/envs/tasks/tabletop/peg_insertion_side/index.html')],
 '仿真示范；字段和任务可用性按环境版本。')
add('rlbench','RLBench',2020,'RA-L / ICRA','Benchmark|Generator','单臂','A1|A2|A3','原子/短程|长程','直接操作|工具操作','可迁移',
 'CoppeliaSim / PyRep','100 个基准任务划分；库持续扩展','广泛桌面操作，包含装配类和多步骤操作。',
 '用统一任务接口开展语言与视觉控制；挑选真实制造相关任务再复刻。',
 '论文中常见 18 任务评测只是子集；waypoint 专家可能引入简化假设。','代码与 task builder 公开',
 [('GitHub','https://github.com/stepjam/RLBench')],
 '自动专家示范、RGB-D / 分割与状态。','基于 waypoint 的专家示范与任务构建；新任务需人工定义关键点/成功条件。')
add('calvin','CALVIN',2022,'RA-L','Benchmark|Dataset','单臂','A1|A2','原子/短程|长程','直接操作','可迁移',
 'PyBullet 桌面工站','连续语言任务链','开抽屉、移动块、开滑门等原子技能组合。',
 '借鉴连续任务链与跨环境泛化协议，测试长程误差累积。',
 '任务链与生产工序 DAG 不同；不考核工业接触质量。','代码与数据公开',
 [('GitHub','https://github.com/mees/calvin')],
 '连续 play 数据、语言标注、图像及机器人动作。')
add('libero','LIBERO（含 LIBERO-10）',2023,'NeurIPS Datasets & Benchmarks','Benchmark|Dataset|Generator','单臂','A1|A2','原子/短程|长程','直接操作','通用参考',
 'MuJoCo / robosuite','130 任务；100 = 90 + 10','空间、物体、目标知识迁移与多阶段桌面操作。',
 'LIBERO-10（常称 Long/Long-10）用于长程子集对照；适合预训练与任务迁移基线。',
 '10 是原套件子集，不另算 10 个独立 benchmark；不是制造装配数据。','代码 / 示范 / 任务生成入口公开',
 [('论文','https://arxiv.org/abs/2306.03310'),('GitHub / 数据','https://github.com/Lifelong-Robot-Learning/LIBERO')],
 '遥操作成功示范；LIBERO-10 常用 10×50=500 条，转换后的 RLDS/LeRobot 应核对切分。',
 '程序化场景/任务生成；语言模板和谓词检查不能替代工艺可执行性。')
add('liberoplus','LIBERO-Plus',2025,'预印本','Benchmark|Dataset','单臂','A1|A2','原子/短程|长程','直接操作','可迁移',
 'LIBERO 扰动扩展','10,030 评测任务 / 7 扰动维度','布局、相机、机器人初态、语言、光照、背景与传感器噪声。',
 '制造实验应借鉴受控扰动，特别是换相机、换批次与工件位姿偏差。',
 '是鲁棒性扩展，不是新增 10,030 种工业技能；评测协议与原 LIBERO 不同。','代码 / 资产 / 训练数据入口公开',
 [('论文','https://arxiv.org/abs/2510.13626'),('GitHub','https://github.com/sylvestf/LIBERO-plus')],
 '提供 RLDS、LeRobot 等训练数据入口；与评测扰动集区分。')
add('liberopro','LIBERO-PRO',2025,'预印本','Benchmark','单臂','A1|A2','原子/短程|长程','直接操作','可迁移',
 'LIBERO 扰动扩展','4 扰动维度','物体、初态、指令与环境扰动，评估记忆依赖。',
 '用来检查“训练场景高分”是否能迁移至真实工站变化。',
 'PRO 与 Plus 是不同项目；不要合并名称或分数。','论文与代码链接公开',
 [('论文','https://arxiv.org/abs/2510.03827'),('GitHub','https://github.com/Zxy-MLlab/LIBERO-PRO')])
add('liberovpro','LIBERO-VPro',2026,'2026-09 新预印本','Benchmark','单臂','A1|A2','原子/短程|长程','直接操作','可迁移',
 '闭环视觉鲁棒性','3,296 task-condition cases（论文）','视觉退化、相机时效、视觉源一致性与任务相关变化。',
 '对相机延迟/冻结测试有启发，值得作为工站视觉鲁棒性补充。',
 '新预印本；本次仅核实论文层面，未确认可复现实验发布。','论文公开；完整代码状态未核实',
 [('论文','https://arxiv.org/abs/2609.24350')])
add('vlabench','VLABench',2024,'首发预印本 2024','Benchmark|Dataset','单臂','A1|A2|A3','原子/短程|长程','直接操作|工具操作','可迁移',
 'MuJoCo / dm_control','100 任务类别 / 2,000+ 物体','常识、隐含意图、工具与长程推理操作。',
 '借鉴语义目标与组合任务；制作“不同订单/工具选择”的制造指令测试。',
 '整体偏通用操作；类别数不是独立固定 episode 数；不同封装提供的任务子集不同。','项目与数据/代码入口公开',
 [('项目','https://vlabench.github.io/'),('论文','https://arxiv.org/abs/2412.18194'),('封装文档','https://huggingface.co/docs/lerobot/vlabench')],
 '仿真任务数据，具体下载与协议随版本核对。')
add('bigym','BiGym',2024,'CoRL','Benchmark|Dataset','双臂','A1|A2','原子/短程|长程','直接操作','通用参考',
 'MuJoCo 移动双臂','40 家庭任务','双手操作、清理厨房、移动操作。',
 '借鉴双臂视觉/本体观测与示范驱动学习。',
 '固定桌面臂没有移动基座；需剥离导航相关任务与动作维度。','论文 / 项目公开',
 [('论文','https://arxiv.org/abs/2407.07788'),('项目','https://chernyadev.github.io/bigym/')],
 '每任务人工示范；RGB-D 和本体状态。')
add('behavior','BEHAVIOR-1K',2022,'CoRL 2022；2026 挑战文档','Benchmark|Dataset|Platform','配置可变','A1|A2|A3','长程','直接操作|工具操作','通用参考',
 'OmniGibson 家庭移动操作','1,000 家庭活动定义','长程家庭活动、对象状态与交互。',
 '借鉴对象状态、前置条件和端到端活动评价。',
 '活动全集、年度挑战子集、本体配置必须分开；固定协作臂只复用桌面部分。','2026 挑战评测文档公开',
 [('官方评测','https://github.com/StanfordVL/BEHAVIOR-1K/blob/main/docs/challenge/evaluation.md')],
 '年度挑战数据与活动库不是同一规模。')
add('robocasa','RoboCasa365',2026,'2026 预印本','Benchmark|Dataset|Generator','配置可变','A1|A2','原子/短程|长程','直接操作|工具操作','通用参考',
 'MuJoCo 家庭/厨房移动操作','365 任务 / 2,500+ 场景 / 3,200+ 物体','厨房操作与组合任务；人工及合成示范。',
 '借鉴规模化资产、任务库与可控域变化。',
 '365 是家庭任务；场景规模不能当制造场景覆盖。固定臂任务需单独筛选。','官方代码 / 数据入口公开',
 [('论文','https://arxiv.org/abs/2603.04356'),('GitHub','https://github.com/robocasa/robocasa')],
 '人工示范 + 自动合成示范。','场景资产组合和 LLM 辅助任务设计；制造需新增 CAD、夹具与工艺状态。')
add('robolab','RoboLab',2026,'RSS','Benchmark|Generator|Platform','配置可变','A1|A2','原子/短程|长程','直接操作','可迁移',
 'Isaac Sim / Lab','120 任务；平均 2.02 子任务','视觉、关系与程序能力；分拣工具、搬物、重定向与堆叠。',
 '可把工件/料盒快速布置成新场景，按本体与策略配置生成环境。',
 '默认任务以通用桌面操作为主；把锤子放进料盒是直接操作，不是锤击。重接触制造需校验仿真。','官方代码与生成工具公开',
 [('论文','https://arxiv.org/abs/2604.09860'),('项目','https://research.nvidia.com/labs/srl/projects/robolab/'),('GitHub','https://github.com/NVLabs/RoboLab')],
 '评测 episode 记录；主要不是大规模实机训练数据集。',
 '人工/代码智能体生成 USD 场景、指令任务和本体配置；采用约束与物理 settle。')
add('mimicgen','MimicGen',2023,'CoRL','Dataset|Generator','单臂','A1|A2|A3','原子/短程|长程','直接操作|工具操作','可迁移',
 'robosuite / MuJoCo','48,000+ 公开示范 / 12 任务','将少量示范分段，并按新对象位姿变换/重组。',
 '扩增拾取、转向、插装与锤击数据，降低新初态采集成本。',
 '需源示范、对象位姿和分段接口；新接触模式/柔性物体不是直接刚体变换能解决。','生成代码 / 环境 / 数据公开',
 [('论文','https://arxiv.org/abs/2310.17596'),('GitHub','https://github.com/NVlabs/mimicgen'),('接口教程','https://github.com/NVlabs/mimicgen/blob/main/docs/tutorials/getting_started.md')],
 'robomimic 兼容 HDF5 仿真动作示范。','对象中心的源示范变换与阶段拼接；生成成功轨迹后仍需去重与测试集隔离。')
add('dexmimicgen','DexMimicGen',2024,'首发 2024；ICRA 2025','Dataset|Generator','双臂','A2|A3','原子/短程|长程','直接操作','可迁移',
 '双臂/灵巧手仿真','20,000+ 示范 / 60 源示范（项目）','双臂协同与精细操作数据合成。',
 '借鉴双臂分阶段协同生成；公开环境中有 TwoArmThreading。',
 '夹爪与灵巧手赛道要区分；官方仓库明确发布环境/数据，未确认核心生成管线完整开放。','环境与数据公开；生成管线开放程度待核实',
 [('论文','https://arxiv.org/abs/2410.24185'),('项目','https://dexmimicgen.github.io/'),('GitHub','https://github.com/NVlabs/dexmimicgen')],
 '合成双臂示范；按末端本体选子集。','论文：双臂轨迹适配与协同生成；当前可直接复用的主要是环境与发布数据。')
add('skillmimicgen','SkillMimicGen',2024,'CoRL 2024 / PMLR 2025','Generator','单臂','A2|A3','长程','直接操作','可迁移',
 '仿真 + 实机示例','技能和运动规划组合','将可泛化技能与自由空间运动规划拼接。',
 '适合制造“搬运运动段 + 局部接触技能”的分层路线。',
 '需提供技能、分段与运动规划接口；生成器不替代工艺质量验证。','论文与项目公开',
 [('论文','https://raw.githubusercontent.com/mlresearch/v270/main/assets/garrett25a/garrett25a.pdf'),('项目','https://skillgen.github.io/')],
 '', '任务拆成运动段/技能段，由规划负责过渡，由技能控制处理接触。')
add('droid','DROID',2024,'RSS','Dataset|Collection','单臂','A1|A2','原子/短程','直接操作|工具操作','通用参考',
 '真实 Franka / 多环境','76k 轨迹 / 350 小时 / 564 场景','日常多场景、多任务遥操作。',
 '优先作为视觉操作预训练和跨场景鲁棒性参考，结合自采制造数据微调。',
 '官网/论文任务数存在 84/86 版本差异，报告不混用；大规模生活数据不保证插装力控。','数据 / 采集与训练代码公开',
 [('论文','https://arxiv.org/abs/2403.12945'),('项目','https://droid-dataset.github.io/'),('训练代码','https://github.com/droid-dataset/droid_policy_learning')],
 '多相机视频、机器人状态/动作、语言；深度/标定按发布文件核对。')
add('bridge','BridgeData V2',2023,'CoRL','Dataset','单臂','A1|A2','原子/短程','直接操作|工具操作','通用参考',
 '真实 WidowX / 桌面','60,096 轨迹 / 24 环境 / 13 技能','抓放、推移、扫颗粒、开关抽屉、堆叠等。',
 '低成本桌面操作预训练参考；支持语言或目标图像条件。',
 '动作空间、相机和夹爪与协作臂不同；60,096 含 9,731 脚本 rollouts，不全是遥操作。','数据与官方项目公开',
 [('项目 / 数据','https://rail-berkeley.github.io/bridgedata/'),('论文','https://proceedings.mlr.press/v229/walke23a/walke23a.pdf')],
 '视觉、状态/动作、任务语言；50,365 遥操作 + 9,731 脚本轨迹。')
add('oxe','Open X-Embodiment',2023,'ICRA 2024','Dataset','单臂|双臂','A1|A2|A3','原子/短程|长程','直接操作|工具操作','通用参考',
 '真实多本体数据聚合','原论文 22 本体 / 21 机构','跨机器人通用技能与多种来源数据。',
 '预训练数据入口；需要按末端类型、动作单位与任务领域选择数据混合。',
 '聚合数据含 Bridge 等来源，不能与子数据集简单求和；不同子集许可和字段不同。','标准化数据/模型入口公开',
 [('论文','https://arxiv.org/abs/2310.08864'),('官方项目','https://robotics-transformer-x.github.io/')],
 'RLDS 格式的跨本体视觉、状态、动作与语言；字段完整性随子集变化。')
add('agibot','AgiBot World',2025,'IROS 2025；T-RO 2026（仓库标注）','Dataset|Benchmark|Collection','双臂','A1|A2|A3','原子/短程|长程','直接操作|工具操作','智能制造',
 '真实移动双臂 / 多种末端','Beta 1,003,672；Alpha 92,214 轨迹','覆盖工业等五类场景、接触与长程操作。',
 '用户所说 aigbot world 按 AgiBot World 解释；优先筛工业子集再微调现有双臂。',
 '双臂/灵巧手/移动数据须筛选；海量轨迹不等于所有工业子集都含力/触觉字段。','数据 / task catalog / GO-1 代码公开',
 [('GitHub / 数据','https://github.com/OpenDriveLab/AgiBot-World')],
 '视觉与本体动作；按 Task Catalog 选择夹爪、工业场景与传感模态，勿假设全量触觉。')
add('umi','UMI',2024,'RSS','Collection|Dataset','单臂|双臂','A1|A2','原子/短程|长程','直接操作','可迁移',
 '手持夹爪采集 + 机器人部署','采集/学习框架与示例数据','无需机器人在场的手持夹爪示教，含双手/动态操作。',
 '与夹爪路线契合，可收工厂搬物、上料与柔性件示范。',
 '不是天然高精度力控示教；SLAM、时序、夹爪尺寸和机器人可达性是关键。','硬件 / 软件 / 采集文档公开',
 [('论文','https://arxiv.org/abs/2402.10329'),('项目','https://umi-gripper.github.io/'),('GitHub','https://github.com/real-stanford/universal_manipulation_interface')],
 '视频、SLAM 末端位姿、夹爪开度；不是人体裸手视频，也不默认有六维力。')
add('ego4d','Ego4D',2022,'CVPR；持续发布','Dataset','人体双手','不适用','原子/短程|长程','直接操作|工具操作','可迁移',
 '真实第一视角人体','官方文档 3,600+ 小时','日常/工作场景与动作、记忆、预测；GoalStep 步骤标注。',
 '适合高层步骤识别、失败理解和语义预训练。',
 '人体视频没有机器人控制 action；需筛制造片段并用自采动作建立映射。','官方数据与标注入口公开',
 [('官方文档','https://ego4d-data.org/docs/')],
 '第一视角视频、语言/任务标注；部分附传感器数据，不等于每条都完备。')
add('egoexo','Ego-Exo4D',2023,'CVPR 2024','Dataset','人体双手','不适用','原子/短程|长程','直接操作|工具操作','可迁移',
 '同步第一/第三视角人体','V2：1,286.30 视频小时 / 5,035 takes','熟练活动，含 Bike Repair；步骤、依赖、专家点评。',
 '维修类工具操作与长程程序理解参考，适合多视角步骤学习。',
 '总视频小时包含多个视角，不能等同操作时长；不提供机器人闭环动作。','官方 V2 文档与数据入口公开',
 [('论文','https://arxiv.org/abs/2311.18259'),('V2 文档','https://docs.ego-exo4d-data.org/')],
 '同步 ego/exo 视频、IMU、语言、人体/手部姿态等；版本字段有差异。')
add('egomimic','EgoMimic',2024,'首发 2024；CoRL 2024','Dataset|Collection','双臂|人体双手','A1|A2','原子/短程|长程','直接操作','可迁移',
 'Aria 人体 + 双臂机器人','3 个实机任务（项目评测）','人类第一视角与机器人遥操作联合学习。',
 '研究“人类示范补充机器人示范”的小样本制造迁移。',
 '需要人体/机器人动作对齐；不能把人手轨迹直接当协作臂关节动作。','数据处理 / 训练代码 / 示例数据公开',
 [('论文','https://arxiv.org/abs/2410.24221'),('项目','https://egomimic.github.io/'),('GitHub','https://github.com/SimarKareer/EgoMimic')],
 '第一视角视频、手部 3D、机器人示范；HF 提供示例 HDF5。')
add('egodex','EgoDex',2025,'研究论文 / 官方仓库','Dataset','人体双手','不适用','原子/短程|长程','直接操作|工具操作','可迁移',
 'Apple Vision Pro / ARKit','829 小时 / 194 任务','桌面人体精细操作与手部姿态、语言。',
 '可用来学习手-物/工具交互语义与精细操作表征。',
 '名称 dexterous 指人体动作；现有夹爪无法覆盖全部多指操作，需筛任务。','官方代码与数据入口公开',
 [('GitHub / 数据','https://github.com/apple-aiml-research/ml-egodex')],
 '30 Hz 1080p 视频、头部/上身/手 3D 位姿、语言；无机器人控制 action。')
add('egoverse','EgoVerse',2026,'RSS','Dataset|Collection','人体双手','不适用','原子/短程|长程','直接操作','可迁移',
 '多机构真实第一视角','官方当前快照 4,003 小时 / ~80k episodes','标准任务与开放任务；人体到不同机器人迁移。',
 '最新 ego 数据入口；适合抓放、装袋、双手精细操作表征迁移。',
 '持续增长快照不能与论文旧版混用；工业 split 需另查字段/许可，本报告不假定全量制造标签。','官方生态与代码入口公开',
 [('论文','https://arxiv.org/abs/2604.07607'),('官方快照','https://egoverse.ai/'),('GitHub','https://github.com/GaTech-RL2/EgoVerse')],
 '人体示范、相机/头部姿态与密集语言；不直接等于机器人动作数据。')
add('taco','TACO',2024,'CVPR','Dataset','人体双手','不适用','原子/短程','工具操作','可迁移',
 '人体双手工具-物体交互','工具-动作-物体理解数据','使用工具与双手协作的 3D 交互。',
 '为工具选择、作用位置和动作意图提供语义参考。',
 '它是人体理解/交互数据，不是双臂机器人工具加工成功率基准。','官方代码与数据入口公开',
 [('GitHub','https://github.com/leolyliu/TACO-Instructions')],
 '人体/工具/物体交互数据；机器人控制标签需另建。')
add('industreal-human','IndustReal（人体视频）',2023,'数据集 / 官方仓库','Dataset','人体双手','不适用','长程','直接操作','智能制造',
 '人体装配/维护视频','84 视频 / 27 参与者','construction-toy 装配和维护步骤。',
 '借鉴装配状态识别、步骤追踪与操作过程理解。',
 '与 NVIDIA IndustReal 机器人 sim-to-real 是同名不同项目，必须分开；无机器人控制动作。','官方视频数据入口公开',
 [('GitHub','https://github.com/TimSchoonbeek/IndustReal')],
 '装配维护视频与步骤/状态相关标注。')

add('duobench','DuoBench',2026,'2026-06 预印本','Benchmark|Dataset','双臂','A1|A2|A3','原子/短程|长程','直接操作','可迁移',
 '仿真 + Franka FR3 Duo','11 任务 / 4 协作类型；4 任务实机复现','非对称支撑、共同操物、顺序交接、并行执行；含 Join-Blocks、Transfer-Reorient。',
 '双臂夹爪基准的新参考；特别适合检验持件、交接和并行是否真的改善任务。',
 '仅 4 项实机复现；不是完整工业工序库，现有臂需要修改本体/夹爪与重采示范。','代码 / 数据入口公开',
 [('论文','https://arxiv.org/abs/2606.11901'),('项目 / 数据 / 代码','https://duobench.github.io/')],
 '全任务人工遥操作数据与阶段语义评价，实机子集按项目说明。')

SURVEYS = [
 dict(title='Towards a Unified Understanding of Robot Manipulation',year='2025 / 2026 修订',url='https://arxiv.org/abs/2510.10903',repo='https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation',note='任务、benchmarks、数据集与高层规划/低层控制总图；作为检索入口，再回查原论文。'),
 dict(title='A Taxonomy for Evaluating Generalist Robot Manipulation Policies',year='2025',url='https://arxiv.org/abs/2503.01238',note='STAR-Gen：把泛化维度拆开；借鉴任务、场景与行为等维度设计独立测试。'),
 dict(title='Robotic Manipulation via Imitation Learning: Taxonomy, Evolution, Benchmark, and Challenges',year='2025',url='https://arxiv.org/abs/2508.17449',note='为 ACT、Diffusion 等策略选基线，关注示范数据和控制范式的匹配。'),
 dict(title='Recent progress and challenges of key technologies in robotic assembly',year='2026 卷期 / 2025 DOI',url='https://www.sciencedirect.com/science/article/pii/S100093452500032X',note='从感知、末端、控制、学习、评测审视装配；指导接触质量与硬件路线。'),
 dict(title='Data Pyramid for Embodied Manipulation: A Survey',year='2026-07 预印本',url='https://arxiv.org/abs/2607.24744',note='区分人体视频、机器人示范和合成数据；关注失败恢复数据与跨本体动作对齐。'),
 dict(title='World-Action Models for Robot Learning and Control: A Survey',year='2026-09 预印本',url='https://arxiv.org/abs/2609.16074',note='了解预测模型与可执行动作的结合；是否改善装配恢复，需要实机实验验证。'),
]

if __name__ == '__main__':
    print(json.dumps(dict(records=RECORDS,surveys=SURVEYS),ensure_ascii=False,indent=2))
