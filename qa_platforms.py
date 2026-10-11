"""Check version provenance, stage-specific platform labels, filtering and exports."""
import json,csv,io
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'research_catalog.json').read_text(encoding='utf8'))
R={r['id']:r for r in D['records']}
assert len(R)==57 and len(D['tasks'])==299 and len(D['competitions'])==24
for key in ['records','tasks','families','competitions']:
 for r in D[key]:
  assert r['simulator_summary'] and r['platform_sources'] and r['platform_checked']=='2026-10-11'
  assert r['real_support']==bool(r['real_platforms'])==bool(r['real_platform_label'])
  for s in r['simulators']:
   assert s['engine'] and s['version'] and s['source'] and s['version_status']
assert [s['version'] for s in R['robolab']['simulators']]==['5.0.0','5.1.0']
assert R['libero']['simulators'][0]['framework']=='robosuite ==1.4.0'
assert R['mimicgen']['simulators'][0]['version']=='2.3.2'
assert R['embodichain']['simulator_names']==['DexSim Engine','Newton']
assert R['robotwin']['simulator_names']==['SAPIEN','Isaac Sim']
assert R['robocoliseum']['simulator_names']==['Isaac Sim'] and not R['robocoliseum']['real_support']
assert R['forge']['simulator_names']==R['automate']['simulator_names']==['Isaac Gym','Isaac Sim']
assert R['geniesim']['simulators'][-1]['version_status']=='实验配置'
assert not R['embodichain']['real_support']
assert not any(R[k]['real_support'] for k in ['ego4d','egoexo','egodex','taco','industreal-human'])
assert R['robotwin']['real_support'] and R['robocasa']['real_support']
for t in D['tasks']:
 if t['source'].startswith('RoboDojo'):
  assert t['real_support']==('实机' in t['source'])
  assert bool(t['simulators'])==('仿真' in t['source'])
 if t['source']=='LIBERO':assert not t['real_support']
 if t['source']=='RoboTwin 2.0':assert t['real_support']==(t['name'] in ['click_bell','handover_block'])
 if '乐聚机器人第一届' in t['source'] or t['source'].startswith('REAL-I'):
  assert t['real_support']==('仿真' not in t['group'])
  assert bool(t['simulators'])==('仿真' in t['group'])
 if t['source'].startswith('EBiM'):assert 'Genesis' not in t['simulator_names']
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport=dict(width=1440,height=1050));errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((ROOT/'embodied_manufacturing_dashboard.html').as_uri()+'#catalog')
 engines=sorted({s for r in D['records'] for s in r['simulator_names']})
 for engine in engines+['__none']:
  page.locator('#simulator').select_option(engine)
  expected=sum(engine in r['simulator_names'] if engine!='__none' else not r['simulator_names'] for r in D['records'])
  assert page.locator('#results .resource').count()==expected,(engine,expected)
 page.locator('#resetBtn').click()
 for val in ['yes','no','shown']:
  page.locator('#realPlatform').select_option(val)
  expected=sum(r['real_support'] if val=='yes' else not r['real_support'] if val=='no' else r['sim2real'].startswith('已展示') for r in D['records'])
  assert page.locator('#results .resource').count()==expected
  if val=='no':assert page.locator('#results .real-platform').count()==0
 page.locator('#resetBtn').click();page.locator('#query').fill('RoboLab')
 page.locator('#results [data-record="robolab"]').click()
 text=page.locator('#dialogContent').inner_text()
 assert all(s in text for s in ['5.0.0','5.1.0','2.2.0','2.3.2.post1','互斥'])
 page.keyboard.press('Escape')
 with page.expect_download() as dl:page.locator('#csvBtn').click()
 path=ROOT/'qa_artifacts/platform_resource_export.csv';dl.value.save_as(str(path))
 row=list(csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig'))))[0]
 assert '5.0.0' in row['simulator_summary'] and '5.1.0' in row['simulator_summary'] and row['platform_sources']
 page.locator('#resetBtn').click();page.locator('#simulator').select_option('Isaac Sim')
 page.evaluate("window.scrollTo({top:document.querySelector('.nav').offsetTop,behavior:'instant'})")
 page.screenshot(path=str(ROOT/'qa_artifacts/platform_catalog_desktop.png'))
 page.locator('[data-go="tasks"]').first.click()
 for engine in sorted({s for r in D['tasks'] for s in r['simulator_names']})+['__none']:
  page.locator('#taskSimulator').select_option(engine)
  expected=sum(engine in t['simulator_names'] if engine!='__none' else not t['simulator_names'] for t in D['tasks'])
  assert int(page.locator('#taskStats .num').first.inner_text())==expected
 page.locator('#taskReset').click();page.locator('#taskReal').select_option('yes')
 expected=sum(t['real_support'] for t in D['tasks'])
 assert int(page.locator('#taskStats .num').first.inner_text())==expected
 assert page.locator('#taskRows .real-platform').count()==min(25,expected)
 with page.expect_download() as dl:page.locator('#taskCsv').click()
 path=ROOT/'qa_artifacts/platform_task_export.csv';dl.value.save_as(str(path))
 rows=list(csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig'))))
 assert len(rows)==expected and all(r['real_platform_label']=='真实平台' for r in rows)
 page.locator('#taskSimulator').select_option('__none')
 saved=page.locator('#taskCount').inner_text()
 page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
 assert page.locator('#taskRows tr').count()==len(D['tasks'])
 assert page.locator('#taskRows .platform-info').count()==len(D['tasks'])
 page.evaluate("window.dispatchEvent(new Event('afterprint'))")
 assert page.locator('#taskReal').input_value()=='yes' and page.locator('#taskSimulator').input_value()=='__none'
 assert page.locator('#taskCount').inner_text()==saved
 page.locator('#taskReset').click();page.locator('#taskSource').select_option('RoboTwin 2.0')
 page.locator('#taskReal').select_option('yes')
 assert page.locator('#taskRows tr').count()==2
 assert page.locator('#taskRows .real-platform').count()==2
 page.screenshot(path=str(ROOT/'qa_artifacts/platform_tasks_desktop.png'))
 page.set_viewport_size(dict(width=390,height=844))
 for panel in ['catalog','tasks','competitions']:
  page.locator('[data-go="'+panel+'"]').first.click()
  assert page.evaluate('document.documentElement.scrollWidth<=window.innerWidth'),panel
 page.locator('[data-go="catalog"]').first.click();page.locator('#resetBtn').click()
 page.locator('#query').fill('RoboTwin 2.0')
 page.screenshot(path=str(ROOT/'qa_artifacts/platform_catalog_mobile.png'),full_page=True)
 assert not errors,errors
 print(json.dumps(dict(records=len(R),tasks=len(D['tasks']),real_resources=sum(r['real_support'] for r in D['records']),real_task_definitions=sum(t['real_support'] for t in D['tasks']),browser_errors=errors,checks='backend/version provenance, task stage labels, filters, detail, exports, print restoration and mobile'),ensure_ascii=False))
 b.close()
