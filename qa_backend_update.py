"""Check neutral copy, multi-backend coverage and RoboColiseum integration."""
from pathlib import Path
import json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'research_catalog.json').read_text(encoding='utf8'))
R={r['id']:r for r in D['records']}
html=(ROOT/'embodied_manufacturing_dashboard.html').read_text(encoding='utf8')
assert '课题组' not in html and '本课题组硬件条件' not in html
assert len([t for t in D['tasks'] if t['source']=='RoboColiseum 持续评测榜单'])==28
assert all(t['simulator_names']==['SAPIEN'] for t in D['tasks'] if t['source']=='RoboTwin 2.0')
assert R['lingbot-challenge26']['simulator_names']==['SAPIEN']
assert R['robocoliseum']['official_dataset_refs'][0]['id']=='data-geniesim'
arena=next(d for d in D['official_datasets'] if d['id']=='robotwin-isaac-arena')
assert not arena['manufacturing_score'] and 'SAPIEN' not in arena['simulator_summary']
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport=dict(width=1440,height=1000));errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((ROOT/'embodied_manufacturing_dashboard.html').as_uri())
 assert page.locator('header .herocard').count()==0
 assert page.locator('header').inner_text().startswith('文献与任务调研')
 page.screenshot(path=str(ROOT/'qa_artifacts/header_neutral_desktop.png'))
 page.locator('[data-go="catalog"]').first.click()
 page.locator('#simulator').select_option('__multi')
 multi=[r for r in D['records'] if len(r['simulators'])>1]
 assert page.locator('#results .resource').count()==len(multi)
 for r in multi:
  card=page.locator('#card-'+r['id'])
  assert card.locator('.platform-line').count()==len(r['simulators'])
  text=card.inner_text()
  assert all(s['version'] in text and s['scope'] in text for s in r['simulators'])
 page.locator('#resetBtn').click();page.locator('#query').fill('RoboColiseum')
 card=page.locator('#card-robocoliseum')
 assert card.is_visible() and '关联官方数据集' in card.inner_text()
 assert card.locator('.real-platform').count()==0
 card.scroll_into_view_if_needed();page.screenshot(path=str(ROOT/'qa_artifacts/robocoliseum_desktop.png'))
 card.locator('[data-dataset="data-geniesim"]').click()
 assert page.locator('#dataset-data-geniesim').is_visible()
 page.locator('#dataset-data-geniesim [data-benchmark="robocoliseum"]').click()
 assert page.locator('#card-robocoliseum').is_visible()
 page.locator('[data-go="tasks"]').first.click()
 page.locator('#taskSource').select_option('RoboColiseum 持续评测榜单')
 assert page.locator('#taskStats .num').first.inner_text()=='28'
 page.locator('#taskManufacturing').select_option('yes')
 assert page.locator('#taskStats .num').first.inner_text()=='3'
 page.locator('[data-go="catalog"]').first.click();page.locator('#query').fill('RoboColiseum')
 page.set_viewport_size(dict(width=390,height=844))
 page.locator('#card-robocoliseum').scroll_into_view_if_needed()
 assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
 page.screenshot(path=str(ROOT/'qa_artifacts/robocoliseum_mobile.png'))
 assert not errors,errors
 print(json.dumps(dict(multi_config_resources=len(multi),coliseum_tasks=28,checks='neutral header, all configuration versions/scopes, source-specific backend boundaries, shared dataset jump/return, task/manufacturing counts and mobile',browser_errors=errors),ensure_ascii=False))
 b.close()
