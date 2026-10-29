"""Source-attributed task definitions, buildable without downloaded paper snapshots."""
import json
from pathlib import Path
from coliseum_data import RECORDS, COMPETITIONS
TASKS=json.loads((Path(__file__).resolve().parent/'task_definitions.json').read_text(encoding='utf8'))

# Every resource has a family coverage row, including human data and generators.
FAMILIES=[dict(id=r['id'],name=r['name'],tasks=r['tasks'],arms=r['arms'],atomic=r['atomic'],
 horizon=r['horizon'],operation=r['operation'],domains=r['domains'],manufacturing=r['manufacturing'],scale=r['scale']) for r in RECORDS]
COVERAGE=[
 dict(source='LIBERO-Industry',declared='216 参数化任务：180 训练 / 36 评测',enumerated='未逐项枚举',status='三种工站各 72 个条件组合；尚未逐条导入任务表，不能加入已枚举任务数。'),
 dict(source='RoboColiseum',declared='4 榜单；28 个命名任务 / 5 类扰动',enumerated=28,status='指令 10 + 操作 10 + 空间 8；扰动维度与 sim2real 对照实验不累加；与 Genie Sim 共源'),
 dict(source='RoboDojo · 仿真',declared='42 个评测任务',enumerated=42,status='完整（不含训练专用 DLC）'),
 dict(source='RoboDojo · 实机',declared='18 个平台-任务定义',enumerated=18,status='完整；与仿真分开计数'),
 dict(source='LIBERO',declared='130 个注册任务',enumerated=130,status='完整；LIBERO-10 不额外累加'),
 dict(source='RoboTwin 2.0',declared='50 个注册任务',enumerated=50,status='完整；clean / randomized 不重复累加'),
 dict(source='RoCo IROS 2026',declared='2 赛道',enumerated=5,status='官方点名操作 / 装配任务，未宣称完整底层实例'),
 dict(source='EBiM 2026',declared='3 核心任务',enumerated=3,status='完整核心任务'),
 dict(source='AgiBot ICRA 2026',declared='操作任务总数未单列',enumerated=7,status='官方任务示例；非完整题库'),
 dict(source='乐聚天池首届',declared='4 仿真 + 3 实机',enumerated=7,status='手册完整清单；与后续赛季分开'),
 dict(source='REAL-I ICRA 2026',declared='3 仿真 + 3 远程真机 + 3 现场',enumerated=9,status='阶段-任务定义；数据卡与手册差异已注明'),
 dict(source='LingBot-VLA 2.0 Challenge',declared='使用 RoboTwin 2.0；参赛子集待核对',enumerated='未重复计数',status='RoboTwin 已列 50 项；不按平台与赛事重复累加'),
 dict(source='OpenLET 2026—2027',declared='3 项任务',enumerated='待核对',status='未取得本赛季完整任务名，不以历史赛题代填'),
 dict(source='天池具身极限 / 百度飞桨 / Qwen',declared='含生成、安全、感知与开放应用方向',enumerated='不混入操作任务',status='赛道和开发方向保留在赛事目录；不是机器人闭环任务清单'),
]
assert len({t['id'] for t in TASKS})==len(TASKS)
