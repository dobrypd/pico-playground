#!/usr/bin/python3

import argparse
import subprocess
import re
import shlex
from git import Repo
from pathlib import Path
import os

FORMATTERS = {
    "clang-format": {
        "exec": "clang-format -i {0}",
        "exts": [".cpp", ".hpp", ".h", ".cxx", ".c", ".cc", ".inl"],
        "fn_p": ".*",
    },
    "black": {"exec": "black {0}", "exts": [".py"], "fn_p": ".*"},
    "cmake-format": {
        "exec": "cmake-format -i {0}",
        "exts": [".txt"],
        "fn_p": "CMakeLists",
    },
    "cmake-format_configs": {
        "exec": "cmake-format -i {0}",
        "exts": [".cmake"],
        "fn_p": "Finder.*",
    },
}


def format_it(abspath, formatter):
    print(f"Will format {abspath}.")
    subprocess.run(shlex.split(formatter["exec"].format(str(abspath))), check=False)


def want_to_format(abspath, formatter):
    return bool(re.match(formatter["fn_p"], abspath.stem))


def get_all_files(repo_root, just_changed):
    r = Repo(repo_root)
    assert not r.bare
    if not just_changed:
        for b in r.tree().traverse():
            p = Path(b.abspath)
            if p.exists() and p.is_file() and p.suffix:
                yield p
    else:
        for diff in r.index.diff(None):
            p = Path(diff.a_blob.abspath)
            if p.exists() and p.is_file() and p.suffix:
                yield p


def get_all_files_with_formatters_format(files, e2fn, formatters):
    for p in files:
        if p.suffix.lower() in e2fn:
            formatter_names_for_this_extension = e2fn[p.suffix.lower()]
            for formatter_name in formatter_names_for_this_extension:
                formatter = formatters[formatter_name]
                if want_to_format(p, formatter):
                    yield p, formatter


def map_extensions_to_formatters(formatters):
    o = {}
    for formatter_name, formatter in formatters.items():
        for ext in formatter["exts"]:
            if not ext in o:
                o[ext] = []
            o[ext].append(formatter_name)
    return o


def repository_root():
    return Path(__file__).parent.parent


def process_all_files(repo_root, just_changed):
    af = get_all_files(repository_root(), just_changed)
    e2f = map_extensions_to_formatters(FORMATTERS)
    aftf = get_all_files_with_formatters_format(af, e2f, FORMATTERS)
    for p, f in aftf:
        format_it(p, f)


def main():
    parser = argparse.ArgumentParser(description="Format all files in this repository.")
    parser.add_argument(
        "--repo_root", type=str, nargs="?", help="the root path to the git repository"
    )
    parser.add_argument(
        "--changed",
        action="store_true",
        help="instead of all files work on just changed and not commited files",
    )
    args = parser.parse_args()
    repo_root = args.repo_root
    if not repo_root:
        repo_root = repository_root()
    just_changed = args.changed
    process_all_files(repo_root, just_changed)


if __name__ == "__main__":
    main()
