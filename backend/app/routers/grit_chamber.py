"""沉砂池运行接口：维护沉砂池，覆盖恢复正常、手动排砂、申请停机等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.grit_chamber import GritChamberService

router = APIRouter(prefix="/api/grit_chamber", tags=["沉砂池运行"])

service = GritChamberService()

LIST_FIELDS = ["池体编号", "进水方式", "水力停留时间", "排砂频率", "搅拌器转速", "砂水分离效率", "运行时长", "运行状态"]
STATUSES = ["正常运行", "排砂异常", "搅拌器故障", "待停机"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按池体编号检索"),
    status: str | None = Query(default=None, description="正常运行、排砂异常、搅拌器故障、待停机"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按池体编号与状态过滤沉砂池运行列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条沉砂池明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"沉砂池 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条沉砂池，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="沉砂池已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条沉砂池执行恢复正常、手动排砂、申请停机；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出沉砂池运行清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "grit_chamber", "total": total, "items": items}
