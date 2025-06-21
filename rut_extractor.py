import argparse
import csv
import os
import re
from typing import Iterable, List, Dict

RUT_REGEX = re.compile(r"\b\d{1,2}(?:\.\d{3}){2}-[0-9kK]\b")


def extract_ruts_from_text(text: str) -> List[str]:
    """Return a list of RUT numbers found in the given text."""
    return RUT_REGEX.findall(text)


def read_ruts_from_file(path: str) -> List[str]:
    """Read a single file and return all RUTs found."""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    except FileNotFoundError:
        return []
    return extract_ruts_from_text(text)


def iter_files(directory: str) -> Iterable[str]:
    """Yield file paths under the given directory."""
    for root, _, files in os.walk(directory):
        for name in files:
            yield os.path.join(root, name)


def lookup_rut(rut: str) -> Dict[str, str]:
    """Placeholder lookup returning sample data for a RUT."""
    # In a real implementation this would fetch data from an API or database.
    return {"RUT": rut, "Name": f"Person {rut[-4:]}"}


def collect_rut_info(input_dir: str) -> List[Dict[str, str]]:
    """Read all files in *input_dir* and return info for each RUT found."""
    seen = set()
    results = []
    for path in iter_files(input_dir):
        for rut in read_ruts_from_file(path):
            if rut not in seen:
                seen.add(rut)
                results.append(lookup_rut(rut))
    return results


def write_results_csv(results: List[Dict[str, str]], output_file: str) -> None:
    """Write collected results to *output_file* in CSV format."""
    if not results:
        return
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract RUT numbers from files")
    parser.add_argument("--input-dir", required=True, help="Folder containing files")
    parser.add_argument("--output-file", required=True, help="Output CSV filename")
    args = parser.parse_args()

    results = collect_rut_info(args.input_dir)
    write_results_csv(results, args.output_file)


if __name__ == "__main__":
    main()
