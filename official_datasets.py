"""Dataset entities linked to resource records; subsets/formats never add benchmark tasks."""
from copy import deepcopy

LIBERO_REPO='https://github.com/Lifelong-Robot-Learning/LIBERO'
LIBERO_HF='https://huggingface.co/datasets/yifengzhu-hf/LIBERO-datasets'
OVERRIDES={
 'fmb':dict(name='FMB 官方操作与装配示范',kind='训练示范',mode='实机',
  url='https://functional-manipulation-benchmark.github.io/dataset/index.html',
  scope='单物体操作与多物体装配数据包；格式与文件划分见官方数据页。'),
 'furniture':dict(name='FurnitureBench 官方示范',kind='训练示范',mode='实机',
  url='https://clvrai.github.io/furniture-bench/docs/tutorials/dataset.html',
  scope='按家具类型与 low / medium / high 初始随机化组织；成功示范，不是仿真自动生成数据。'),
 'automate':dict(name='AutoMate · 100 组装配几何',kind='装配几何 / 资产',mode='资产',
  url='https://github.com/isaac-sim/IsaacGymEnvs/blob/automate/docs/automate.md#dataset',
  scope='官方提供 100 组可仿真与可 3D 打印的装配网格；不把网格数当成人工控制轨迹数。'),
 'roco':dict(name='RoCo 官方齿轮箱装配数据',kind='训练示范',mode='混合',
  url='https://huggingface.co/datasets/rocochallenge2025/rocochallenge2025',
  source='https://github.com/rocochallenge/roco_dataset_devkit#dataset-download',
  scope='包含 Galaxea R1 / R1 Lite 的仿真与真实数据分目录；AAAI 数据不自动当作 IROS 2026 赛题数据。'),
 'assemblybench':dict(name='AssemblyBench 官方合成数据',kind='几何轨迹 / 图文',mode='资产',
  url='https://zenodo.org/records/19742725',source='https://github.com/merlresearch/AssemblyBench#dataset--checkpoint-download',
  scope='图文说明、部件几何与部件 6-DoF 装配轨迹；不是机械臂关节动作。'),
 'hail':dict(name='HAIL · 论文描述的示范数据',kind='训练示范',mode='实机',available=False,
  scope='论文描述真实示范；本次没有核实可下载的官方公开数据包。'),
 'robotwin':dict(name='RoboTwin 2.0 官方预采集示范',kind='训练示范',mode='仿真',
  url='https://huggingface.co/datasets/TianxingChen/RoboTwin2.0/tree/main/dataset',
  source='https://github.com/RoboTwin-Platform/RoboTwin#dataset',
  scope='仿真预采集数据；下载时区分任务、本体、clean / randomized 配置。论文实机实验不等于数据包全部为实机。',
  scale='官方 README 声明 100,000+ 条预采集轨迹'),
 'maniskill':dict(name='ManiSkill 官方 Demonstrations',kind='训练示范',mode='仿真',
  url='https://huggingface.co/datasets/mani-skill/ManiSkill_Demonstrations',
  source='https://maniskill.readthedocs.io/en/latest/user_guide/datasets/demos.html',
  scope='按 ENV_ID 下载；可用任务以下载器列出的条目为准。精简数据可能只保存动作与环境状态，视觉观察通过回放生成。',
  command='python -m mani_skill.utils.download_demo ENV_ID'),
 'liberoplus':dict(name='LIBERO-Plus 官方训练数据',kind='训练示范',mode='仿真',
  url='https://huggingface.co/datasets/Sylvest/libero_plus_data_4suite',
  source='https://github.com/sylvestf/LIBERO-plus',
  scope='四套件训练数据；RLDS 与 LeRobot 为作者提供的表示格式，同源数据不能因格式不同重复计数。与 10,030 个扰动评测实例分开。',
  extra=[('RLDS 格式','https://huggingface.co/datasets/Sylvest/libero_plus_rlds'),
         ('LeRobot 格式','https://huggingface.co/datasets/Sylvest/libero_plus_lerobot')],
  scale='四套件训练数据；轨迹数量按下载版本核对'),
 'liberopro':dict(name='LIBERO-PRO 官方评测配置',kind='评测配置',mode='仿真',
  url='https://huggingface.co/datasets/zhouxueyang/LIBERO-Pro',source='https://github.com/Zxy-MLlab/LIBERO-PRO',
  scope='作者发布 BDDL 与初始状态文件，供并行评测；这不是新的机器人遥操作训练示范包。',
  scale='BDDL / init 文件；不按控制轨迹计数'),
 'vlabench':dict(name='VLABench 官方数据 / 评测 episodes',kind='训练示范 / 评测配置',mode='仿真',
  url='https://huggingface.co/VLABench/datasets',source='https://github.com/OpenMOSS/VLABench',
  scope='官方组织发布 primitive 微调数据与标准评测 episodes；按实际数据仓库区分训练与评测用途，不把模型权重当成数据集。'),
 'bigym':dict(name='BiGym 官方人工示范',kind='训练示范',mode='仿真',
  url='https://github.com/chernyadev/bigym#working-with-demonstrations',
  scope='DemoStore 从 GitHub releases 自动下载。官方提示部分示范不能成功完成任务，且仅支持特定 action modes。'),
 'behavior':dict(name='BEHAVIOR · 2025 Challenge 官方示范',kind='训练示范',mode='仿真',
  url='https://huggingface.co/datasets/behavior-1k/2025-challenge-demos',
  source='https://behavior.stanford.edu/challenge/archive/2025/dataset.html',
  extra=[('原始状态数据','https://huggingface.co/datasets/behavior-1k/2025-challenge-rawdata')],
  scope='2025 挑战赛 50 任务的示范，不等于全部 1,000 活动。官方指出回放生成的 joint effort 字段有误，应按修订版数据卡使用。',
  scale='10,000 条遥操作示范 / 50 个任务'),
 'robocasa':dict(name='RoboCasa365 官方数据',kind='训练示范',mode='仿真',
  url='https://robocasa.ai/docs/datasets/using_datasets.html',
  source='https://github.com/robocasa/robocasa/blob/main/docs/datasets/using_datasets.md',
  scope='包含 human 预训练、MimicGen 预训练、human target 三类数据；当前文档为 LeRobot 格式，按注册表选择版本与来源。',
  command='python -m robocasa.scripts.download_datasets --all'),
 'mimicgen':dict(name='MimicGen 官方生成数据',kind='训练示范',mode='仿真',
  url='https://huggingface.co/datasets/amandlek/mimicgen_datasets',
  source='https://github.com/NVlabs/mimicgen/blob/main/mimicgen/__init__.py',
  scope='下载以官方数据注册表为准；Google Drive 下载已弃用。论文任务覆盖与公开数据任务数分开。',
  scale='公开 README：48,000+ 条示范 / 12 个任务'),
 'dexmimicgen':dict(name='DexMimicGen 官方数据',kind='训练示范',mode='仿真',
  url='https://huggingface.co/datasets/MimicGen/dexmimicgen_datasets',
  source='https://github.com/NVlabs/dexmimicgen#datasets',
  scope='公开 HDF5 示范与环境；不是将论文真实灵巧手验证数据自动推成全部公开数据。',
  command='python scripts/download_hf_dataset.py --path /path/to/datasets'),
 'skillmimicgen':dict(name='SkillMimicGen · 数据发布说明',kind='训练示范',mode='混合',available=False,
  scope='项目展示生成及真实部署能力；本次未核实独立、公开可下载的官方训练数据包。'),
 'umi':dict(name='UMI · 官方手持夹爪示范',kind='手持夹爪示范',mode='手持采集器',
  url='https://real.stanford.edu/umi/data/zarr_datasets/',
  source='https://github.com/real-stanford/universal_manipulation_interface',
  scope='官方提供处理后的 cup_in_the_wild 等 Zarr 数据；采集器由人手持，不等于机器人实机采集。真实机械臂部署是另一项能力。',
  extra=[('官方杯子整理数据包','https://real.stanford.edu/umi/data/zarr_datasets/cup_in_the_wild.zarr.zip')]),
 'egomimic':dict(name='EgoMimic 官方人体 / 机器人数据',kind='人体 / 机器人示范',mode='混合',
  url='https://egomimic.github.io/',
  scope='区分 Aria 人体第一视角与 ALOHA 真实双臂数据；对齐学习不表示全部人体轨迹直接可执行。'),
 'egoverse':dict(name='EgoVerse 官方第一视角数据',kind='人体示范 / 对齐数据',mode='人体为主',
  url='https://egoverse.ai/',source='https://github.com/GaTech-RL2/EgoVerse',
  scope='以人体第一视角数据与对齐接口为主；机器人迁移 / Eva 接口与公开数据包含的本体分别核对，不将全部人体样本标成机器人采集。'),
 'duobench':dict(name='DuoBench 官方任务示范',kind='训练示范',mode='仿真',
  url='https://huggingface.co/datasets/RobotControlStack/duobench',
  source='https://github.com/RobotControlStack/duobench',
  scope='按 11 个任务目录发布的数据；数据仓库与论文 4 项真实任务的范围分开核对。'),
 'ebim':dict(name='EBiM · 示范数据发布说明',kind='训练示范',mode='混合',available=False,
  scope='赛方说明有多地采集 / 实机阶段；当前未确认独立可下载的完整官方示范数据包。'),
 'geniesim':dict(name='Genie Sim 3.0 官方合成数据',kind='训练示范',mode='仿真',
  url='https://modelscope.cn/datasets/agibot_world/GenieSim3.0-Dataset',
  source='https://github.com/AgibotTech/genie_sim',
  scope='合成数据与 GenieSimAssets 场景资产是两类产物；以下载包、机器人配置和数据卡核对小时数。',
  scale='README 声明 10,000+ 小时合成数据；不是本看板实测'),
 'agibot-challenge25':dict(name='AgiBot World Challenge 2025 官方数据',kind='训练示范 / 世界模型',mode='混合',
  url='https://huggingface.co/datasets/agibot-world/AgiBotWorldChallenge-2025',
  scope='2025 届赛道数据；操作与世界模型数据用途分别核对，不用 2026 数据代填。'),
 'agibot-challenge26':dict(name='AgiBot World Challenge 2026 官方数据',kind='训练示范 / 世界模型',mode='混合',
  url='https://huggingface.co/datasets/agibot-world/AgiBotWorldChallenge-2026',
  scope='2026 届赛事数据；数据目录与赛道任务映射以官方版本为准。'),
 'openlet-community':dict(name='OpenLET / LET-Data 官方社区入口',kind='训练示范',mode='实机',available=False,
  scope='社区数据和 2026—2027 赛题分开；当前未取得逐包下载与本赛季任务对应清单。'),
 'kuavo-tianchi':dict(name='Kuavo 天池首届官方赛事数据',kind='训练示范',mode='混合',
  url='https://kdc-doc.netlify.app/tianchi/cn/pages/datasets',
  scope='首届手册的数据入口与 rosbag / LeRobot 说明；仿真和真机数据按目录 / 任务区分。'),
 'reali-kuavo':dict(name='REAL-I 2026 官方 Kuavo 数据',kind='训练示范',mode='仿真',
  url='https://huggingface.co/datasets/LejuRobotics/kuavo_data_challenge_icra',
  source='https://kdc-doc.netlify.app/icra/en/pages/datasets',
  scope='数据卡中的 real 目录尚未更新；当前公开数据与手册中的真机评测阶段分开，不将计划真机数据标成已下载可用。'),
}

def apply_official_datasets(records):
    result=[];byid={r['id']:r for r in records}
    def add(owner,id,name,kind='训练示范',mode='仿真',url='',source='',scope='',scale='',available=True,command='',extra=()):
        r=byid[owner]
        # A literature PDF is a provenance link, never the default download destination.
        nonpaper=[l for l in r['links'] if not any(x in l['url'] for x in ['arxiv.org','raw.githubusercontent.com','sciencedirect.com','/assets/garrett25a/'])]
        preferred=next((l['url'] for l in nonpaper if '数据' in l['label'] or '/datasets/' in l['url']),
                       nonpaper[0]['url'] if nonpaper else r['links'][0]['url'])
        item=dict(id=id,name=name,provider_id=owner,provider_name=r['name'],benchmark_ids=[owner] if 'Benchmark' in r['roles'] else [],
          kind=kind,mode=mode,scope=scope,scale=scale or r['scale'],signals=r['data'] or '字段以官方数据说明 / 数据包为准',
          available=available,status='官方入口已核实' if available else '公开下载待核实',command=command,
          links=[dict(label='官方下载 / 数据说明' if available else '论文 / 发布说明',url=url or preferred)]+[dict(label=n,url=u) for n,u in extra],
          source=source or url or preferred,checked='2026-10-11',
          manufacturing=r['manufacturing'],manufacturing_score=r['manufacturing_score'],manufacturing_reason=r['manufacturing_reason'],
          simulator_summary=r['simulator_summary'],version_note='关联资源的公开仿真配置；数据实际采集 / 回放版本仍需按包内元数据核对。')
        result.append(item)
        r['official_dataset_refs'].append(dict(id=id,relation='作者提供' if available else '数据说明 / 待核实'))
        return item
    for r in records:r['official_dataset_refs']=[]
    for r in records:
        rid=r['id']
        if rid in ['libero','calvin','robodojo','lingbot-challenge26','robocoliseum']:continue
        if 'Dataset' not in r['roles'] and rid not in OVERRIDES:continue
        cfg=deepcopy(OVERRIDES.get(rid,{}))
        kind=cfg.pop('kind','人体数据' if rid in ['ego4d','egoexo','egodex','taco','industreal-human'] else '训练示范')
        mode=cfg.pop('mode','人体' if kind=='人体数据' else '实机' if r['real_support'] else '混合')
        name=cfg.pop('name',r['name']+' · 官方数据')
        add(rid,'data-'+rid,name,kind,mode,**cfg)
    add('behavior','behavior-2026','BEHAVIOR · 2026 Challenge 官方示范',
        url='https://huggingface.co/datasets/behavior-1k/2026-challenge-demos',
        source='https://huggingface.co/behavior-1k/datasets',
        scope='作者组织发布的 2026 届数据；与 2025 届的数据包分开登记，任务与规模不从旧赛季继承。',
        scale='任务 / 轨迹数量以 2026 官方数据卡为准',
        extra=[('2026 原始数据','https://huggingface.co/datasets/behavior-1k/2026-challenge-rawdata')])
    arena=add('robotwin','robotwin-isaac-arena','RoboTwin · IsaacLab-Arena 转换数据',kind='转换示范',mode='仿真',
        url='https://huggingface.co/datasets/littleTang/IsaacLab-Arena_RoboTwin_Data',
        source='https://github.com/RoboTwin-Platform/RoboTwin/blob/IsaacLab-Arena/data/_download_data.py',
        scope='由官方 IsaacLab-Arena 分支下载脚本指定；检索时根目录仅核实 stack_bowls_three。数据为 Isaac 平台回放 / 转换结果，不等于全部 50 项已移植，也不当成额外独立任务或原始新示范。',
        scale='已核实 1 个任务目录；HF 显示行数不直接当作机器人轨迹数',
        command='git checkout IsaacLab-Arena；bash script/_download_data.sh')
    arena.update(manufacturing='',manufacturing_score=0,manufacturing_reason='',
        simulator_summary='Isaac Sim 5.1.0 / IsaacLab-Arena（官方分支安装配置）')
    # LIBERO-100 is partitioned, not another row to sum with its 90 / 10 subsets.
    for slug,name,n,scope in [
        ('spatial','LIBERO-Spatial',10,'空间关系变化的任务套件'),
        ('object','LIBERO-Object',10,'操作对象变化的任务套件'),
        ('goal','LIBERO-Goal',10,'目标变化的任务套件'),
        ('90','LIBERO-90',90,'LIBERO-100 的预训练划分'),
        ('10','LIBERO-Long / LIBERO-10',10,'官方注册名 libero_10；LIBERO-100 的下游 10 任务划分，常用名称 LIBERO-Long'),
    ]:
        id='libero-long' if slug=='10' else 'libero-'+slug
        d=add('libero',id,name,url=LIBERO_HF+'/tree/main/libero_'+slug,
          source=LIBERO_REPO+'#datasets',scale=f'{n} 个任务；遥操作成功示范',
          scope=scope+'。LIBERO-90 与 LIBERO-10 合计 100；与其余三套件合计 130。子集不增加 benchmark 的任务统计。',
          extra=[('官方任务注册 / 划分',LIBERO_REPO+'/blob/master/libero/libero/benchmark/__init__.py'),
                 ('原始数据下载脚本',LIBERO_REPO+'/blob/master/benchmark_scripts/download_libero_datasets.py')])
        d['task_count']=n;d['signals']='原始 HDF5：图像、机器人观测 / 状态、动作；以各任务文件字段为准。'
        d['aliases']=['LIBERO-Long','LIBERO Long','LIBERO-10','libero_10'] if slug=='10' else []
    for split,name in [('D_D','CALVIN D → D'),('ABC_D','CALVIN ABC → D'),('ABCD_D','CALVIN ABCD → D')]:
        add('calvin','calvin-'+split.lower(),name,url='https://github.com/mees/calvin/blob/main/dataset/README.md',
            source='https://github.com/mees/calvin/blob/main/dataset/README.md',
            scope='不同训练场景切分共享 D 测试场景；切分含共享数据，不相加成独立轨迹数。',
            scale='官方训练 / 测试切分；每环境约 6 小时 play 数据',
            extra=[('官方压缩包','http://calvin.cs.uni-freiburg.de/dataset/task_'+split+'.zip')])
    for mode,name,scope in [('仿真','RoboDojo 仿真训练数据','仿真训练数据；按任务、本体与 split 下载，不等于 42 项评测全部可用训练示范。'),
                            ('实机','RoboDojo 实机示范数据','18 个平台-任务定义、1,800 条实机示范；仿真集和实机集分开。')]:
        add('robodojo','robodojo-'+('sim' if mode=='仿真' else 'real'),name,mode=mode,
            url='https://huggingface.co/datasets/RoboDojo-Benchmark/RoboDojo',
            source='https://robodojo-benchmark.com/doc/usage/install-and-download/#6-download-data',scope=scope,
            scale='1,800 条实机示范 / 18 个平台-任务定义' if mode=='实机' else '仿真训练数据；按任务目录核对',
            extra=[('官方 ModelScope 镜像','https://modelscope.cn/datasets/RoboDojo-Benchmark/RoboDojo')])
    # The competition uses the authors' same dataset rather than publishing a second copy.
    byid['lingbot-challenge26']['official_dataset_refs']=[dict(id='data-robotwin',relation='赛事使用（RoboTwin 作者发布）')]
    next(d for d in result if d['id']=='data-robotwin')['benchmark_ids'].append('lingbot-challenge26')
    byid['robocoliseum']['official_dataset_refs']=[dict(id='data-geniesim',relation='榜单配套（Genie Sim 作者发布）')]
    genie=next(d for d in result if d['id']=='data-geniesim')
    genie['benchmark_ids'].append('robocoliseum')
    genie['scope'] += '。RoboColiseum 官方下载脚本支持 instruction / manipulation / sim2real；空间与鲁棒性训练包覆盖需另查，不将 4 个榜单当成 4 个独立数据集。'
    genie['links'].append(dict(label='RoboColiseum 官方下载脚本',url='https://github.com/AgibotTech/genie_sim/blob/main/source/geniesim_benchmark/skills/robocoliseum/challenge-download-datasets/scripts/download_dataset.sh'))
    lookup={d['id']:d for d in result}
    for r in records:
        r['official_dataset_names']=[lookup[d['id']]['name'] for d in r['official_dataset_refs']]
    assert len(lookup)==len(result)
    assert all(d['source'] and d['links'] for d in result)
    order={r['id']:i for i,r in enumerate(records)}
    result.sort(key=lambda d:order[d['provider_id']])
    return result
