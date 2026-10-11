# 机器人操作任务与评测资源

在线阅读：[机器人操作任务与评测资源看板](https://dreamlights001.github.io/Embodied_arm/)。

直接用浏览器打开 `embodied_manufacturing_dashboard.html`。这是自包含 HTML，离线支持筛选、统计、收藏、最多四项对比、CSV/JSON 导出与完整报告打印；引用链接需联网。

研究快照：2026-10-11。默认统计全部应用领域，智能制造相关内容独立标记。面向用户指定的 PiperX、宇树 R1-7A、越疆 CR5 类夹爪平台。收录 57 个资源/版本条目、299 个已枚举任务定义、24 项赛事/届次/持续榜单、7 篇综述与评测分类论文，以及 12 个制造实验任务设计。资源角色为多标签：42 个 Benchmark/场景条目、39 个 Dataset/示例数据条目、13 个生成框架。不同单位不能混加。

智能制造相关性采用三级星标：★★★ 为明确制造工序，★★ 为制造子集或装配代理任务，★ 为有具体依据的辅助工艺或生产物流能力。无相关依据的条目不显示标记；“可以迁移到制造”或名称含 Factory 不足以获得星标。资源评级为 18 项三星、14 项二星、3 项一星，22 项不标注；任务为 21 项三星、1 项二星、9 项一星，其余 268 项不标注。星级是报告的相关性判断，不是性能、成熟度或本体适配评分。混合资源与赛事按覆盖范围评级，具体任务独立判断。收藏采用文字按钮，与相关性星级分开。

报告章节：研究总览、任务统计、挑战赛与赛道、资源看板、生成器与数据、制造任务与选题、硬件与实验协议、文献与口径。新增 RoboDojo、EmbodiChain（官方拼写）、Genie Sim、EBiM、AgiBot 赛事数据等。LIBERO-10 归入 LIBERO；AgiBot Alpha/Beta 不累加；人体双手与双臂机器人区分；同名的两种 IndustReal 分开。

新增“官方数据集”目录：49 个数据包、切分或发布说明，其中 45 个核实官方入口、4 个公开下载待核实。28 个 Benchmark / 场景条目附有关联数据链接；点击在看板内定位到具体数据集，再由数据集条目访问官方说明 / 下载，或返回 benchmark。资源卡片、表格、详情、生成器与来源目录均提供关联。目录实体与资源记录独立，切分、镜像和格式转换不增加 57 个资源与 299 个任务的统计；也不把目录实体数与原先 39 个含 Dataset 角色的资源数相加。

LIBERO 的 Spatial、Object、Goal 各 10 个任务，LIBERO-90 和 LIBERO-Long / LIBERO-10 分别为 90、10 个任务。10 任务子集保留官方 `libero_10` 名称及原作者 Hugging Face 目录；不是额外新增的 10 个独立任务。LIBERO-PRO 的 BDDL / init 是评测配置，AutoMate 的装配网格是几何资产，与训练示范区分。LIBERO-Plus 的不同格式不重复计数；LingBot 使用 RoboTwin 作者发布的数据，链接到同一数据集实体。RoboDojo 仿真 / 实机、CALVIN 的不同切分、BEHAVIOR 的不同赛季分别说明。HAIL、SkillMimicGen、EBiM 与 OpenLET 仅核实数据描述 / 社区入口，保留公开下载待核实状态。

任务定义：RoboColiseum 三张命名任务表 28（鲁棒性扰动与 sim2real 对照不累加），RoboDojo 仿真 42 + 实机 18，LIBERO 官方注册表 130，RoboTwin 50，RoCo 公开任务 5，EBiM 核心任务 3，AgiBot ICRA 2026 公开任务示例 7，乐聚天池首届 7，REAL-I ICRA 2026 的阶段-任务定义 9。这些是各来源内的定义，不是跨来源去重后的语义任务数；未取得完整清单的资源保留在全量任务族表里。难度为报告初筛标签；任务链无法确认时保留“待核对”。公开任务定义与来源链接在 `task_definitions.json`；原始下载快照保留在本地。

赛事目录：北京亦庄五场赛事分别登记，另含北京世界人形机器人运动会、IROS 的 RoCo / AgiBot / RoboSense / WorldArena 工作坊关联挑战、EBiM 社区赛和 AgiBot ICRA 2026。赛道、应用领域、产品类别、障碍例按不同单位显示；完整清单与官方点名示例分别注明。EBiM 当前官网的 workshop 日期/地点待定，未直接归为 IROS 正式比赛。

平台赛事补充 11 项：灵波 2026、OpenLET 2026—2027、乐聚天池首届、REAL-I、天池具身极限系列、Qwen 首届双赛道、ERNIE 2025、AI Studio 自主机器人大赛 2025、飞桨 2023 电力巡检 / 救援 / 智能汽车相关赛题。提供平台/生态与评测类型筛选。平台为多标签：飞桨 5、天池 5、灵波 2、魔搭 2、Qwen 1、OpenLET 3；不可相加。天池系列含三个子赛，系列只计一条。开放应用与算法赛事不混入机械臂具体任务分母。

证据边界：REAL-I 数据卡 real 目录尚未更新，且名称与现行任务手册不一致，任务统计采用手册；OpenLET 本赛季三项任务名未取得，不以历史赛题代填。AI Studio 1421 仅确认赛事入口，主办/规则待核对。蚂蚁灵波、Qwen 模型、魔搭承办与天池平台分别标注；飞桨承载赛事不等于百度独立主办。

建议首期建立“配料搬运—定向插装—质量检查—失败恢复”工站，再扩展双臂主动持件、工具紧固与联合长程任务。该建议是报告的工程判断；论文与官方文档支持的事实单独呈现。未安装或运行全部外部机器人项目。

## 更新

基础条目在 `research_data.py`；新增来源、领域与赛事在 `revision_data.py`；平台/生态赛事在 `ecosystem_data.py`；任务解析与覆盖口径在 `task_inventory.py`；星级及逐项理由在 `manufacturing_ratings.py`，由构建脚本统一应用。正文/交互位于 `dashboard_template.html`、`revision_panels.html`、`revision_ui.js`。修改后运行：

官方数据实体与关联在 `official_datasets.py`；数据集目录与定位逻辑在 `dataset_panel.html`、`dataset_ui.js`。官方发布依据保留在每条数据集的来源链接中；原始页面快照保留在本地。数据集支持独立 CSV 和随全量 JSON 导出，以及筛选状态在打印后恢复。可直接打开 HTML 的 `#datasets/libero-long` 定位链接。

```text
python build_dashboard.py
```

输出 HTML、`research_catalog.json` 及对应的 `docs/` 网页发布文件。JSON 是附带的可编辑研究目录；阅读 HTML 不需要此文件。

仿真器与真实平台：57 个资源、299 个具体任务、任务族及赛事均补充后端、版本 / 版本范围、上层框架、适用分支、真实本体和 sim2real 证据范围。资源看板和任务表支持按仿真器、真实平台及已展示迁移筛选；详情、对比、CSV / JSON 与打印同步包含这些字段。当前 33 个资源有真实机器人平台依据；44 个具体任务定义有相应任务 / 阶段的真实平台标记，不能与跨来源去重后的实机任务数等同。

元数据位于 `simulator_support.py`；安装 / 依赖来源 URL 清单在 `simulator_sources.json`；原文快照保留在本地。版本按官方可核实配置记录，未锁版本、范围、未披露与不适用分别显示；例如 RoboLab 的 Isaac Sim 5.0.0 / Isaac Lab 2.2.0 和 Isaac Sim 5.1.0 / Isaac Lab 2.3.2.post1 两套环境互斥。Isaac Lab、robosuite、ROS 的版本不当成底层仿真器版本；Blender 不算物理仿真器。RoboDojo 仿真与实机任务、Kuavo 仿真与真机阶段分别处理。RoboTwin 论文实机任务只对明确同名的任务下推标记；不把全部 50 个任务推成已验证实机。人体第一视角数据不打真实机器人平台标记；真实采集数据也不等于有实时控制驱动。

## 本地验证

使用已有 Python Playwright 和 Chromium：

```text
python qa_dashboard.py
python qa_platforms.py
python qa_datasets.py
python qa_backend_update.py
```

验证离线加载、统计计数、资源/任务/赛事筛选、任务分页、卡片/表格切换、详情、对比、CSV/JSON 下载、文献检索、打印状态恢复与手机布局。截图与打印检查文件存于 `qa_artifacts`，用于页面验证，不是外部论文实验结果。

RoboColiseum（智元 Genie Sim，2026）新增为独立资源与持续榜单条目；与 RLBench 上的 Colosseum（2024）区分。复用 Genie Sim 官方数据入口，不新增重复数据实体。任务为 instruction 10 + manipulation 10 + spatial 8；跨来源任务定义可能语义重叠，299 不是去重后的能力数量。

多仿真配置本次核对：RoboTwin 的 SAPIEN 3.0.0b1 / Isaac Sim 5.1.0（Arena 分支），AutoMate 和 FORGE 的原始 Isaac Gym / Isaac Sim 移植版，EmbodiChain 的 DexSim default / Newton，Genie Sim 的 Isaac Sim PhysX / Newton standalone / Isaac Sim 6.0 Newton 实验配置。版本未披露时明确标注。MuJoCo-Warp 作为 Newton 求解路径记录，不推成独立 MuJoCo 评测后端。RoboTwin Arena 数据另列一个转换数据条目，官方脚本指定 HF 仓库；当前仅核实 stack_bowls_three 目录。RoboColiseum 当前评测 runtime 与 RT 引擎分立，比赛不继承未核实的全部后端；灵波赛事仍按 SAPIEN 环境登记。安装、配置与任务表来源链接随条目公开；原始快照保留在本地。RoboColiseum 数据及任务入口在 coliseum_data.py。


## GitHub 发布

仓库使用独立项目 `Dreamlights001/Embodied_arm`，GitHub Pages 使用项目路径 `/Embodied_arm/`。Pages 的发布来源仅为该项目的 `main` 分支 `/docs` 目录，不设置根站域名或个人简历仓库配置。

修改目录、模板或任务定义后，运行 `python build_dashboard.py` 并提交到 `main`；构建会同步生成 `docs/index.html` 与 `docs/research_catalog.json`，GitHub Pages 会自动发布 `/docs`。构建仅依赖 Python 标准库，不需要原始下载快照。`task_definitions.json` 保存已经核实的任务定义及来源；`simulator_sources.json` 保存安装依据 URL。

本地 QA 截图、打印结果、下载页面、缓存和认证文件均不提交。采集脚本可以在本地重新核查来源；测试可安装 `playwright` 后运行 `python -m playwright install chromium`，采集脚本另需 `requests` 和 `beautifulsoup4`。
