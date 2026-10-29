"""RoboColiseum's current boards, distinct from Colosseum (2024)."""
from pathlib import Path
import json
from ecosystem_data import RECORDS, SURVEYS, COMPETITIONS, event, track
from research_data import add

add('libero-industry','LIBERO-Industry',2026,'2026-10 预印本','Benchmark|Dataset','单臂','A2|A3','长程','直接操作','智能制造',
 'MuJoCo / robosuite；真实 AUBO-i5H','216 个参数化任务：训练 180，评测 36',
 '静态到动态上料、动态到静态卸料、动态到动态转运；改变工件、速度、操作窗口和放置容差。',
 '适合研究动态上料、限时多工件转运、几何公差及工艺约束下的泛化；对照整任务成功率和目标转移完成率。',
 '实机仅验证动态到静态工站；双臂支持仍开发中。评测的五个模型各 360 次 rollout 整任务成功率均为 0%，不代表所有工业任务或训练方法均为零。',
 '论文、代码和 HDF5 数据入口公开；未在本地运行',
 [('论文','https://arxiv.org/abs/2610.16782'),('代码 / 安装','https://github.com/IAIE-PhysicalAI/LIBERO-Industry'),('HDF5 数据','https://huggingface.co/datasets/cindysung/LIBERO-industry-datasets')],
 '论文实机数据 95 条示范；官方另列 LeRobot v2.1 页面，检索时显示空。')
RECORDS[-1].update(domains=['制造','物流'],source_type='论文 / 开源项目',checked='2026-10-29')

REPO='https://github.com/AgibotTech/genie_sim'
SOURCE=REPO+'/blob/main/README.md#52--genie-sim-benchmark-leaderboard'
DEFINITIONS=json.loads((Path(__file__).resolve().parent/'task_definitions.json').read_text(encoding='utf8'))
BOARD_TASKS={}
for name,title in [('指令遵循','Instruction'),('通用操作','Manipulation'),('空间推理','Spatial')]:
 BOARD_TASKS[name]=[t['name'] for t in DEFINITIONS if t['source']=='RoboColiseum 持续评测榜单' and t['group']==name]
assert [len(v) for v in BOARD_TASKS.values()]==[10,10,8]

add('robocoliseum','RoboColiseum',2026,'智元 / Genie Sim 官方持续评测',
 'Benchmark|Platform','双臂','A1|A2','原子/短程|长程','直接操作|工具操作','',
 'Genie Sim Benchmark / Isaac Sim；Genie G2 双臂平台',
 '4 类榜单；README 枚举 28 个命名任务；鲁棒性另列 5 类扰动',
 '指令选物、空间摆放、堆叠、工件倾倒、货架整理、包裹分拣、舀取和连续分拣。双臂平台不代表每个任务必须双臂。',
 '适合检验语言约束、视觉扰动、定向上料和连续分拣。制造实验可在工件倾倒后加入姿态检测、批次计数和异常回收。',
 '榜单为子任务完成度聚合，不能直接当作整条任务成功率。鲁棒性扰动不是新增操作任务；与 Genie Sim 共用任务与数据，跨资源不能重复相加。另有 Colosseum / robot-colosseum（2024，RLBench），属于不同项目。',
 '官方在线榜单、离线评测代码与配套数据入口公开',
 [('官方榜单','https://robocoliseum.ai/'),('任务 / 评分',SOURCE),('离线运行',REPO+'/blob/main/source/geniesim_benchmark/USAGE.md'),
  ('官方数据下载脚本',REPO+'/blob/main/source/geniesim_benchmark/skills/robocoliseum/challenge-download-datasets/scripts/download_dataset.sh'),
  ('平台论文','https://arxiv.org/abs/2601.02078')],
 '复用 GenieSim3.0-Dataset；脚本支持 instruction / manipulation / sim2real，空间与鲁棒性训练包覆盖另核对。')
RECORDS[-1].update(domains=['通用操作','制造','物流','零售','餐饮'],source_type='挑战赛')
tracks=[track(name,'制造 / 物流 / 通用操作' if name=='通用操作' else '通用操作',names,
 manufacturing=name=='通用操作',arms='双臂',horizon='长程' if name=='通用操作' else '待核对',operation='直接操作 / 工具操作' if name=='通用操作' else '直接操作',atomic='A1 / A2') for name,names in BOARD_TASKS.items()]
tracks.insert(1,track('鲁棒性','通用操作',['指令','机器人位姿','背景','图像质量','相机位置'],unit='扰动维度',arms='双臂'))
event('robocoliseum26','RoboColiseum 持续评测榜单',2026,'智元 / RoboColiseum',
 '4 榜单：instruction / robust / manip / spatial',
 '28 个命名任务来自指令 / 操作 / 空间表；5 类鲁棒性扰动单列。持续榜单不按 4 次独立赛事计数。',
 '对接策略推理服务，离线调试后在线提交；按官方子任务完成度与套件协议评分。',
 '将工件倾倒、连续分拣等映射为桌面上料 / 分拣工站；用指令与空间任务作非制造对照。',
 'GenieSim-Sim2Real 的 8 项对照实验是独立验证表，不作为第五个竞赛榜单；在线榜单开放状态以平台为准。',
 'https://robocoliseum.ai/',tracks,[('官方任务表',SOURCE),('评测运行说明',REPO+'/blob/main/source/geniesim_benchmark/USAGE.md')])
COMPETITIONS[-1].update(platforms=['智元','RoboColiseum'],evaluation='机器人操作',organizers='智元 Genie Sim 团队',
 models='开放策略提交；参考模型见官方榜单',period='2026-06-25 官方发布记录；持续评测',state='公开榜单；提交状态以平台为准')

def append_tasks(task):
 for group,names in BOARD_TASKS.items():
  for name in names:
   atomic='A2' if group=='通用操作' or name in ['straighten_object','Stack Bowls','Stack Three Building Blocks','Sort Cubes by Size','Sort Number'] else 'A1'
   horizon='长程' if name=='Sorting Packages Continuous' else '待核对' if group=='通用操作' or name in ['Sort Cubes by Size','Sort Number'] else '原子/短程'
   op='工具操作' if name=='Scoop Popcorn' else '待核对' if name=='Clean the Desktop' else '直接操作'
   domain='制造' if name=='Pour Workpiece' else '物流' if name.startswith('Sorting Packages') else '零售' if 'Shelf' in name else '餐饮' if name in ['Hold Pot','Scoop Popcorn'] else '通用操作'
   task('RoboColiseum 持续评测榜单',name,'双臂',atomic,horizon,op,domain,False,group,SOURCE,
    '官方 README 榜单命名任务；保留原名。双臂描述为 Genie G2 平台；未推断每项均需双臂。难度与任务链为本报告初筛；扰动 / sim2real 验证表不重复计入。')
