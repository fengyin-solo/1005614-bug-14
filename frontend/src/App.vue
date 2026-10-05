<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">污水处理厂工艺管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向格栅、沉砂池、生化池、二沉池、深度处理与污泥脱水的污水厂全流程工艺调度后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "进水监测", path: "/influent_monitor" }, { label: "沉砂池运行", path: "/grit_chamber" }, { label: "生化池工况", path: "/aeration_tank" }, { label: "鼓风机房", path: "/blower" }, { label: "二沉池运行", path: "/clarifier" }, { label: "出水监测", path: "/effluent_monitor" }, { label: "污泥脱水", path: "/sludge_dewatering" }, { label: "加药管理", path: "/chemical_dosing" }, { label: "消毒处理", path: "/disinfection" }, { label: "泵站运行", path: "/pump_station" }, { label: "在线仪表", path: "/instrument" }, { label: "设备维保", path: "/equipment_maintain" }, { label: "能耗计量", path: "/energy_meter" }, { label: "化验室检测", path: "/sample_lab" }, { label: "除臭运行", path: "/deodorization" }, { label: "应急预案", path: "/emergency" }, { label: "运行日志", path: "/shift_log" }, { label: "排污许可", path: "/discharge_permit" }]
</script>
