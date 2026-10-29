"""Exercise benchmark->dataset->benchmark navigation, deep links and exports."""
from pathlib import Path
from collections import Counter
import json,csv,io
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'research_catalog.json').read_text(encoding='utf8'))
ds={d['id']:d for d in D['official_datasets']};records={r['id']:r for r in D['records']}
assert len(records)==58 and len(D['tasks'])==299 and len(D['competitions'])==24
assert ds['data-libero-industry']['provider_id']=='libero-industry'
assert len(ds)==len(D['official_datasets'])
assert sum(d.get('task_count',0) for d in ds.values() if d['provider_id']=='libero')==130
assert ds['libero-long']['task_count']==10
assert ds['libero-long']['links'][0]['url'].endswith('/libero_10')
assert ds['data-liberopro']['kind']=='评测配置'
assert ds['data-umi']['mode']=='手持采集器'
assert ds['data-robotwin']['mode']=='仿真'
for r in records.values():
 assert all(ref['id'] in ds for ref in r['official_dataset_refs'])
for d in ds.values():
 assert d['provider_id'] in records and d['links'] and d['source']
 if not d['available']:assert d['status']=='公开下载待核实'
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport=dict(width=1440,height=1050));errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((ROOT/'embodied_manufacturing_dashboard.html').as_uri()+'#catalog')
 page.locator('#query').fill('LIBERO（含 LIBERO-10）')
 links=page.locator('#card-libero [data-dataset]')
 assert links.count()==5
 page.locator('#card-libero [data-dataset="libero-long"]').click()
 assert page.locator('#datasets').is_visible()
 assert page.url.endswith('#datasets/libero-long')
 assert page.locator('#dataset-libero-long').is_visible()
 assert page.locator('#dataset-libero-long').evaluate('(el)=>el===document.activeElement')
 assert 'libero_10' in page.locator('#dataset-libero-long').inner_text()
 assert '130' in page.locator('#dataset-libero-long').inner_text()
 assert page.locator('#dataset-libero-long .manufacturing-rating').count()==0
 page.screenshot(path=str(ROOT/'qa_artifacts/libero_long_dataset_desktop.png'))
 page.go_back()
 assert page.locator('#catalog').is_visible()
 assert page.locator('#query').input_value()=='LIBERO（含 LIBERO-10）'
 page.go_forward();assert page.locator('#datasets').is_visible()
 # A restrictive dataset filter must not block a dataset anchor from elsewhere.
 page.locator('#datasetQuery').fill('does-not-exist')
 page.wait_for_function("document.querySelectorAll('.dataset-card').length === 0")
 page.locator('[data-go="catalog"]').first.click()
 page.locator('#resetBtn').click();page.locator('#query').fill('FurnitureBench')
 page.locator('#card-furniture [data-dataset]').click()
 assert page.locator('#datasetQuery').input_value()==''
 assert page.locator('#dataset-data-furniture').is_visible()
 page.locator('#dataset-data-furniture [data-benchmark="furniture"]').click()
 assert page.locator('#catalog').is_visible() and page.locator('#card-furniture').is_visible()
 page.locator('#query').fill('LIBERO（含 LIBERO-10）')
 page.locator('#card-libero [data-record="libero"]').click()
 page.locator('#dialogContent [data-dataset="libero-long"]').click()
 assert not page.locator('#detailDialog').is_visible() and page.locator('#datasets').is_visible()
 page.locator('#dataset-libero-long [data-benchmark="libero"]').click()
 page.locator('#viewBtn').click()
 page.locator('#resourceTable [data-dataset="libero-long"]').click()
 assert page.locator('#datasets').is_visible()
 page.locator('#dataset-libero-long [data-benchmark="libero"]').click()
 # Test every declared relationship without external network navigation.
 for r in records.values():
  for ref in r['official_dataset_refs']:
   page.locator('[data-go="catalog"]').first.click();page.locator('#resetBtn').click()
   page.locator('#card-'+r['id']+' [data-dataset="'+ref['id']+'"]').click()
   assert page.locator('#dataset-'+ref['id']).is_visible(),(r['id'],ref)
   assert page.url.endswith('#datasets/'+ref['id'])
 page.locator('#datasetProvider').select_option('libero')
 assert page.locator('.dataset-card').count()==5
 with page.expect_download() as dl:page.locator('#datasetCsv').click()
 path=ROOT/'qa_artifacts/libero_official_datasets.csv';dl.value.save_as(str(path))
 rows=list(csv.DictReader(io.StringIO(path.read_text(encoding='utf-8-sig'))))
 assert len(rows)==5 and any(r['id']=='libero-long' for r in rows)
 page.locator('#datasetReset').click()
 for kind,n in Counter(d['kind'] for d in ds.values()).items():
  page.locator('#datasetKind').select_option(kind)
  assert page.locator('.dataset-card').count()==n
 page.locator('#datasetReset').click();page.locator('#datasetAvailability').select_option('no')
 assert page.locator('.dataset-card').count()==sum(not d['available'] for d in ds.values())
 saved=page.locator('#datasetCount').inner_text()
 page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
 assert page.locator('.dataset-card').count()==len(ds)
 page.evaluate("window.dispatchEvent(new Event('afterprint'))")
 assert page.locator('#datasetCount').inner_text()==saved
 page.goto((ROOT/'embodied_manufacturing_dashboard.html').as_uri()+'#datasets/libero-long')
 assert page.locator('#dataset-libero-long').is_visible() and page.locator('#datasets').is_visible()
 page.wait_for_function("(()=>{const y=document.getElementById('dataset-libero-long').getBoundingClientRect().top;return y>=60&&y<=130})()")
 page.set_viewport_size(dict(width=390,height=844))
 page.reload()
 page.wait_for_function("(()=>{const el=document.getElementById('dataset-libero-long'),y=el.getBoundingClientRect().top;return y>=60&&y<=130&&el===document.activeElement})()")
 assert page.evaluate('document.documentElement.scrollWidth<=window.innerWidth')
 page.screenshot(path=str(ROOT/'qa_artifacts/libero_long_dataset_mobile.png'))
 assert not errors,errors
 print(json.dumps(dict(dataset_entries=len(ds),official_entries=sum(d['available'] for d in ds.values()),linked_benchmarks=sum(bool(r['official_dataset_refs']) and 'Benchmark' in r['roles'] for r in records.values()),checks='all internal references, LIBERO splits, precise navigation, back/forward, deep links, filters, CSV, print and mobile',browser_errors=errors),ensure_ascii=False))
 b.close()
