import pytest
import string
from password_generator import generate_password

def test_password_length():
    assert len(generate_password(length=10)) == 10
    assert len(generate_password(length=25)) == 25
    assert len(generate_password(length=1)) == 1

def test_password_contains_uppercase():
    password = generate_password(length=20, use_uppercase=True, use_lowercase=False, use_digits=False, use_symbols=False)
    assert all(c.isupper() for c in password)

def test_password_contains_lowercase():
    password = generate_password(length=20, use_uppercase=False, use_lowercase=True, use_digits=False, use_symbols=False)
    assert all(c.islower() for c in password)

def test_password_contains_digits():
    password = generate_password(length=20, use_uppercase=False, use_lowercase=False, use_digits=True, use_symbols=False)
    assert all(c.isdigit() for c in password)

def test_password_contains_symbols():
    password = generate_password(length=20, use_uppercase=False, use_lowercase=False, use_digits=False, use_symbols=True)
    assert all(c in string.punctuation for c in password)

def test_password_mix_all_characters():
    password = generate_password(length=30, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True)
    assert any(c.isupper() for c in password)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)

def test_invalid_length_input():
    with pytest.raises(ValueError, match="O comprimento da senha deve ser um número inteiro positivo."):
        generate_password(length=0)
    with pytest.raises(ValueError, match="O comprimento da senha deve ser um número inteiro positivo."):
        generate_password(length=-5)
    with pytest.raises(ValueError, match="O comprimento da senha deve ser um número inteiro positivo."):
        generate_password(length="abc")

def test_no_character_types_selected():
    with pytest.raises(ValueError, match="Pelo menos um tipo de caractere"):
        generate_password(use_uppercase=False, use_lowercase=False, use_digits=False, use_symbols=False)