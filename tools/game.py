#!/usr/bin/env python3
"""Delegate this title's build and launch to the pinned shared native driver."""
from pathlib import Path
import argparse
import json
import os
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('check', 'prepare', 'bind', 'recover', 'partition', 'configure', 'build', 'run'))
    parser.add_argument('--paths', type=Path, default=ROOT / 'local/paths.json')
    parser.add_argument('--generated', type=Path)
    parser.add_argument('--build-dir', type=Path)
    parser.add_argument('--development-framework', type=Path,
                        help='Explicit development worktree; records its actual HEAD and tracked changes')
    args, extra = parser.parse_known_args()
    pin = json.loads((ROOT / 'framework.json').read_text(encoding='utf-8'))
    framework = (args.development_framework or ROOT / pin['directory']).resolve()
    git = 'C:/Program Files/Git/cmd/git.exe' if os.name == 'nt' else shutil.which('git')
    head = subprocess.check_output([git, '-C', str(framework), 'rev-parse', 'HEAD'], text=True).strip()
    changes = subprocess.check_output([git, '-C', str(framework), 'status', '--short', '--untracked-files=no'], text=True)
    if args.development_framework is None and (head != pin['revision'] or changes):
        raise ValueError('Framework differs from the tested clean pin; select an explicit development worktree for development')
    paths_file = args.paths.resolve()
    private = json.loads(paths_file.read_text(encoding='utf-8'))
    generated = args.generated or Path(private.get('generated', ROOT / 'build/generated'))
    build = args.build_dir or Path(private.get('build_dir', ROOT / 'build/host'))
    evidence = ROOT / 'local/driver-invocations'
    evidence.mkdir(parents=True, exist_ok=True)
    record = dict(action=args.action, framework=str(framework), framework_head=head,
                  tested_pin=pin['revision'], development=args.development_framework is not None,
                  tracked_framework_changes=changes, generated=str(generated), build=str(build))
    command = [sys.executable, str(framework / 'tools/native_title.py'), args.action,
               '--title', str(ROOT / 'native-title.toml'), '--paths', str(paths_file),
               '--generated', str(generated), '--build-dir', str(build), *extra]
    record['command'] = command
    (evidence / (str(time.time_ns()) + '.aot-private.json')).write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    return subprocess.run(command, cwd=ROOT).returncode


if __name__ == '__main__':
    raise SystemExit(main())
