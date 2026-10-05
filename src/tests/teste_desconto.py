import pytest

from tech.angelofdiasg.qabank.operacoes.calcular_desconto import calcular_desconto


def test_compra_abaixo_100_comum():
    assert calcular_desconto(50, "COMUM") == 0.00


def test_compra_abaixo_100_vip():
    assert calcular_desconto(50, "VIP") == 2.50


def test_compra_imediatamente_abaixo_100():
    assert calcular_desconto(99.99, "COMUM") == 0.00


def test_compra_exatamente_100_comum():
    assert calcular_desconto(100, "COMUM") == 10.00


def test_compra_exatamente_100_vip():
    assert calcular_desconto(100, "VIP") == 15.00


def test_compra_entre_100_e_500_comum():
    assert calcular_desconto(300, "COMUM") == 30.00


def test_compra_imediatamente_abaixo_500():
    assert calcular_desconto(499.99, "COMUM") == 50.00


def test_compra_exatamente_500_comum():
    assert calcular_desconto(500, "COMUM") == 100.00


def test_compra_exatamente_500_vip():
    assert calcular_desconto(500, "VIP") == 125.00


def test_cliente_vip_minusculo():
    assert calcular_desconto(300, "vip") == 45.00


def test_cliente_vip_letras_misturadas():
    assert calcular_desconto(300, "ViP") == 45.00


def test_desconto_exatamente_no_teto():
    assert calcular_desconto(800, "VIP") == 200.00


def test_desconto_acima_teto_vip():
    assert calcular_desconto(1000, "VIP") == 200.00


def test_desconto_acima_teto_comum():
    assert calcular_desconto(1500, "COMUM") == 200.00


def test_compra_negativa():
    with pytest.raises(ValueError):
        calcular_desconto(-100, "VIP")