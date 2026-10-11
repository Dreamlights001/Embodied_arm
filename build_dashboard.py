"""Build the self-contained research dashboard (no network dependency at runtime)."""
from pathlib import Path
import json
from coliseum_data import RECORDS, SURVEYS, COMPETITIONS
from task_inventory import TASKS, FAMILIES, COVERAGE
from manufacturing_ratings import apply_ratings, RUBRIC
from simulator_support import apply_platforms, POLICY
from official_datasets import apply_official_datasets

apply_ratings(RECORDS, TASKS, FAMILIES, COMPETITIONS)
apply_platforms(RECORDS, TASKS, FAMILIES, COMPETITIONS)
OFFICIAL_DATASETS = apply_official_datasets(RECORDS)

ROOT = Path(__file__).resolve().parent
data = dict(records=RECORDS, surveys=SURVEYS, competitions=COMPETITIONS,
            tasks=TASKS, families=FAMILIES, task_coverage=COVERAGE, manufacturing_rubric=RUBRIC, platform_policy=POLICY,
            official_datasets=OFFICIAL_DATASETS)
payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
template = (ROOT / 'dashboard_template.html').read_text(encoding='utf-8')
template = template.replace('__REVISION_PANELS__', (ROOT/'revision_panels.html').read_text(encoding='utf-8'))
template = template.replace('__REVISION_JS__', (ROOT/'revision_ui.js').read_text(encoding='utf-8'))
template = template.replace('__DATASET_PANEL__', (ROOT/'dataset_panel.html').read_text(encoding='utf-8'))
template = template.replace('__DATASET_JS__', (ROOT/'dataset_ui.js').read_text(encoding='utf-8'))
output = ROOT / 'embodied_manufacturing_dashboard.html'
output.write_text(template.replace('__RESEARCH_DATA__', payload), encoding='utf-8')
(ROOT / 'research_catalog.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
site = ROOT / 'docs'
site.mkdir(exist_ok=True)
(site / 'index.html').write_bytes(output.read_bytes())
(site / 'research_catalog.json').write_bytes((ROOT / 'research_catalog.json').read_bytes())
(site / '.nojekyll').touch()
print(f'Built {output.name}: {len(RECORDS)} records, {len(SURVEYS)} surveys, {output.stat().st_size:,} bytes')
