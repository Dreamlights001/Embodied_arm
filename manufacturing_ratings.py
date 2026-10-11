"""Editorial relevance ratings, grounded in the already-cited task descriptions.

Stars measure relevance to intelligent manufacturing, never policy performance,
hardware compatibility, dataset completeness or deployment readiness.
"""
RUBRIC={
 3:'明确的制造工序：装配、紧固、工业上料、工件定向、生产工站或工业数据。',
 2:'包含制造子任务，或使用装配代理任务；整个资源不等同制造任务集。',
 1:'具有具体的辅助工艺或生产物流能力，可支撑制造研究；尚无完整制造工序评测。',
}
RESOURCE_RATINGS={
 'robocoliseum':(2,'含工件倾倒上料等制造子任务；零售、生活、语言 / 空间选物任务不继承制造标记。'),
 'nist':(3,'销孔、螺纹、连接器和布线均对应明确装配工序。'),
 'fmb':(3,'工件定向、重抓与多阶段插装对应柔性装配。'),
 'furniture':(3,'家具组件连接和装配属于产品制造工序。'),
 'ramp':(3,'梁件组合与销紧固对应结构件装配。'),
 'factory':(3,'螺母螺栓、销孔等工业接触装配任务。'),
 'industreal':(3,'接触丰富插装及感知初始化装配。'),
 'forge':(3,'螺纹、齿轮啮合及行星齿轮系统装配。'),
 'automate':(3,'多几何工件接触插装及拆卸轨迹。'),
 'fabrica':(3,'双臂持件、支撑和装配联合规划。'),
 'roco':(3,'齿轮系统逐阶段安装及失败恢复。'),
 'roco-iros':(3,'连接器、布线、螺钉紧固和电池装配；其中积木组装为代理任务。'),
 'workbench':(2,'Duplo 积木装配用于工序依赖和稳定性研究，属于装配代理任务。'),
 'assemblybench':(3,'装配说明、零件模型、工序与零件装配轨迹；不代表机器人实机工艺验证。'),
 'ariac':(3,'工业配料、搬运、装配与动态订单工站。'),
 'hail':(3,'协作臂精密插装、工具和柔性件工艺动作。'),
 'robotwin':(1,'锤击、盖章、扫描等部分任务可支撑辅助工艺研究；通用生活任务不随套件评级获得制造标记。'),
 'robosuite':(2,'包含 NutAssembly 与 Peg-in-Hole 装配任务；其余通用任务另看。'),
 'maniskill':(2,'包含插装、AssemblingKits 与 FMB 仿真子任务。'),
 'rlbench':(2,'广泛桌面任务中包含装配类子任务；非全套工业任务。'),
 'mimicgen':(2,'公开任务及用途包含插装、锤击示范扩增；生成方法本身不验证工艺质量。'),
 'dexmimicgen':(2,'TwoArmThreading 等装配相关子任务；须区分夹爪与灵巧手配置。'),
 'agibot':(2,'数据包含工业子集；厨房、零售等其他场景不继承制造标记。'),
 'egoexo':(1,'Bike Repair 的维修、工具与步骤数据对辅助工艺有参考价值；人体数据无机器人控制动作。'),
 'taco':(1,'工具—对象接触与双手协作数据支持辅助工艺动作研究，未提供工业合格质量协议。'),
 'industreal-human':(2,'construction-toy 装配和维护步骤属于工业流程代理；不是实机制造数据。'),
 'duobench':(2,'Join-Blocks 等装配代理任务与双臂定向协作；其他协调任务不全部归为制造。'),
 'robodojo':(2,'套件中的螺纹紧固任务关联制造；烹饪、整理、游戏等任务不获得制造标记。'),
 'ebim':(3,'线缆布线和导热垫放置对应明确工序；康养喂食任务单独保持无标记。'),
 'geniesim':(2,'场景和任务含工业子集；零售、餐饮、居家场景不全部归为制造。'),
 'agibot-challenge25':(2,'官方说明含工业子集；世界模型预测与其他生活任务另看。'),
 'agibot-challenge26':(2,'工件翻转等工业子任务；厨房和生活任务不继承标记。'),
 'openlet-community':(3,'工业真实作业、抓取交接和工站后训练；零售、家庭数据另筛选。'),
 'kuavo-tianchi':(3,'工业物料分拣、零件称重、汽车大件上料及仿真工站任务。'),
 'reali-kuavo':(3,'工业件分拣、翻面与日化上料；玩具分类无制造标记，快递物流相关性较弱。'),
}

def assign(item,score,reason):
 item['manufacturing_score']=score
 item['manufacturing_reason']=reason if score else ''
 item['manufacturing']='智能制造 '+('★'*score) if score else ''

def task_rating(t):
 name,source=t['name'],t['source']
 if source=='RoboColiseum 持续评测榜单':
  if name=='Pour Workpiece':return 3,'官方命名工件倾倒操作，可对应散件上料；具体工件材质与工艺质量需另行限定。'
  if name.startswith('Sorting Packages'):return 1,'包裹分拣与连续分拣可支持生产物流研究；未视为产品装配工序。'
 if '乐聚机器人第一届' in source:
  return 3,'官方工业场景任务：'+name+'；按本报告相关性评级。'
 if 'REAL-I' in source:
  if name in {'Toy Sorting'}:return 0,''
  if name in {'Parcel Weighing','Express Package Scanning'}:
   return 1,'包裹称重/扫码属于物流；流程与生产物流相近，未当成产品加工或装配。'
  return 3,'官方工业件处理或日化生产上料任务：'+name+'。'
 if 'RoCo' in source:
  return (2,'积木组装是装配依赖的代理任务。') if '积木' in name else (3,'官方装配、布线或紧固工序。')
 if 'EBiM' in source:
  return (3,'线缆布线或导热垫放置对应制造工序。') if t['manufacturing'] else (0,'')
 if 'AgiBot' in source:
  if name=='工件翻转':return 3,'工件翻转对应工业定向上料。'
  if name=='物流分拣':return 1,'通用物流分拣流程可支撑生产物流；未确认具体加工工序。'
 if source.startswith('RoboDojo') and name=='fasten_screws':return 3,'螺钉紧固对应装配工序。'
 if source=='RoboTwin 2.0' and name in {'beat_block_hammer','stamp_seal','scan_object','scan_qrcode'}:
  return 1,'锤击、标记或扫描动作与辅助工艺相关；官方任务为通用场景，不视为完整制造工序。'
 return 0,''

def apply_ratings(records,tasks,families,competitions):
 for r in records:assign(r,*RESOURCE_RATINGS.get(r['id'],(0,'')))
 by_id={r['id']:r for r in records}
 for f in families:
  r=by_id[f['id']];assign(f,r['manufacturing_score'],r['manufacturing_reason'])
 for t in tasks:
  score,reason=task_rating(t);assign(t,score,reason)
 for e in competitions:
  for tr in e['tracks']:
   matched=[t for t in tasks if t['source']==e['name'] and t['group']==tr['name']]
   if matched:
    score=max(t['manufacturing_score'] for t in matched)
    reason='按本赛道已登记任务的最高相关性显示；赛道内其他任务不继承评级。'
   elif tr['manufacturing']:
    score=3 if e['id']=='openlet26' or tr['domain']=='制造' else 2
    reason='官方领域或任务示例明确包含制造；未取得完整清单时不估计制造任务比例。'
   else:score,reason=0,''
   assign(tr,score,reason)
  score=max((tr['manufacturing_score'] for tr in e['tracks']),default=0)
  assign(e,score,'按赛道最高相关性显示；不表示整场赛事所有任务均属于制造。')
