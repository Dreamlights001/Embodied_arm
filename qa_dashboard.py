"""Browser QA for the offline artifact; uses an already-installed Playwright browser."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
DATA=json.loads((ROOT/'research_catalog.json').read_text(encoding='utf8'))
N=len(DATA['records'])
M=sum(r['manufacturing_score']>0 for r in DATA['records'])
D=sum('Dataset' in r['roles'] for r in DATA['records'])
G=sum('Generator' in r['roles'] for r in DATA['records'])
T=len(DATA['tasks'])
TM=sum(t['manufacturing_score']>0 for t in DATA['tasks'])
E=len(DATA['competitions'])
OUTPUT = ROOT / 'qa_artifacts'
OUTPUT.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport=dict(width=1440, height=1080), device_scale_factor=1)
    errors=[]
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto((ROOT / 'embodied_manufacturing_dashboard.html').as_uri())
    page.wait_for_selector('#stats .stat')
    assert page.locator('.resource').count() == N
    assert page.locator('#stats .num').all_text_contents() == list(map(str,[N,len(DATA['tasks']),len(DATA['competitions']),D,G]))
    page.screenshot(path=str(OUTPUT / 'overview_desktop.png'), full_page=True)
    page.locator('[data-go="catalog"]').first.click()
    page.locator('[data-preset="manufacturing"]').first.click()
    assert page.locator('.resource').count() == M
    assert page.locator('.resource.manufacturing').count() == M
    page.locator('#viewBtn').click()
    assert page.locator('#resourceTable').is_visible()
    assert not page.locator('#results').is_visible(), 'Card view should be hidden in table mode'
    page.locator('#viewBtn').click()
    page.locator('#resetBtn').click()
    page.locator('#query').fill('libero')
    assert page.locator('.resource').count() >= 4
    page.locator('#resetBtn').click()
    page.locator('#role').select_option('Dataset')
    assert page.locator('.resource').count() == D
    page.locator('#resetBtn').click()
    page.locator('#arms').select_option('双臂')
    page.locator('#horizon').select_option('长程')
    assert page.locator('.resource').count() > 4
    page.screenshot(path=str(OUTPUT / 'catalog_desktop.png'), full_page=True)
    checkboxes=page.locator('#results [data-compare]')
    checkboxes.nth(0).check()
    checkboxes.nth(1).check()
    page.locator('#compareBtn').click()
    assert page.locator('#detailDialog').is_visible()
    assert page.locator('.compare-table thead th').count()==3
    page.locator('#closeDialog').click()
    page.locator('#clearCompareBtn').click()
    page.locator('#resetBtn').click()
    page.locator('#query').fill('LIBERO-Plus')
    page.locator('#results [data-record="liberoplus"]').click()
    assert '10,030' in page.locator('#dialogContent').inner_text()
    assert '评测协议' in page.locator('#dialogContent').inner_text()
    page.keyboard.press('Escape')
    with page.expect_download() as dl:
        page.locator('#csvBtn').click()
    dl.value.save_as(str(OUTPUT / 'filtered.csv'))
    assert len((OUTPUT / 'filtered.csv').read_text(encoding='utf-8-sig').splitlines()) == 2
    with page.expect_download() as dl:
        page.locator('#jsonBtn').click()
    dl.value.save_as(str(OUTPUT / 'catalog_export.json'))
    assert len(json.loads((OUTPUT / 'catalog_export.json').read_text(encoding='utf-8'))['records']) == N
    page.locator('#resetBtn').click()
    page.locator('[data-go="generators"]').first.click()
    assert page.locator('.gendetail').count()==G
    page.locator('[data-go="sources"]').first.click()
    assert page.locator('.survey').count()==len(DATA['surveys'])
    page.locator('#sourceQuery').fill('DuoBench')
    assert page.locator('.sourceitem').count()==1
    page.locator('#sourceQuery').fill('')
    page.locator('[data-go="proposals"]').first.click()
    assert page.locator('.proposal-table tbody tr').count()==12
    page.screenshot(path=str(OUTPUT / 'proposals_desktop.png'),full_page=True)
    # Print must include all resources even when screen view is filtered.
    page.locator('[data-go="catalog"]').first.click()
    page.locator('[data-preset="manufacturing"]').first.click()
    page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
    assert page.locator('.resource').count()==N
    assert page.locator('#taskRows tr').count()==len(DATA['tasks'])
    page.emulate_media(media='print')
    page.pdf(path=str(OUTPUT / 'print_qa.pdf'),format='A4',print_background=True)
    page.emulate_media(media='screen')
    page.evaluate("window.dispatchEvent(new Event('afterprint'))")
    assert page.locator('.resource').count()==M
    page.locator('[data-go="overview"]').first.click()
    page.set_viewport_size(dict(width=390,height=844))
    page.screenshot(path=str(OUTPUT / 'overview_mobile.png'),full_page=True)
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'), 'Mobile overview overflow'
    page.locator('[data-go="catalog"]').first.click()
    page.screenshot(path=str(OUTPUT / 'catalog_mobile.png'),full_page=True)
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'), 'Mobile catalog overflow'
    assert errors==[], errors
    page.set_viewport_size(dict(width=1440,height=1080))
    page.locator('[data-go="tasks"]').first.click()
    assert page.locator('#taskStats .num').first.inner_text()==str(T)
    assert page.locator('#familyRows tr').count()==N
    page.locator('#taskSource').select_option('LIBERO')
    assert page.locator('#taskStats .num').first.inner_text()=='130'
    page.locator('#taskQuery').fill('')
    page.locator('#taskHorizon').select_option('长程')
    assert page.locator('#taskStats .num').first.inner_text()=='10'
    page.locator('#taskReset').click()
    page.locator('#taskManufacturing').select_option('yes')
    assert page.locator('#taskRows .industrial-row').count()==min(25,TM)
    assert page.locator('#taskStats .num').first.inner_text()==str(TM)
    with page.expect_download() as dl:
        page.locator('#taskCsv').click()
    dl.value.save_as(str(OUTPUT/'task_export.csv'))
    assert len((OUTPUT/'task_export.csv').read_text(encoding='utf-8-sig').splitlines())==TM+1
    page.locator('#taskReset').click()
    page.locator('#taskNext').click()
    assert page.locator('#taskPage').inner_text()==f'2 / {(T+24)//25}'
    page.screenshot(path=str(OUTPUT/'tasks_desktop.png'),full_page=True)
    page.locator('[data-go="competitions"]').first.click()
    assert page.locator('.competition-card').count()==E
    for platform in ['百度 / 飞桨','阿里云天池','蚂蚁灵波','Qwen / 通义千问','OpenLET']:
        page.locator('#competitionPlatform').select_option(platform)
        expected=sum(platform in e['platforms'] for e in DATA['competitions'])
        assert page.locator('.competition-card').count()==expected,platform
        page.locator('#competitionEvaluation').select_option('机器人操作')
        expected=sum(platform in e['platforms'] and e['evaluation']=='机器人操作' for e in DATA['competitions'])
        assert page.locator('.competition-card').count()==expected,platform+' operation'
        page.locator('#competitionReset').click()
    page.locator('[data-ecosystem="Qwen / 通义千问"]').first.click()
    assert page.locator('.competition-card').count()==sum('Qwen / 通义千问' in e['platforms'] for e in DATA['competitions'])
    page.locator('#competitionEvaluation').select_option('开放应用 / 算法')
    assert page.locator('.competition-card').count()==1
    page.locator('#competitionQuery').fill('Agent Builder')
    assert page.locator('.competition-card').count()==1
    page.evaluate("window.dispatchEvent(new Event('beforeprint'))")
    assert page.locator('.competition-card').count()==E
    page.evaluate("window.dispatchEvent(new Event('afterprint'))")
    assert page.locator('.competition-card').count()==1
    page.screenshot(path=str(OUTPUT/'qwen_events_desktop.png'),full_page=True)
    page.locator('#competitionReset').click()
    page.locator('#competitionPlatform').select_option('阿里云天池')
    page.screenshot(path=str(OUTPUT/'tianchi_events_desktop.png'),full_page=True)
    page.locator('#competitionReset').click()
    page.locator('#competitionGroup').select_option('北京亦庄')
    assert page.locator('.competition-card').count()==5
    page.locator('#competitionReset').click()
    page.locator('#competitionGroup').select_option('IROS')
    assert page.locator('.competition-card').count()==4
    page.screenshot(path=str(OUTPUT/'competitions_desktop.png'),full_page=True)
    page.locator('#competitionReset').click()
    page.set_viewport_size(dict(width=390,height=844))
    for panel in ['tasks','competitions']:
        page.locator('[data-go="'+panel+'"]').first.click()
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),panel+' mobile overflow'
        page.screenshot(path=str(OUTPUT/(panel+'_mobile.png')),full_page=True)
    assert errors==[],errors
    print(json.dumps(dict(records=N,manufacturing=M,datasets=D,generators=G,surveys=len(DATA['surveys']),tasks=len(DATA['tasks']),competitions=len(DATA['competitions']),browser_errors=errors,checks='resource/task/event filters, paging, table, compare, detail, exports, sources, print, responsive'),ensure_ascii=True))
    browser.close()
