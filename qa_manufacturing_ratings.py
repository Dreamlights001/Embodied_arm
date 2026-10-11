"""Verify the requested star filters, unmarked items and exported relevance fields."""
from pathlib import Path
import json,csv,io
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'research_catalog.json').read_text(encoding='utf8'))
assert '直接制造' not in (ROOT/'embodied_manufacturing_dashboard.html').read_text(encoding='utf8')
for collection in ['records','tasks','families','competitions']:
 for item in DATA[collection]:
  n=item['manufacturing_score']
  assert n in {0,1,2,3}
  assert item['manufacturing']==('智能制造 '+'★'*n if n else '')
  assert bool(item['manufacturing_reason'])==bool(n)
with sync_playwright() as p:
 b=p.chromium.launch()
 page=b.new_page(viewport=dict(width=1440,height=1080))
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((ROOT/'embodied_manufacturing_dashboard.html').as_uri())
 page.locator('[data-go="catalog"]').first.click()
 for value in ['3','2','1','no','yes']:
  n=sum(r['manufacturing_score']==int(value) if value.isdigit() else bool(r['manufacturing_score']) if value=='yes' else not r['manufacturing_score'] for r in DATA['records'])
  page.locator('#manufacturing').select_option(value)
  assert page.locator('#results .resource').count()==n
  if value=='no':assert page.locator('#results .manufacturing-rating').count()==0
  elif value in {'1','2','3'}:
   assert page.locator('#results .manufacturing-rating[data-rating="'+value+'"]').count()==n
 page.locator('#manufacturing').select_option('3')
 page.locator('#sort').select_option('manufacturing')
 page.evaluate("window.scrollTo({top:0,behavior:'instant'})")
 page.screenshot(path=str(ROOT/'qa_artifacts/manufacturing_stars_desktop.png'))
 with page.expect_download() as download:page.locator('#csvBtn').click()
 export=ROOT/'qa_artifacts/manufacturing_stars.csv';download.value.save_as(str(export))
 rows=list(csv.DictReader(export.read_text(encoding='utf-8-sig').splitlines()))
 assert len(rows)==18
 assert all(r['manufacturing_score']=='3' and r['manufacturing_reason'] for r in rows)
 page.locator('#resetBtn').click()
 page.locator('#query').fill('LIBERO-Plus')
 assert page.locator('#results .manufacturing-rating').count()==0
 page.locator('#results [data-record="liberoplus"]').click()
 assert page.locator('#dialogContent .manufacturing-rating').count()==0
 page.keyboard.press('Escape')
 page.locator('#resetBtn').click()
 page.locator('#query').fill('NIST')
 page.locator('#results [data-record="nist"]').click()
 assert '智能制造 ★★★' in page.locator('#dialogContent').inner_text()
 assert '销孔、螺纹' in page.locator('#dialogContent').inner_text()
 page.keyboard.press('Escape')
 for panel,selector,collection,count_selector in [
  ('tasks','taskManufacturing','tasks','#taskStats .num'),
  ('competitions','competitionManufacturing','competitions','.competition-card')]:
  page.locator('[data-go="'+panel+'"]').first.click()
  for value in ['1','2','3','no']:
   page.locator('#'+selector).select_option(value)
   expected=sum(r['manufacturing_score']==(0 if value=='no' else int(value)) for r in DATA[collection])
   actual=int(page.locator(count_selector).first.inner_text()) if panel=='tasks' else page.locator(count_selector).count()
   assert actual==expected,(panel,value,actual,expected)
   if value=='no':assert page.locator('#taskRows .manufacturing-rating' if panel=='tasks' else '.competition-card .manufacturing-rating').count()==0
  page.locator('#'+selector).select_option('')
 assert errors==[],errors
 page.locator('[data-go="catalog"]').first.click()
 page.locator('#resetBtn').click()
 page.set_viewport_size(dict(width=390,height=844))
 assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
 page.screenshot(path=str(ROOT/'qa_artifacts/manufacturing_stars_mobile.png'))
 print('Star ratings: resources/tasks/events, empty labels, reasons, CSV and mobile checks passed')
 b.close()
