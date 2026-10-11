"""Platform-hosted challenges. Hosts, models, tasks and editions stay distinct."""
from revision_data import RECORDS, SURVEYS, COMPETITIONS, event, track
from research_data import add

TIANCHI='阿里云天池'
PADDLE='百度 / 飞桨'
LINGBO='蚂蚁灵波'
QWEN='Qwen / 通义千问'
MODELSCOPE='魔搭社区'
KDC='https://kdc-doc.netlify.app/tianchi/cn/pages/tasks'
REALI='https://kdc-doc.netlify.app/icra/en/pages/tasks'
OPENLET='https://tianchi.aliyun.com/competition/entrance/532515/introduction'
LINGBOT='https://tianchi.aliyun.com/competition/entrance/532514/introduction'
POWER='https://ai.baidu.com/support/news?action=detail&id=3013'

def metadata(platforms,kind,organizers,models='',period='',state=''):
 e=COMPETITIONS[-1]
 e.update(platforms=platforms,evaluation=kind,organizers=organizers,models=models,period=period,state=state)

event('lingbot26','蚂蚁灵波具身大模型挑战赛',2026,'天池 / 灵波',
 '线上初赛 + 线下真机黑客马拉松','阶段不是两个独立 benchmark；使用 RoboTwin 2.0 统一任务，未取得赛事完整任务子集',
 '线上复现、训练调优与泛化评测；线下真机适配。官方要求 RoboTwin 2.0 clean 数据，不能以 randomized 数据训练。',
 '优先复用已有 RoboTwin 任务注册表与双臂评测接口，再对自有 URDF 和相机标定做迁移。',
 '灵波为蚂蚁生态；天池与魔搭共同发起。模型、承载平台、本体供应商分别注明；RoboTwin 50 项不再按此赛事重复计数。',
 LINGBOT,[track('线上初赛','通用操作',['RoboTwin 2.0 标准任务；完整参赛子集待核对'],arms='双臂',operation='直接操作 / 工具操作'),
 track('线下真机黑客马拉松','通用操作',['真机任务与部署验证；完整规则待核对'],unit='赛段')],
 [('RoboTwin 数据','https://huggingface.co/datasets/TianxingChen/RoboTwin2.0'),('天池赛事目录','https://tianchi.aliyun.com/competition/')])
metadata([TIANCHI,LINGBO,MODELSCOPE],'机器人操作','蚂蚁灵波科技、魔搭社区、阿里云天池共同发起',
 'LingBot-VLA 2.0','2026-09-11—11-15；线下 11-13—15','截至 2026-10-11：进行中；线下阶段尚未开始')

event('openlet26','OpenLET 具身智能挑战赛','2026—2027','天池 / OpenLET',
 '3 项任务；冬季仿真、春季仿真＋真机、年度真机总决赛','已核对阶段、榜单与组织；3 项当前赛季完整任务名待核对',
 '各任务 100 分；综合榜仿真 30%、真机 70%；冬季仅仿真。总决赛现场重新计分，前期成绩不带入。',
 '可借鉴工业后训练、自动评测与远程实机验证；首期做抓取—交接—称重—定向放置工站。',
 '不同赛段、榜单、城市不是新增任务；不把第一届天池或 ICRA 的任务清单代填为本赛季 3 项赛题。',
 OPENLET,[track('冬季仿真','制造',[],True,unit='赛段'),track('春季仿真＋真机','制造',[],True,unit='赛段'),
 track('年度真机总决赛','制造',[],True,unit='赛段')],[('数据社区','https://openlet.openatom.tech/')])
metadata([TIANCHI,LINGBO,'OpenLET'],'机器人操作',
 '主办：开放原子开源基金会 / OpenLET 社区；承办：乐聚、蚂蚁灵波；协办含阿里云天池',
 '指定数据、模型、工具版本以本赛季资源表为准',
 '冬季 2026-09-29—12-31；春季 2027-01-01—03-31；决赛计划 2027-05-24—28',
 '截至 2026-10-11：冬季仿真进行中；后续阶段为计划')

event('kuavo-tianchi25','乐聚机器人第一届具身智能操作任务挑战赛 & 创业启航营','2025—2026','天池 / 乐聚',
 '手册：4 个仿真任务 + 3 个真实场景任务','7 个阶段-任务定义完整登记；不宣称等于跨版本全部赛题',
 '仿真先筛选，真机验证；按阶段完成、姿态与时间计分；rosbag 数据转训练格式，Docker 提交评测。',
 '最贴近夹爪协作臂工站：传送带抓取、称重、定姿分拣；汽车大件需按负载与空间缩小。',
 '采用当前天池手册的 4+3 清单；后续赛季与 ICRA 规则另列。双臂人形平台不能直接视为任意单臂即插即用。',
 'https://tianchi.aliyun.com/competition/entrance/532415',
 [track('仿真阶段','制造',['移动目标抓取','移动物体称重','物体定姿摆放','全流程分拣'],True,unit='赛段',arms='双臂',operation='直接操作',atomic='A1 / A2'),
 track('实机阶段','制造',['桌面物料分拣','工业零件称重','汽车大件上料'],True,unit='赛段',arms='双臂',operation='直接操作',atomic='A1 / A2')],
 [('任务手册',KDC),('数据手册','https://kdc-doc.netlify.app/tianchi/cn/pages/datasets'),('届次入口关联','https://tianchi.aliyun.com/forum/issue/927757')])
metadata([TIANCHI,'OpenLET'],'机器人操作','赛事手册由乐聚发布；天池承载比赛与提交；完整联合主办名单以届次规则为准',
 '手册提供 Diffusion Policy / ACT 等基线；不自动归为 Qwen 比赛','2025 届启动；手册快照 2026-10-11','赛程状态未在已取得手册中确认')

event('reali26','REAL-I · ICRA 2026 真机具身学习挑战赛',2026,'ICRA',
 '手册：仿真 3 项 / 远程真机 3 项 / 现场 3 项','9 个阶段-任务定义；同类翻面与扫描在不同协议下分别登记',
 '阶段任务独立计分；现场部分设 Level 1/2，涉及移动传送带、连续物件、双臂空中交接。',
 '直接支持工业件翻面、动态分拣、日化上料；称重、扫码属于借助工站设备的联合流程。',
 '数据卡的 real 目录标 not updated yet，名称与现行手册不一致：数据卡不能代替评测规范。现场 Level 1/2 不是两个新增语义任务。',
 'https://www.kdc.icra.lejurobot.com/',
 [track('仿真阶段','通用操作',['Toy Sorting','Parcel Weighing','Conveyor Belt Parts Sorting'],True,unit='赛段',arms='双臂',operation='直接操作',atomic='A1 / A2'),
 track('远程真机阶段','制造 / 物流',['Small Part Flipping','Express Package Scanning','Bottling'],True,unit='赛段',arms='双臂',operation='直接操作',atomic='A2'),
 track('现场阶段','制造 / 物流',['Metal Parts Righting','Daily Chemical Bottle Pick & Place','Express Package Scanning'],True,unit='赛段',arms='双臂',operation='直接操作',atomic='A2')],
 [('任务手册',REALI),('赛事数据卡','https://huggingface.co/datasets/LejuRobotics/kuavo_data_challenge_icra/blob/main/README.md'),
 ('基金会赛事回顾','https://openatom.cn/journalism/detail/LSJBItXNcOYR')])
metadata(['OpenLET','ICRA'],'机器人操作','乐聚与开放原子社区赛事来源；联合组织名单以官方赛事页为准',
 'Kuavo 数据、任务脚本及学习基线','ICRA 2026；现场任务按当前公开手册','2026 届已举办；本看板不统计参赛成绩')

event('tianchi-extreme26','2026 具身极限挑战赛（系列）',2026,'阿里云天池',
 '3 个具身子赛：仿真合成 / 安全应用 / 跨本体认知','系列按 1 个赛事条目登记，子赛列 3 行；不再把系列与子赛相加',
 '分别评测资产生成质量、安全闭环鲁棒性与跨本体泛化；安全赛有 6 类攻击环节及简单/中等/困难设置。',
 '用于自有工件视频转仿真资产、Piper / R1 / CR5 跨本体实验、工站异常与恢复协议。',
 '6 类攻击环节不是 6 个操作任务；资产生成分数不是机器人执行成功率。当前未取得三个子赛的完整执行任务表与全部规则。',
 'https://tianchi.aliyun.com/competition/activeList',
 [track('2026 具身仿真合成挑战赛','仿真资产',['多设备物体视频 → 几何、外观、物理与交互可信的仿真资产'],unit='子赛',arms='不适用',horizon='不适用',operation='不适用',atomic='不适用'),
 track('2026 具身安全应用挑战赛','安全',['视觉感知、空间感知、任务决策、控制通信、状态估计、执行反馈：6 类攻击环节'],unit='子赛'),
 track('2026 跨本体具身认知极限联合挑战赛','跨本体泛化',['多本体、多环境下的泛化；完整任务清单待核对'],unit='子赛',arms='配置可变')])
metadata([TIANCHI],'生成 / 安全 / 泛化','天池官方目录承载；各子赛主办方与技术伙伴名单待独立核对',
 '未确认统一指定 Qwen 或 LingBot；不按平台关联推断模型',
 '系列 2026-08-06—11-30；合成 / 安全子赛目录标 07-30—11-15','截至 2026-10-11：2026 赛期内；子赛节点分别核对')

event('qwen-first','通义千问 AI 挑战赛（首届）','2023—2024','Qwen / 魔搭 / 天池',
 '2 赛道：Code Qwen / Agent Builder','公开算法和创意应用赛；无统一闭环机械臂任务清单',
 'Code Qwen 对模型做数据与微调优化；Agent Builder 提交基于模型与框架的应用。',
 '适合作为任务规划、代码助手与工具调用原型参考；机器人效果需另做闭环实机测试。',
 '软件 Tool Call 不计为机械臂持工具操作；不能将所有 Agent 作品归为制造 benchmark。',
 'https://tianchi.aliyun.com/specials/promotion/Qwen',
 [track('Code Qwen 能力算法赛道','代码模型',['通义千问微调与代码能力优化'],arms='不适用',horizon='不适用',operation='不适用',atomic='不适用'),
 track('Agent Builder 创意挑战赛道','开放应用',['Qwen + 魔搭 Agent-Builder 的应用设计'],arms='不适用',horizon='不适用',operation='不适用',atomic='不适用')],
 [('Agent 赛道入口','https://tianchi.aliyun.com/competition/entrance/532169')])
metadata([TIANCHI,MODELSCOPE,QWEN],'开放应用 / 算法','官方专题：阿里云与 NVIDIA；魔搭 / 天池承办',
 'Qwen、Code Qwen、Agent-Builder','首届历史赛事；专题与赛道入口保留','历史赛事；不按网站抓取时间重记为 2026 届')

event('ernie25','ERNIE AI Developer Challenge',2025,'百度 / 飞桨',
 '3 类开发任务；8 个具体方向','Warm-up 1 / Model-Building 3 / Application-Building 4；奖项数不当作赛道数',
 '在线开发并提交作品、代码与演示；含模型微调、OCR、多模态、边缘机器人与多智能体方向。',
 '边缘视觉与机器人部署可参考 RDK X5；夹爪动作控制、接触力与长期执行仍需自行定义评测。',
 '只有部分方向涉及机器人。赛事开放作品未提供统一单臂/双臂 benchmark；不加入具体机器人任务分母。',
 'https://baiduernieai.devpost.com/',
 [track('Warm-up','OCR / 文档',['PaddleOCR + ERNIE：PDF 转网页'],unit='任务类别',arms='不适用',horizon='不适用',operation='不适用',atomic='不适用'),
 track('Model-Building','模型训练',['Unsloth ERNIE 微调','LLaMA-Factory ERNIE 微调','PaddleOCR-VL 微调'],unit='任务类别',arms='不适用',horizon='不适用',operation='不适用',atomic='不适用'),
 track('Application-Building','开放应用 / 边缘机器人',['百度 API 多模态应用','Novita API 应用','D-Robotics RDK X5 边缘 AI 与机器人','CAMEL-AI 多智能体'],unit='任务类别',arms='不适用',horizon='不适用',operation='不适用',atomic='不适用')],
 [('完整规则','https://baiduernieai.devpost.com/rules'),('飞桨社区线下活动回顾','https://pfcc.blog/posts/japan-hackathon')])
metadata([PADDLE],'开放应用 / 算法','Baidu；赛事规则列开发工具与硬件生态伙伴',
 'ERNIE、PaddleOCR、PaddleOCR-VL','2025-11-18—12-23','已结束；东京线下活动归入本赛事，不额外加一届')

event('paddle-robot25','2025 国际自主智能机器人大赛',2025,'百度 / 飞桨',
 'AI Studio 官方赛事入口','已确认赛事标题与入口；公开抓取未取得完整赛道规则',
 '评测流程与任务表待核对。',
 '保留入口供继续追踪；取得任务规范后再判断是否适合夹爪协作臂。',
 'AI Studio 是承载平台，不据此认定百度独立主办；不编造赛道数量或制造标签。',
 'https://aistudio.baidu.com/competition/detail/1421',[])
metadata([PADDLE],'待核对','主办与合作机构名单待核对','未确认指定模型','2025 届','入口已确认；规则覆盖待补')

event('paddle-power23','中国软件杯 2023 · 智能四足机器狗电力巡检系统开发',2023,'百度 / 飞桨',
 '1 个机器人赛题；预选、区域、总决赛','百度 2023-04-06 官方赛题汇总；不是机械臂装配任务',
 '预选做仪表、火点、安全帽识别；区域与总决赛用 Go1 在规定地图完成自动巡检、避障及任务，按质量和时间计分。',
 '工业视觉巡检、异常识别与移动技能；可转成协作臂工站相机检测对照。',
 '能源巡检单列领域，不标为制造装配。感知预选与地图实机阶段不能共用成功率。',
 POWER,[track('智能四足机器狗电力巡检','能源 / 巡检',['仪表识别','火点识别','安全帽识别','自主巡检与避障'],unit='赛题',arms='不适用',horizon='待核对',operation='不适用',atomic='不适用')],
 [('AI Studio 赛题','https://aistudio.baidu.com/aistudio/competition/detail/771/0/introduction'),
 ('训练数据','https://aistudio.baidu.com/aistudio/datasetdetail/199384'),('基线','https://aistudio.baidu.com/aistudio/projectdetail/5718676')])
metadata([PADDLE],'移动 / 感知','中国软件杯赛题；百度飞桨提供技术、平台与硬件支持',
 'PaddlePaddle / EdgeBoard；宇树 Go1','2023 届；预选—区域—总决赛','历史赛事；保留实机地图协议参考')

event('paddle-rescue23','2023 中国大学生计算机设计大赛 · 智慧救援挑战赛',2023,'百度 / 飞桨',
 '智慧救援赛题；线上识别与实机地图','飞桨官方账号发布赛题；完整地图与子任务谓词待核对',
 '线上灾害元素识别；实机机器狗在地图中完成救援场景指定任务。',
 '可作为非制造长程与异常场景对照；视觉识别与物理执行分别评测。',
 '飞桨作者来源位于 SegmentFault；不把新闻任务例写成完整 benchmark；本体为机器狗，机械臂难度不适用。',
 'https://segmentfault.com/a/1190000043422298',
 [track('智慧救援','应急 / 救援',['灾害场景元素识别','实机地图救援任务'],unit='赛题',arms='不适用',operation='不适用',atomic='不适用')])
metadata([PADDLE],'移动 / 感知','计算机设计大赛相关赛题；百度飞桨技术生态支持',
 'PaddlePaddle；机器狗平台','2023 届','历史赛事；完整赛题覆盖待补')

event('paddle-car23','第十八届全国大学生智能汽车竞赛 · 百度完全模型组竞速赛',2023,'百度 / 飞桨',
 '百度完全模型组竞速赛','仅登记百度官方汇总明确点名的组别；不代表整个智能汽车竞赛全部组别',
 '线上指定飞桨与 AI Studio 做模型设计、训练、预测；线下使用指定 EdgeBoard，涉及车道定位和目标识别。',
 '适合研究移动工站、视觉控制与边缘部署；桌面夹爪课题只借鉴感知与工程管线。',
 '车辆组不归为机械臂搬运；未把风电预测和医疗分割等非机器人赛题纳入此目录。',
 POWER,[track('百度完全模型组竞速赛','移动机器人',['视觉模型训练','车道定位与识别','自动行驶'],unit='组别',arms='不适用',operation='不适用',atomic='不适用')])
metadata([PADDLE],'移动 / 感知','全国大学生智能汽车竞赛相关组别；百度技术与硬件支持',
 'PaddlePaddle、AI Studio、EdgeBoard','2023 第十八届','历史赛事；与巡检赛共享官方汇总来源，任务不同')

# Only robot-task resources enter the scientific catalog; coding hackathons stay in events.
add('lingbot-challenge26','LingBot-VLA 2.0 Challenge',2026,'天池 / 蚂蚁灵波 / 魔搭','Benchmark|Dataset',
 '双臂','A1|A2','原子/短程|长程','直接操作|工具操作','可迁移','RoboTwin 2.0 + 真机',
 '线上 + 线下两阶段；任务子集待核对','通用双臂操作、训练调优、泛化与真机部署。',
 '与 Piper 类双臂部署相关；与已有 RoboTwin 任务注册表共享来源。',
 '数据限定 clean；不能重复累加 RoboTwin 50 个任务。无证据将整个赛事归为智能制造。',
 '赛事规则与训练数据入口公开；2026-10-11 进行中',
 [('赛事规则',LINGBOT),('训练数据','https://huggingface.co/datasets/TianxingChen/RoboTwin2.0')],
 '赛事训练与测试分割按本届规则；RoboTwin 数据与赛事数据角色分别说明。')
add('openlet-community','OpenLET 数据社区 / 2026—2027 挑战赛',2026,'开放原子 / 乐聚 / 蚂蚁灵波 / 天池',
 'Benchmark|Dataset|Platform','双臂|配置可变','A1|A2','原子/短程|长程','直接操作','智能制造',
 '仿真 + 真机 / 数据与后训练工具','社区声明 10,000+ 分钟真机数据、6 个真机任务；本赛季规则另称 3 项任务',
 '抓取、交接、翻面、扫描与工业作业；社区覆盖工业、零售、居家。',
 '用于本土协作臂数据格式、后训练与真机评测工站设计。',
 '社区任务数、赛季任务数及历史比赛任务不能相加；6 项名称未完整取得。数据、LET-Tool 与 LET-Brain 版本分别固定。',
 '官方社区入口与挑战规则公开；公开声明规模未独立复现',
 [('社区','https://openlet.openatom.tech/'),('赛事规则',OPENLET)],
 '社区汇集 LET-Data；下载许可、观察字段与本体版本需逐个数据包核对。')
add('kuavo-tianchi','Kuavo Tianchi Challenge 数据与任务',2025,'第一届天池 / 乐聚赛事手册',
 'Benchmark|Dataset','双臂','A1|A2','原子/短程|长程','直接操作','智能制造',
 'MuJoCo / Kuavo 人形双臂 + 真机','手册枚举 4 仿真 + 3 实机任务',
 '动态目标抓取、称重、定姿、全流程分拣；实机物料分拣、工业零件称重、汽车大件上料。',
 '可缩成桌面夹爪工站；保留姿态判定与按阶段计分。',
 '汽车大件需按夹爪、负载和可达范围缩放；天池历史手册与后续赛事分别记录。',
 '任务、数据格式、基线、提交与评测手册公开',
 [('任务',KDC),('数据','https://kdc-doc.netlify.app/tianchi/cn/pages/datasets'),('天池','https://tianchi.aliyun.com/competition/entrance/532415')],
 'rosbag；按任务手册采集观察与机器人状态，训练转换参见手册；轨迹规模不在本条估计。')
add('reali-kuavo','REAL-I 2026 / Kuavo Challenge Dataset',2026,'ICRA 2026 / 乐聚 / OpenLET',
 'Benchmark|Dataset','双臂','A1|A2','原子/短程|长程','直接操作','智能制造',
 'Kuavo 4 Pro；仿真 / 远程真机 / 现场','手册 9 个阶段-任务定义；数据卡称每任务 1,000 episodes，real 尚未更新',
 '玩具分类、包裹称重、工业件分拣、翻面、扫码与日化上料；现场包含双臂空中交接。',
 '工业件定向、流水线送料、扫码及称重联合流程均适合夹爪平台缩比验证。',
 '数据卡列 real 任务与现行手册不一致；不直接累乘成已下载轨迹总数。9 项有跨阶段语义重叠。',
 '公开任务手册与数据卡；版本差异明确标出',
 [('手册',REALI),('数据卡','https://huggingface.co/datasets/LejuRobotics/kuavo_data_challenge_icra/blob/main/README.md'),('赛事','https://www.kdc.icra.lejurobot.com/')],
 '以 rosbag 保留传感器与状态；sim 数据与 real 目录发布状态分开，不能把未更新目录当成已开放训练集。')
for r in RECORDS:
 if r['id'] in {'lingbot-challenge26','openlet-community','kuavo-tianchi','reali-kuavo'}:
  r['domains']=['通用操作'] if r['id']=='lingbot-challenge26' else ['制造','物流','通用操作']
  r['source_type']='挑战赛'
for e in COMPETITIONS:
 e.setdefault('platforms',[e['group']])
 e.setdefault('evaluation','移动 / 感知' if e['id'] in {'robosense25','warrior26','marathon26'} else '综合赛事' if e['id']=='humanoid25' else '场景应用 / 展示' if e['id']=='elder25' else '待核对' if e['id']=='yizhuang25' else '机器人操作')
 e.setdefault('organizers','见本届官方来源；赛事关联与主办机构分别核对')
 e.setdefault('models','未确认统一指定模型')
 e.setdefault('period',str(e['year'])+' 届；详细节点见官方来源')
 e.setdefault('state','按来源快照登记；不由年份推断报名状态')
