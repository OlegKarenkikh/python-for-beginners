"""Тесты для финального проекта."""
import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from premium_calculator import age_factor, accident_factor, experience_factor, calculate_premium


def test_age_factor_young():
    assert age_factor(22) == 1.5

def test_age_factor_normal():
    assert age_factor(35) == 1.1

def test_age_factor_senior():
    assert age_factor(65) == 1.2

def test_accident_factor_zero():
    assert accident_factor(0) == 0.90

def test_accident_factor_one():
    assert accident_factor(1) == 1.15

def test_experience_factor_veteran():
    assert experience_factor(12) == 0.85

def test_experience_factor_new():
    assert experience_factor(1) == 1.4

def test_calculate_premium_basic():
    client = {"id": 1, "name": "Test", "age": 35, "experience": 12, "accidents": 0}
    result = calculate_premium(client, base_rate=12_000)
    # 12000 * 1.1 * 0.90 * 0.85 = 10098.0
    assert result["premium"] == 10098.0
    assert result["policy_number"] == "POL-2024-00001"

def test_calculate_premium_young_with_accident():
    client = {"id": 2, "name": "Young", "age": 22, "experience": 2, "accidents": 1}
    result = calculate_premium(client, base_rate=12_000)
    # 12000 * 1.5 * 1.15 * 1.1 = 22770.0
    assert result["premium"] == 22770.0
