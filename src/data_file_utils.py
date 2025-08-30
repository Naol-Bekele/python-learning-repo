from pathlib import Path
import csv
from collections import defaultdict


def create_sample_directory_structure():
    """Create practice directory structure with sample files"""
    practice_dir = Path.home() / "Desktop" / "practice_files"
    documents_dir = practice_dir / "documents"
    images_dir = practice_dir / "images"

    # Create directories
    documents_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(exist_ok=True)

    # Create sample files
    sample_files = [
        documents_dir / "image1.png",
        documents_dir / "image2.gif",
        documents_dir / "image3.png",
        documents_dir / "image4.jpg",
        documents_dir / "document1.txt",
        documents_dir / "data.csv",
    ]

    for file_path in sample_files:
        file_path.touch(exist_ok=True)

    return practice_dir, documents_dir, images_dir


def move_files_by_extension(source_dir, target_dir, extensions):
    """Move files with specific extensions to target directory"""
    moved_count = 0
    for file_path in source_dir.iterdir():
        if file_path.suffix.lower() in extensions:
            destination = target_dir / file_path.name
            file_path.replace(destination)
            moved_count += 1
    return moved_count


def calculate_high_scores(input_path, output_path):
    """Calculate high scores from CSV data"""
    high_scores = defaultdict(int)

    with input_path.open(mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            player = row["name"]
            score = int(row["score"])
            if score > high_scores[player]:
                high_scores[player] = score

    # Write high scores
    with output_path.open(mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "high_score"])
        for player, score in high_scores.items():
            writer.writerow([player, score])

    return high_scores
