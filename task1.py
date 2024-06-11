import shutil
import argparse
from pathlib import Path

def recursive_copy(src_dir: str, dest_dir: str = "dist") -> None:
    src = Path(src_dir)
    dest = Path(dest_dir)
    if not dest.exists():
        dest.mkdir()
    
    for new_src in src.iterdir():
        new_dest = dest.joinpath(new_src.name)
        if new_src.is_dir():
            new_dest.mkdir()
            recursive_copy(new_src, new_dest)
        else:
            shutil.copyfile(new_src, new_dest)

def main():
    parser = argparse.ArgumentParser(description="Copy files by extension.")
    parser.add_argument("source_dir", type=str, help="Path to the source directory")
    parser.add_argument("destination_dir", type=str, nargs="?", default="dist", help="Path to the destination directory (default: dist)")
    args = parser.parse_args()

    try:
        
        recursive_copy(args.source_dir, args.destination_dir)
        print("Files copied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
