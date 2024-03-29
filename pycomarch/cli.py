
import argparse
from dataclasses import dataclass
import logging
from pathlib import Path
from typing import List, Tuple

from .logger import Logger
logger = Logger("zipper")
from . import zipper

@dataclass
class Args:
    src: Path
    dest: Path
    include_patterns: List[str]
    exclude_patterns: List[str]
    recursive: bool
    one_dir: bool
    
    class InValidArgumentsError(Exception):
        pass
    
    def validate(self) -> Tuple[bool, str]:
        ext = self.dest.suffix
        if ext != ".zip":
            return False, f"dest must be .zip file, not {ext}"
        
        return True, ""
    
    def raiseError(self, reason: str):
        raise self.InValidArgumentsError(reason)

def parse() -> Args:
    parser = argparse.ArgumentParser(
        description="A CLI tool to compress archives with useful features."
    )
    
    parser.add_argument("dest", type=Path, help="a destination file name")
    parser.add_argument("src", type=Path, help="a src file or directory to zip")
    parser.add_argument("--include-patterns", nargs="*", default=[], help="a list of patterns to include files or directories even if it matches exclude_patterns. You can use any rule supported by glob.")
    parser.add_argument("-x", "--exclude-patterns", nargs="*", default=[], help="a list of patterns to ignore files or directories. You can use any rule supported by glob.")
    parser.add_argument("-r", "--recursive", action="store_true", help="determine if zip directory recursively.")
    parser.add_argument("--one-dir", action="store_true", help = "determine nesting the zip file. When `dest` = temp.zip and set `--one-dir`, then the output zip file is \"temp.zip\" whose content is the directory \"temp/\" including the files in the src.")
    parser.add_argument("-v", "--verbose", action="store_true")
    
    namespace = parser.parse_args()
    
    logger.setLevel(logging.DEBUG if namespace.verbose else logging.INFO)
    
    args = Args(
        namespace.src, namespace.dest,
        namespace.include_patterns, namespace.exclude_patterns,
        namespace.recursive,
        namespace.one_dir
    )
    
    isvalid, reason = args.validate()
    if not isvalid:
        logger.error(reason)
        args.raiseError(reason)
    
    
    return args

def main():
    args = parse()
    zipper.zip_files(
        args.src, args.dest, args.include_patterns, args.exclude_patterns, recursive=args.recursive, one_dir=args.one_dir
    )

if __name__ == '__main__':
    main()
