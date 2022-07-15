
from pathlib import Path
from typing import List
import zipfile
import fnmatch

def is_match(name: str, patterns: List[str]):
    for pattern in patterns:
        if fnmatch.fnmatch(name, pattern):
            return True
    
    return False

def is_exclude(name: str, include_patterns: List[str], exclude_patterns: List[str]) -> bool:
    include = is_match(name, include_patterns)
    exclude = is_match(name, exclude_patterns)
    return not include and exclude

def get_files_from_directory_to_zip(root: Path, include_patterns: List[str], exclude_patterns: List[str], recursive: bool = True) -> list[Path]:
    result: list[Path] = []
    for f in root.glob("*"):
        if is_exclude(f.name, include_patterns, exclude_patterns):
            continue

        if f.is_dir() and recursive:
            files = get_files_from_directory_to_zip(f, include_patterns, exclude_patterns, recursive)
            result.extend(files)
        
        elif f.is_file():
            result.append(f)
    
    return result

def write(dest, files):
    with zipfile.ZipFile(str(dest), mode="w") as zf:
        for file in files:
            zf.write(str(file))

def zip_files(src: Path, dest: Path, include_patterns: List[str] = [], exclude_patterns: List[str] = [], recursive: bool = False):
    files_to_zip = get_files_from_directory_to_zip(src, include_patterns, exclude_patterns, recursive)
    # 相対パスじゃないと生成されるzipファイルがフルパスを反映してしまう
    files_to_zip = [f.relative_to(src) for f in files_to_zip]
    write(dest, files_to_zip)
