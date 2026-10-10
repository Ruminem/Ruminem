# SPDX-License-Identifier: Apache-2.0
"""Rebuild the project lists in README.md from each repository's .github/profile.md.

    python3 build_readme.py           fetch from GitHub and rewrite README.md
    python3 build_readme.py --test    self-check, no network

A repository is listed when it is public, not a fork, not archived and created on or
after SINCE. Extensions (package.json with engines.vscode) go under VS Code, the rest
under Other, each in creation order. A repository without .github/profile.md still
shows up, described by its GitHub description and README, until one is written.
"""
import json, os, re, sys, urllib.request

OWNER = 'Ruminem'
SINCE = '2026-01-01'
README = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
GROUPS = ('vscode', 'other')
SKIP = re.compile(r'^(!\[|\[!|<|\||```|>|\*\*English\*\*|\[English\]|한국어 문서는|English:|- |\d+\. )')
HANGUL = re.compile(r'[가-힣]')


def get(url, token=None):
    req = urllib.request.Request(url, headers={'User-Agent': OWNER})
    if token:
        req.add_header('Authorization', f'Bearer {token}')
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def list_repos(token):
    # One page holds 100; the loop is for the day there are more
    repos, page = [], 1
    while True:
        batch = json.loads(get(f'https://api.github.com/users/{OWNER}/repos?type=owner&per_page=100&page={page}', token))
        repos += batch
        if len(batch) < 100:
            return repos
        page += 1


def raw(name, path):
    return get(f'https://raw.githubusercontent.com/{OWNER}/{name}/HEAD/{path}')


def wanted(repo):
    return (not repo['private'] and not repo['fork'] and not repo.get('archived')
            and repo['name'] != OWNER and repo['created_at'] >= SINCE)


def sections(text):
    """`## English` / `## Korean` bodies of a profile.md, comments dropped."""
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    out, key = {}, None
    for line in text.splitlines():
        m = re.match(r'^##\s+(English|Korean)\s*$', line)
        if m:
            key = m.group(1).lower()
            out[key] = []
        elif key:
            out[key].append(line)
    return {k: '\n'.join(v).strip() for k, v in out.items()}


def first_para(lines):
    cur = []
    for line in lines:
        s = line.strip()
        if s.startswith('#'):
            if cur:
                break
            continue
        if not s or SKIP.match(s):
            if cur:
                break
            continue
        cur.append(s)
    return ' '.join(cur)


def fallback(readme, description):
    """Words for a repository that has no profile.md yet."""
    lines = (readme or '').splitlines()
    ko = []
    for i, line in enumerate(lines):
        if re.match(r'^##\s+(Korean|한국어)\s*$', line):
            lines, ko = lines[:i], lines[i + 1:]
            break
    en_intro, ko_intro = first_para(lines), first_para(ko)
    if HANGUL.search(en_intro) and not ko_intro:
        en_intro, ko_intro = '', en_intro
    en = description or en_intro
    return {'english': en, 'korean': ko_intro or en}


def group(package_json):
    try:
        return 'vscode' if 'vscode' in json.loads(package_json or '{}').get('engines', {}) else 'other'
    except ValueError:
        return 'other'


def entry(name, text, lang):
    tail = ' —' if lang == 'korean' else ''
    return f'**[{name}](https://github.com/{OWNER}/{name})**{tail}\n{text}'


def render(items):
    """items: (name, group, {'english', 'korean'}) in display order -> {marker: block}"""
    blocks = {}
    for g in GROUPS:
        for lang, short in (('english', 'en'), ('korean', 'ko')):
            blocks[f'{g}:{short}'] = '\n\n'.join(entry(n, words[lang], lang) for n, gg, words in items if gg == g)
    return blocks


def replace(text, blocks):
    for key, body in blocks.items():
        pat = re.compile(rf'(<!-- {re.escape(key)}:start -->\n).*?(\n<!-- {re.escape(key)}:end -->)', re.S)
        if not pat.search(text):
            raise SystemExit(f'README.md has no <!-- {key}:start/end --> pair')
        text = pat.sub(lambda m: m.group(1) + body + m.group(2), text)
    return text


def collect(token):
    items = []
    for repo in sorted(filter(wanted, list_repos(token)), key=lambda r: r['created_at']):
        name = repo['name']
        profile = raw(name, '.github/profile.md')
        words = sections(profile) if profile else {}
        if not words.get('english') or not words.get('korean'):
            print(f'{name}: no usable .github/profile.md, using its description and README', file=sys.stderr)
            words = fallback(raw(name, 'README.md'), repo.get('description'))
        items.append((name, group(raw(name, 'package.json')), words))
    return items


def main():
    items = collect(os.environ.get('GITHUB_TOKEN'))
    old = open(README, encoding='utf-8').read()
    new = replace(old, render(items))
    if new != old:
        open(README, 'w', encoding='utf-8').write(new)
    print(f'{len(items)} repositories, README.md {"rewritten" if new != old else "unchanged"}')


def test():
    base = {'private': False, 'fork': False, 'archived': False, 'created_at': '2026-03-01T00:00:00Z'}
    assert wanted({**base, 'name': 'a'})
    assert not wanted({**base, 'name': 'a', 'fork': True})
    assert not wanted({**base, 'name': 'a', 'archived': True})
    assert not wanted({**base, 'name': 'a', 'private': True})
    assert not wanted({**base, 'name': 'a', 'created_at': '2019-12-05T10:23:54Z'})
    assert not wanted({**base, 'name': OWNER})

    s = sections('<!-- note -->\n## English\n\nFor a.\nTwo lines.\n\n## Korean\n\n가 할 때 씀.\n<!-- old\n## English\nstale -->\n')
    assert s == {'english': 'For a.\nTwo lines.', 'korean': '가 할 때 씀.'}, s

    assert group('{"engines": {"vscode": "^1.80.0"}}') == 'vscode'
    assert group('{"engines": {"node": ">=18"}}') == 'other'
    assert group(None) == 'other' and group('not json') == 'other'

    f = fallback('# T\n\n**English** · [한국어](#korean)\n\nEnglish intro.\n\n## Korean\n\n[English](#t) · **한국어**\n\n한국어 소개임.\n', None)
    assert f == {'english': 'English intro.', 'korean': '한국어 소개임.'}, f
    f = fallback('# 테마\n\n직접 만든 테마임.\n\n## 받는 법\n', 'Themes.')
    assert f == {'english': 'Themes.', 'korean': '직접 만든 테마임.'}, f
    assert fallback(None, 'Desc.') == {'english': 'Desc.', 'korean': 'Desc.'}

    items = [('ext', 'vscode', {'english': 'E1', 'korean': 'K1'}),
             ('tool', 'other', {'english': 'E2', 'korean': 'K2'}),
             ('ext2', 'vscode', {'english': 'E3', 'korean': 'K3'})]
    b = render(items)
    assert b['vscode:en'] == f'**[ext](https://github.com/{OWNER}/ext)**\nE1\n\n**[ext2](https://github.com/{OWNER}/ext2)**\nE3'
    assert b['other:ko'] == f'**[tool](https://github.com/{OWNER}/tool)** —\nK2'

    doc = ''.join(f'x\n<!-- {k}:start -->\nold\n<!-- {k}:end -->\n' for k in b)
    out = replace(doc, b)
    assert 'old' not in out and out.count('**[ext2]') == 2 and out == replace(out, b)
    try:
        replace('no markers', b)
        raise AssertionError('missing markers must stop the build')
    except SystemExit:
        pass
    print('ok')


if __name__ == '__main__':
    test() if '--test' in sys.argv else main()
