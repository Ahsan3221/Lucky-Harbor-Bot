from settings import BRAND,GAMES
from crm import parse_game,parse_account_template
def test_brand_cashmaster():
    assert BRAND=="Lucky Harbor"
    assert "CashMaster" in GAMES
    assert parse_game(["CASHMASTER"])=="CashMaster"
    a=parse_account_template("👤 Username: Sarah333CM\n🔑 Password: 009988")
    assert (a.game,a.username,a.password)==("CashMaster","Sarah333CM","009988")
