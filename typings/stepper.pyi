# https://github.com/Klipper3d/klipper/blob/master/klippy/stepper.py
from typing import Literal

from mcu import MCU

type _Pos = list[float]

class MCU_stepper:
    def get_mcu(self) -> MCU:
        pass
    def get_name(self, short: bool = False) -> str:
        pass
    def get_commanded_position(self) -> _Pos:
        pass
    def is_active_axis(self, axis: Literal["x", "y", "z", "e"]) -> bool:
        pass
