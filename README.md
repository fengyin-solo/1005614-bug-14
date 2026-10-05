# 污水处理厂工艺管理平台

面向格栅、沉砂池、生化池、二沉池、深度处理与污泥脱水的污水厂全流程工艺调度后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 进水监测 | `influent_monitor` | 进水记录 | 记录编号、监测时间、进水流量 |
| 沉砂池运行 | `grit_chamber` | 沉砂池 | 池体编号、进水方式、水力停留时间 |
| 生化池工况 | `aeration_tank` | 生化池 | 池体编号、处理工艺、溶解氧浓度 |
| 鼓风机房 | `blower` | 鼓风机 | 风机编号、型号规格、额定风量 |
| 二沉池运行 | `clarifier` | 二沉池 | 池体编号、池体形式、刮泥机状态 |
| 出水监测 | `effluent_monitor` | 出水记录 | 记录编号、监测时间、出水流量 |
| 污泥脱水 | `sludge_dewatering` | 脱水设备 | 设备编号、脱水方式、进泥含水率 |
| 加药管理 | `chemical_dosing` | 加药记录 | 记录编号、药剂名称、投加点位 |
| 消毒处理 | `disinfection` | 消毒设备 | 设备编号、消毒方式、接触时间 |
| 泵站运行 | `pump_station` | 水泵机组 | 泵组编号、泵型规格、额定扬程 |
| 在线仪表 | `instrument` | 在线仪表 | 仪表编号、仪表类型、安装位置 |
| 设备维保 | `equipment_maintain` | 维保计划 | 计划编号、设备名称、维保类型 |
| 能耗计量 | `energy_meter` | 能耗记录 | 记录编号、计量日期、总用电量 |
| 化验室检测 | `sample_lab` | 水样检测单 | 检测编号、采样点位、检测项目 |
| 除臭运行 | `deodorization` | 除臭设备 | 设备编号、除臭工艺、风量 |
| 应急预案 | `emergency` | 应急预案 | 预案编号、预案名称、触发条件 |
| 运行日志 | `shift_log` | 运行日志 | 日志编号、值班班组、当班人员 |
| 排污许可 | `discharge_permit` | 排污许可 | 许可编号、许可类型、排污指标 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
