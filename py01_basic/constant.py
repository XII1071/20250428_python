class _constant:
  def __setattr__(self, key, value):
    if key in self.__dict__:
      raise Exception("변수에 값을 할당할 수 없습니다.")
    self.__dict__[key] = value
  def __delattr__(self, item):
    if item in self.__dict__:
      raise Exception("변수를 삭제할 수 없습니다.")
# python의 sys객체에 _constant 클래스를 등록함으로 static하게 사용
import sys
sys.modules[__name__] = _constant()