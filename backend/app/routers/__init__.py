"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import influent_monitor as router_influent_monitor
from app.routers import grit_chamber as router_grit_chamber
from app.routers import aeration_tank as router_aeration_tank
from app.routers import blower as router_blower
from app.routers import clarifier as router_clarifier
from app.routers import effluent_monitor as router_effluent_monitor
from app.routers import sludge_dewatering as router_sludge_dewatering
from app.routers import chemical_dosing as router_chemical_dosing
from app.routers import disinfection as router_disinfection
from app.routers import pump_station as router_pump_station
from app.routers import instrument as router_instrument
from app.routers import equipment_maintain as router_equipment_maintain
from app.routers import energy_meter as router_energy_meter
from app.routers import sample_lab as router_sample_lab
from app.routers import deodorization as router_deodorization
from app.routers import emergency as router_emergency
from app.routers import shift_log as router_shift_log
from app.routers import discharge_permit as router_discharge_permit

ROUTERS = [router_influent_monitor, router_grit_chamber, router_aeration_tank, router_blower, router_clarifier, router_effluent_monitor, router_sludge_dewatering, router_chemical_dosing, router_disinfection, router_pump_station, router_instrument, router_equipment_maintain, router_energy_meter, router_sample_lab, router_deodorization, router_emergency, router_shift_log, router_discharge_permit]
