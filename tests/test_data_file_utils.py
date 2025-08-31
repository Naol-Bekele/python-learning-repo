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



