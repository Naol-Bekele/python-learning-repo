import pytest
from pathlib import Path
from src.data_file_utils import (
    create_sample_directory_structure,
    move_files_by_extension,
    calculate_high_scores,
)


def test_create_sample_directory_structure(tmp_path):
    practice_dir, documents_dir, images_dir = create_sample_directory_structure()
    assert practice_dir.exists()
    assert documents_dir.exists()
    assert images_dir.exists()


def test_move_files_by_extension(tmp_path):
    practice_dir, documents_dir, images_dir = create_sample_directory_structure()
    moved = move_files_by_extension(documents_dir, images_dir, (".png", ".gif", ".jpg"))
    assert moved == 4


def test_calculate_high_scores(tmp_path):
    # Create test CSV
    test_data = """name,score
    Player1,100
    Player2,150
    Player1,200
    Player2,120"""

    test_file = tmp_path / "test_scores.csv"
    test_file.write_text(test_data)

    output_file = tmp_path / "high_scores.csv"
    results = calculate_high_scores(test_file, output_file)

    assert results["Player1"] == 200
    assert results["Player2"] == 150
    assert output_file.exists()
