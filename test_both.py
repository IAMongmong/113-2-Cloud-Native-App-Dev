from addNum import addNum
from multiplyNum import multiplyNum
def test_addNum():
    assert addNum(2, 3) == 5  # 測試「2 + 3」結果是否為 5
    
def test_multiplyNum():
    assert multiplyNum(2, 3) == 6  # 測試「2 * 3」結果是否為 6
