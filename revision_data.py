"""Additional first-party sources and competition hierarchy, checked 2026-10-11."""
from research_data import add, RECORDS, SURVEYS

add('robodojo','RoboDojo',2026,'2026-07 预印本 / 官方开放项目','Benchmark|Dataset|Platform','双臂','A1|A2|A3','原子/短程|长程','直接操作|工具操作','可迁移',
 'Isaac Sim；实机 ARX X5 / Piper / Piper X','42 仿真任务；18 实机任务；实机 1,800 示范',
 '通用操作；按泛化、记忆、精度、长程、开放指令评测，包含整理、烹饪、工具清扫、螺纹紧固等。',
 '可用作 Piper 类双臂的通用能力对照；精度和工具任务可转成制造实验。',
 '仿真与实机任务不一一配对，不能用两套分数直接测 sim-to-real；42 不含训练专用 DLC。当前仓库强调 eval-only，策略服务由 XPolicyLab 承担。',
 '论文、代码、任务规范与评测入口公开',
 [('论文','https://arxiv.org/abs/2607.04434'),('GitHub','https://github.com/RoboDojo-Benchmark/RoboDojo'),('任务规范','https://robodojo-benchmark.com/doc/'),('策略接口','https://github.com/XPolicyLab/XPolicyLab')],
 '实机：语言、机器人状态、头部与双腕 RGB，25 Hz；仿真/实机示范分开。')
add('embodichain','EmbodiChain',2025,'官方项目 / Alpha','Platform|Generator','配置可变','A1|A2','原子/短程|长程','直接操作','可迁移',
 'GPU 仿真 / 可扩展机器人与任务注册','框架规模不等同固定 benchmark 任务数',
 '仿真、任务环境、生成数据、训练与评测；任务族涵盖 manipulation 和 classic control。',
 '适合把自有 URDF、工件和工站接入同一数据与评测管线；制造任务成功判据需自行实现。',
 '官方拼写为 EmbodiChain（对应用户提到的 Embodiedchain）。处于 Alpha；支持扩展并不代表已验证 PiperX / R1-7A / CR5 的控制适配。',
 'Apache-2.0 仓库与文档公开；持续开发',
 [('GitHub','https://github.com/DexForce/EmbodiChain'),('文档','https://dexforce.github.io/EmbodiChain/'),('任务结构','https://github.com/DexForce/EmbodiChain/blob/main/embodichain_tasks/README.md')],
 generation='可扩展物理环境、配置定义的任务程序、自动采集与轨迹扩增；场景/动作生成与 benchmark 定义需分别审核。')
add('ebim','EBiM 2026',2026,'双臂社区 Benchmark / Challenge（Alpha）','Benchmark|Dataset','双臂','A2|A3','长程','直接操作|工具操作','智能制造',
 '仿真 + 多地 Mobile FR3 Duo 实机','3 核心任务；各任务独立排行榜',
 '线缆布线、导热垫放置、辅助生活与喂食；前两项制造，第三项康养。',
 '兼顾双臂接触、柔性材料与跨实验室评测；适合比较持件 / 工具使用 / 协作。',
 '“智能制造”表示含制造子任务，整个套件并非全为制造。当前官方页对 workshop 地点和日期标 TBD，不能据早期关联直接认定为 IROS 正式比赛。',
 '官方规范、代码与赛果入口公开；Alpha',
 [('规范 / 任务','https://ebim-benchmark.github.io/competition.html'),('GitHub','https://github.com/EBiM-Benchmark'),('工作坊关联','https://bimanual-robot-learning.github.io/')],
 '多地示范数据按发布入口核对。')
add('geniesim','Genie Sim',2025,'官方项目 / 3.0 及后续更新','Benchmark|Dataset|Generator|Platform','双臂|配置可变','A1|A2|A3','原子/短程|长程','直接操作|工具操作','智能制造',
 '数字孪生 / 多物理后端','官方当前声明 200+ 任务 / 100,000+ 场景；非逐项已复现',
 '零售、工业、餐饮、居家、办公中的操作与移动操作；与 AgiBot World Challenge 2026 评测衔接。',
 '提供重建、场景泛化、数据采集和自动评测；可借鉴工业工件与通用任务同库管理。',
 '场景数、任务数、数据小时不可相加；README 的迁移表现是作者声明，不能外推到自有臂或精密接触工艺。',
 '代码、资产与数据入口公开；依赖和版本按快照固定',
 [('GitHub','https://github.com/AgibotTech/genie_sim'),('项目','https://agibot-world.com/genie-sim')],
 '官方声明开放 10,000+ 小时合成数据；下载版本与本体另核对。',
 '场景重建与泛化、语言驱动配置生成、遥操作 / 自动轨迹采集、自动评测。')
add('agibot-challenge25','AgiBot World Challenge 2025',2025,'IROS 2025 Challenge','Benchmark|Dataset','双臂','A1|A2|A3','原子/短程|长程','直接操作','智能制造',
 '线上仿真 + 线下实机；世界模型线上评测','操作赛道 10 任务；世界模型 10 任务取样 / 30+ 动作序列',
 '居家、超市、工业；抽屉收纳、倒水、动态物体打包、双臂协作和精细操作。',
 '赛事提供数据、基线、测试服务和实机阶段，比只读论文更适合对齐完整评测流程。',
 '世界模型赛道预测视频，不等于闭环任务执行；原始 World 数据集与赛事训练/测试集分别登记。',
 '官方规则、测试与数据入口公开',
 [('规则','https://opendrivelab.com/challenge2025/'),('赛事','https://agibot-world.com/challenge'),('数据','https://huggingface.co/datasets/agibot-world/AgiBotWorldChallenge-2025')])
add('agibot-challenge26','AgiBot World Challenge 2026',2026,'ICRA 2026 Challenge','Benchmark|Dataset','双臂','A1|A2|A3','原子/短程|长程','直接操作|工具操作','智能制造',
 'Genie Sim 3.0 + 实机；世界模型线上','2 赛道；世界模型 10 场景 / 30,000+ 真实轨迹',
 'Reasoning to Action 与 World Model；物流分拣、工件翻转、货架整理、爆米花舀取、开门、清桌、双臂端锅。',
 '工业工件翻转可直接改成夹爪实验；其他任务保留为通用操作对照。',
 '此届为 ICRA，不是 IROS；新闻只列部分操作示例，不能用 7 个示例充当完整赛题总数。',
 '官方规则、基线、赛事数据公开',
 [('官方说明','https://www.agibot.com/article/231/detail/45.html'),('赛事','https://agibot-world.com/challenge2026'),('数据','https://huggingface.co/datasets/agibot-world/AgiBotWorldChallenge-2026')])

SURVEYS.append(dict(title='Research Challenges and Progress in Robotic Grasping and Manipulation Competitions',year='2021',url='https://arxiv.org/abs/2108.01483',note='从抓取与操作比赛梳理任务设计、评分与工程挑战；用于补足仅按论文检索会漏掉的赛事来源。'))

# A competition is an event edition; a track is not automatically an executable task.
COMPETITIONS=[]
def event(id,name,year,group,declared,coverage,protocol,transfer,limits,url,tracks,resources=None):
 COMPETITIONS.append(dict(id=id,name=name,year=year,group=group,declared=declared,coverage=coverage,
  protocol=protocol,transfer=transfer,limits=limits,url=url,tracks=tracks,resources=resources or [],checked='2026-10-11'))
def track(name,domain,tasks,manufacturing=False,unit='赛道',arms='待核对',horizon='待核对',operation='待核对',atomic='待核对'):
 return dict(name=name,domain=domain,tasks=tasks,manufacturing=manufacturing,unit=unit,arms=arms,horizon=horizon,operation=operation,atomic=atomic)

event('yizhi26','亦智杯·2026 亦庄具身智能开发者挑战赛',2026,'北京亦庄',
 '6 应用领域 / 12 道赛题','已核对 6 领域及新闻点名的 10 个任务例；12 道完整规则未取得',
 '仿真初赛与实景阶段；统一机器人平台；多阶段评审。',
 '保留柔性预装与物料分拣的桌面流程；医疗物流、餐饮与园区任务可作非制造长程对照。',
 '新闻中的“产业场景”包含医疗/商业等，不等于 12 道全部工业制造；任务例不与赛题逐一等同。',
 'https://kw.beijing.gov.cn/xwdt/kcyx/kcyxkchd/202606/t20260629_4733719.html',[
  track('城市运行','城市 / 应急',['展馆运营','园区运维'],unit='应用领域'),
  track('农林水务','农业',['农业种植','园林养护'],unit='应用领域'),
  track('商业服务','零售 / 餐饮',['零售餐饮'],unit='应用领域'),
  track('辅助医疗与智慧康养','医疗 / 康养',['医疗物流','医护康养'],unit='应用领域'),
  track('教育科研','教育 / 科研',['科普讲解'],unit='应用领域'),
  track('工业制造','制造',['柔性预装','物料分拣'],True,unit='应用领域')],
  [('收官报道','https://www.beijing.gov.cn/ywdt/gzdt/202608/t20260804_4807849.html'),('医疗物流实景案例','https://www.beijing.gov.cn/fuwu/lqfw/gggs/202607/t20260731_4803287.html')])
event('yizhuang25','2025 北京亦庄全域人工智能之城机器人应用场景大赛',2025,'北京亦庄',
 '已确认启动；赛道总数待核对','官方报道未提供可枚举赛道',
 '真实应用场景供给；详细任务与计分须向主办方规则回查。',
 '作为寻找现场任务、用户需求和工站条件的入口。',
 '独立于 2026 亦智杯；不能把万台机器人计划的场景数直接当成本届赛道数。',
 'https://www.beijing.gov.cn/ywdt/gzdt/202507/t20250731_4163337.html',[])
event('elder25','首届智慧健康养老机器人（北京）邀请赛',2025,'北京亦庄',
 '5 产品大类 / 14 支类','已核对 5 大类；14 支类完整清单未取得',
 '项目路演 + 场景实操演示；评技术、实用、便捷、安全和市场潜力。',
 '用康养任务检验服务流程与人机交互；直接搬到工业臂上需另定义对象与成功条件。',
 '产品类别和路演评分不等同标准化闭环操作 benchmark。',
 'https://kfqgw.beijing.gov.cn/ywdt/kjcgzhgd/kjqy/202506/t20250609_4246466.html',[
  track(n,'医疗 / 康养',[],unit='产品大类',arms='不适用',atomic='不适用',operation='不适用') for n in ['康复训练','护理照护','智能陪伴','健康监测','公共服务']])
event('warrior26','2026 机器人勇士挑战赛',2026,'北京亦庄',
 '17 项实景障碍','新闻点名 5 项障碍；完整 17 项规则未取得',
 '人形、四足与轮足；限时闯关，遥控与自主模式分别看待。',
 '固定协作臂可借鉴关阀操作；越障、搜救和导航需移动平台。',
 '不能把障碍数、参赛轮数、控制模式和赛道数相加；遥操作成绩不等于自主策略成绩。',
 'https://kfqgw.beijing.gov.cn/zwgkkfq/ztzl/lqztkfq/lqzx/zxxx/202604/t20260421_4598706.html',[
  track(n,'城市 / 应急',[],unit='障碍例',arms='待核对' if n=='紧急关阀' else '不适用',atomic='A3' if n=='紧急关阀' else '不适用',operation='直接操作' if n=='紧急关阀' else '不适用') for n in ['窄桥通行','断崖跳跃','破窗救援','紧急关阀','沙漠搜救']])
event('marathon26','2026 北京亦庄人形机器人半程马拉松',2026,'北京亦庄',
 '半程马拉松；非操作赛题库','单列移动能力赛事',
 '连续长距离运动与导航；按本届正式规则解读控制模式。',
 '可作具身能力全景背景，固定协作臂无法直接执行。',
 '补给、导览、售卖等配套场景不计入比赛赛道；不进入单臂/双臂操作矩阵。',
 'https://www.beijing.gov.cn/ywdt/gzdt/202604/t20260430_4631733.html',[
 track('半程马拉松','移动 / 导航',[],unit='竞赛项目',arms='不适用',horizon='长程',atomic='不适用',operation='不适用')])
event('humanoid25','2025 世界人形机器人运动会',2025,'北京其他赛事',
 '官方报道 26 个项目','本看板登记 4 个官方点名应用项目；非完整 26 项',
 '运动与应用项目并行；应用项目各自按场景计分。',
 '制造部分可拆成固定协作臂整理/搬运；医药分拣与迎宾保留为非制造参照。',
 '比赛举办地与北京亦庄企业参赛身份分别登记，不能称为亦庄举办。',
 'https://www.beijing.gov.cn/ywdt/gzdt/202508/t20250820_4178594.html',[
 track('工厂物料整理','制造',['工厂物料整理'],True,unit='应用项目'),
 track('物料搬运','物流',['物料搬运'],unit='应用项目'),
 track('医药拆药分拣','医疗 / 康养',['医药拆药分拣'],unit='应用项目'),
 track('迎宾技能','服务',['迎宾技能'],unit='应用项目')])
event('roco26','RoCo Assembly Challenge @ IROS 2026',2026,'IROS',
 '2 赛道','2/2 赛道已枚举',
 '方案审核、仿真与现场操作；关注感知、装配、工序依赖与恢复。',
 '工业任务板可对应插接、布线、紧固；积木赛道提供长程装配结构。',
 '规则依赛道变化；积木完成不能代表工业接触质量。',
 'https://rocochallenge.github.io/RoCo-IROS2026/',[
 track('Industrial Board Assembly','制造',['连接器插入','线缆布线','螺钉紧固','电池装配'],True,horizon='长程',operation='直接操作 / 工具操作',atomic='A3'),
 track('Brick Assembly','装配 / 教育',['定制积木结构装配'],True,horizon='长程',operation='直接操作',atomic='A2')])
event('agibot25','AgiBot World Challenge @ IROS 2025',2025,'IROS',
 '2 赛道','2/2 赛道已枚举；具体任务清单未全取',
 '操作赛道线上仿真与线下实机；世界模型赛道线上预测。',
 '10 个操作任务涵盖居家、超市、工业；根据来源子任务再标制造。',
 '生成视频的评测不能统计为机器人任务完成；两赛道数据不与主数据集规模累加。',
 'https://opendrivelab.com/challenge2025/',[
 track('Manipulation','通用操作',['抽屉收纳','倒水','动态物体打包'],True,arms='双臂',horizon='原子/短程 / 长程',operation='直接操作',atomic='A1 / A2 / A3'),
 track('World Model','世界模型',[],unit='赛道',arms='不适用',atomic='不适用',operation='不适用')])
event('robosense25','RoboSense Challenge @ IROS 2025',2025,'IROS',
 '5 赛道','5/5 赛道已枚举',
 '数据、工具包、基线与各赛道服务器；评感知稳健性与跨平台适应。',
 '可借鉴视觉扰动和传感器位置变化评测，非操作成功率基准。',
 'Track 4 官方标题为无人机跨模态导航，任务内容强调语言引导的跨视角图像检索。',
 'https://robosense2025.github.io/',[
 track(n,'感知 / 导航',[],arms='不适用',atomic='不适用',operation='不适用') for n in ['Driving with Language','Social Navigation','Cross-Sensor Placement 3D Object Detection','Cross-Modal Drone Navigation','Cross-Platform 3D Object Detection']],
 [('工具包','https://github.com/robosense2025/toolkit'),('论文','https://arxiv.org/abs/2601.05014')])
event('worldarena26','WorldArena 2.0 Challenge（IROS 2026 工作坊关联）',2026,'IROS',
 '3 赛道','3/3 赛道已由工作坊官网核对',
 '视频生成质量、交互环境用于 RL 的效用、真实机器人操作能力。',
 '关注世界模型的训练/评测效用；制造工艺质量另测。',
 '关联 workshop，不等同主会论文；挑战赛独立官网本次访问不稳定，完整规则待核对。',
 'https://physical-world-models.github.io/IROS2026/',[
 track(n,'世界模型',[],arms='待核对' if n=='实机操作' else '不适用',atomic='待核对' if n=='实机操作' else '不适用',operation='待核对' if n=='实机操作' else '不适用') for n in ['视频质量','交互 RL 效用','实机操作']])
event('ebim26','EBiM 2026 双臂社区挑战赛',2026,'国际社区',
 '3 核心任务','3/3 核心任务已枚举',
 '开放仿真 → 跨地同平台实机验证 → 结果交流；结果、过程与安全分层记录。',
 '线缆和导热垫适合制造柔性操作；辅助生活任务用于工具/人机协作对照。',
 '2026 Alpha；官方当前 workshop 日期/地点 TBD。本看板单列社区赛事，保留 IROS 双臂工作坊关联链接。',
 'https://ebim-benchmark.github.io/competition.html',[
 track('Cable Routing','制造',['线缆布线'],True,unit='核心任务',arms='双臂',horizon='长程',operation='直接操作',atomic='A3'),
 track('Thermal Pad Placement','制造',['导热垫放置'],True,unit='核心任务',arms='双臂',horizon='长程',operation='直接操作',atomic='A3'),
 track('Assisted Living & Feeding','医疗 / 康养',['辅助生活与喂食'],unit='核心任务',arms='双臂',horizon='长程',operation='工具操作',atomic='A2')])
event('agibot26','AgiBot World Challenge @ ICRA 2026',2026,'ICRA',
 '2 赛道','2/2 赛道与 7 个操作任务示例已核对',
 '推理到动作：仿真与实机；世界模型：线上视频生成。',
 '工业工件翻转、物流分拣与通用场景共库，可搭建制造与通用泛化联合评测。',
 '7 个示例不是完整赛题数；此届与 IROS 2025 分开。',
 'https://www.agibot.com/article/231/detail/45.html',[
 track('Reasoning to Action','通用操作',['物流分拣','工件翻转','货架补货与摆正','爆米花舀取','开门','清桌','双臂端锅'],True,arms='双臂',horizon='原子/短程 / 长程',atomic='A1 / A2 / A3',operation='直接操作 / 工具操作'),
 track('World Model','世界模型',[],arms='不适用',atomic='不适用',operation='不适用')])

# Multi-domain coverage is independent from manufacturing applicability.
DOMAIN_MAP={
 'nist':['制造'],'fmb':['制造'],'furniture':['装配 / 家具'],'ramp':['制造'],'factory':['制造'],
 'industreal':['制造'],'forge':['制造'],'automate':['制造'],'fabrica':['制造'],'roco':['制造'],
 'roco-iros':['制造','装配 / 教育'],'workbench':['装配 / 教育'],'assemblybench':['装配 / 家具'],
 'ariac':['制造','物流'],'hail':['制造','通用操作'],'robotwin':['通用操作','居家','餐饮','工具'],
 'robofactory':['通用操作','装配'],'robosuite':['通用操作','装配'],'maniskill':['通用操作','居家'],'rlbench':['通用操作','居家','工具'],
 'calvin':['居家'],'libero':['居家'],'liberoplus':['居家'],'liberopro':['居家'],'liberovpro':['居家'],
 'vlabench':['通用操作','居家','工具'],'bigym':['居家'],'behavior':['居家'],'robocasa':['居家','餐饮'],
 'robolab':['通用操作'],'mimicgen':['通用操作','装配'],'dexmimicgen':['通用操作','装配'],
 'skillmimicgen':['通用操作'],'droid':['通用操作','居家'],'bridge':['居家','餐饮'],'oxe':['通用操作'],
 'agibot':['制造','物流','零售','餐饮','居家'],'umi':['居家','通用操作'],'ego4d':['日常活动'],
 'egoexo':['日常活动','运动'],'egomimic':['居家'],'egodex':['日常活动'],'egoverse':['日常活动'],
 'taco':['工具'],'industreal-human':['装配 / 维护'],'duobench':['通用操作','装配'],
 'robodojo':['居家','餐饮','工具','通用操作'],'embodichain':['通用操作','餐饮','经典控制'],
 'ebim':['制造','医疗 / 康养'],'geniesim':['制造','零售','餐饮','居家','办公'],
 'agibot-challenge25':['制造','零售','居家','世界模型'],'agibot-challenge26':['制造','物流','零售','餐饮','居家','世界模型']}
for r in RECORDS:
 r['domains']=DOMAIN_MAP.get(r['id'],['通用操作'])
 r['source_type']='挑战赛' if r['id'] in ['ariac','roco-iros','ebim','agibot-challenge25','agibot-challenge26'] else '论文 / 项目'
