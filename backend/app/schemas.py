"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class InfluentMonitorEntry(BaseModel):
    """进水记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 监测时间
    field_2: str | None = None  # 进水流量
    field_3: str | None = None  # COD浓度
    field_4: str | None = None  # 氨氮浓度
    field_5: str | None = None  # 总磷浓度
    field_6: str | None = None  # pH值
    field_7: str | None = None  # 进水状态

class GritChamberEntry(BaseModel):
    """沉砂池明细结构。"""

    field_0: str | None = None  # 池体编号
    field_1: str | None = None  # 进水方式
    field_2: str | None = None  # 水力停留时间
    field_3: str | None = None  # 排砂频率
    field_4: str | None = None  # 搅拌器转速
    field_5: str | None = None  # 砂水分离效率
    field_6: str | None = None  # 运行时长
    field_7: str | None = None  # 运行状态

class AerationTankEntry(BaseModel):
    """生化池明细结构。"""

    field_0: str | None = None  # 池体编号
    field_1: str | None = None  # 处理工艺
    field_2: str | None = None  # 溶解氧浓度
    field_3: str | None = None  # 污泥浓度MLSS
    field_4: str | None = None  # 污泥沉降比SV
    field_5: str | None = None  # 水温
    field_6: str | None = None  # 混合液回流比
    field_7: str | None = None  # 运行状态

class BlowerEntry(BaseModel):
    """鼓风机明细结构。"""

    field_0: str | None = None  # 风机编号
    field_1: str | None = None  # 型号规格
    field_2: str | None = None  # 额定风量
    field_3: str | None = None  # 运行频率
    field_4: str | None = None  # 出口压力
    field_5: str | None = None  # 轴承温度
    field_6: str | None = None  # 电机电流
    field_7: str | None = None  # 运行状态

class ClarifierEntry(BaseModel):
    """二沉池明细结构。"""

    field_0: str | None = None  # 池体编号
    field_1: str | None = None  # 池体形式
    field_2: str | None = None  # 刮泥机状态
    field_3: str | None = None  # 表面负荷
    field_4: str | None = None  # 排泥周期
    field_5: str | None = None  # 出水堰状态
    field_6: str | None = None  # 污泥层厚度
    field_7: str | None = None  # 运行状态

class EffluentMonitorEntry(BaseModel):
    """出水记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 监测时间
    field_2: str | None = None  # 出水流量
    field_3: str | None = None  # COD浓度
    field_4: str | None = None  # 氨氮浓度
    field_5: str | None = None  # 总磷浓度
    field_6: str | None = None  # SS浓度
    field_7: str | None = None  # 排放状态

class SludgeDewateringEntry(BaseModel):
    """脱水设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 脱水方式
    field_2: str | None = None  # 进泥含水率
    field_3: str | None = None  # 出泥含水率
    field_4: str | None = None  # 絮凝剂用量
    field_5: str | None = None  # 泥饼产量
    field_6: str | None = None  # 转运去向
    field_7: str | None = None  # 运行状态

class ChemicalDosingEntry(BaseModel):
    """加药记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 药剂名称
    field_2: str | None = None  # 投加点位
    field_3: str | None = None  # 设计投加量
    field_4: str | None = None  # 实际投加量
    field_5: str | None = None  # 储罐剩余量
    field_6: str | None = None  # 配药人
    field_7: str | None = None  # 投加状态

class DisinfectionEntry(BaseModel):
    """消毒设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 消毒方式
    field_2: str | None = None  # 接触时间
    field_3: str | None = None  # 余氯指标
    field_4: str | None = None  # 紫外灯管时数
    field_5: str | None = None  # 出水菌落数
    field_6: str | None = None  # 清洁周期
    field_7: str | None = None  # 运行状态

class PumpStationEntry(BaseModel):
    """水泵机组明细结构。"""

    field_0: str | None = None  # 泵组编号
    field_1: str | None = None  # 泵型规格
    field_2: str | None = None  # 额定扬程
    field_3: str | None = None  # 运行频率
    field_4: str | None = None  # 电机电流
    field_5: str | None = None  # 轴承温度
    field_6: str | None = None  # 出水压力
    field_7: str | None = None  # 运行状态

class InstrumentEntry(BaseModel):
    """在线仪表明细结构。"""

    field_0: str | None = None  # 仪表编号
    field_1: str | None = None  # 仪表类型
    field_2: str | None = None  # 安装位置
    field_3: str | None = None  # 量程范围
    field_4: str | None = None  # 校准日期
    field_5: str | None = None  # 读数偏差
    field_6: str | None = None  # 维护周期
    field_7: str | None = None  # 仪表状态

class EquipmentMaintainEntry(BaseModel):
    """维保计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 设备名称
    field_2: str | None = None  # 维保类型
    field_3: str | None = None  # 计划日期
    field_4: str | None = None  # 维保人员
    field_5: str | None = None  # 更换备件
    field_6: str | None = None  # 润滑周期
    field_7: str | None = None  # 计划状态

class EnergyMeterEntry(BaseModel):
    """能耗记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 计量日期
    field_2: str | None = None  # 总用电量
    field_3: str | None = None  # 工艺电耗
    field_4: str | None = None  # 办公电耗
    field_5: str | None = None  # 峰段电费
    field_6: str | None = None  # 谷段电费
    field_7: str | None = None  # 记录状态

class SampleLabEntry(BaseModel):
    """水样检测单明细结构。"""

    field_0: str | None = None  # 检测编号
    field_1: str | None = None  # 采样点位
    field_2: str | None = None  # 检测项目
    field_3: str | None = None  # 采样时间
    field_4: str | None = None  # 检测方法
    field_5: str | None = None  # 检出值
    field_6: str | None = None  # 限值标准
    field_7: str | None = None  # 检测状态

class DeodorizationEntry(BaseModel):
    """除臭设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 除臭工艺
    field_2: str | None = None  # 风量
    field_3: str | None = None  # 填料层状态
    field_4: str | None = None  # 喷淋量
    field_5: str | None = None  # 排放浓度
    field_6: str | None = None  # 运行气味检测
    field_7: str | None = None  # 运行状态

class EmergencyEntry(BaseModel):
    """应急预案明细结构。"""

    field_0: str | None = None  # 预案编号
    field_1: str | None = None  # 预案名称
    field_2: str | None = None  # 触发条件
    field_3: str | None = None  # 响应级别
    field_4: str | None = None  # 指挥长
    field_5: str | None = None  # 应急措施
    field_6: str | None = None  # 物资清单
    field_7: str | None = None  # 预案状态

class ShiftLogEntry(BaseModel):
    """运行日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 值班班组
    field_2: str | None = None  # 当班人员
    field_3: str | None = None  # 值班时段
    field_4: str | None = None  # 交接事项
    field_5: str | None = None  # 异常摘要
    field_6: str | None = None  # 处理措施
    field_7: str | None = None  # 日志状态

class DischargePermitEntry(BaseModel):
    """排污许可明细结构。"""

    field_0: str | None = None  # 许可编号
    field_1: str | None = None  # 许可类型
    field_2: str | None = None  # 排污指标
    field_3: str | None = None  # 许可总量
    field_4: str | None = None  # 已排放总量
    field_5: str | None = None  # 剩余额度
    field_6: str | None = None  # 有效期至
    field_7: str | None = None  # 许可状态
