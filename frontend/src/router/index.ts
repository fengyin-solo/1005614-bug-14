import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const InfluentMonitor = () => import('@/views/influent_monitor/index.vue')
const GritChamber = () => import('@/views/grit_chamber/index.vue')
const AerationTank = () => import('@/views/aeration_tank/index.vue')
const Blower = () => import('@/views/blower/index.vue')
const Clarifier = () => import('@/views/clarifier/index.vue')
const EffluentMonitor = () => import('@/views/effluent_monitor/index.vue')
const SludgeDewatering = () => import('@/views/sludge_dewatering/index.vue')
const ChemicalDosing = () => import('@/views/chemical_dosing/index.vue')
const Disinfection = () => import('@/views/disinfection/index.vue')
const PumpStation = () => import('@/views/pump_station/index.vue')
const Instrument = () => import('@/views/instrument/index.vue')
const EquipmentMaintain = () => import('@/views/equipment_maintain/index.vue')
const EnergyMeter = () => import('@/views/energy_meter/index.vue')
const SampleLab = () => import('@/views/sample_lab/index.vue')
const Deodorization = () => import('@/views/deodorization/index.vue')
const Emergency = () => import('@/views/emergency/index.vue')
const ShiftLog = () => import('@/views/shift_log/index.vue')
const DischargePermit = () => import('@/views/discharge_permit/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/influent_monitor', name: 'influent_monitor', component: InfluentMonitor },
    { path: '/grit_chamber', name: 'grit_chamber', component: GritChamber },
    { path: '/aeration_tank', name: 'aeration_tank', component: AerationTank },
    { path: '/blower', name: 'blower', component: Blower },
    { path: '/clarifier', name: 'clarifier', component: Clarifier },
    { path: '/effluent_monitor', name: 'effluent_monitor', component: EffluentMonitor },
    { path: '/sludge_dewatering', name: 'sludge_dewatering', component: SludgeDewatering },
    { path: '/chemical_dosing', name: 'chemical_dosing', component: ChemicalDosing },
    { path: '/disinfection', name: 'disinfection', component: Disinfection },
    { path: '/pump_station', name: 'pump_station', component: PumpStation },
    { path: '/instrument', name: 'instrument', component: Instrument },
    { path: '/equipment_maintain', name: 'equipment_maintain', component: EquipmentMaintain },
    { path: '/energy_meter', name: 'energy_meter', component: EnergyMeter },
    { path: '/sample_lab', name: 'sample_lab', component: SampleLab },
    { path: '/deodorization', name: 'deodorization', component: Deodorization },
    { path: '/emergency', name: 'emergency', component: Emergency },
    { path: '/shift_log', name: 'shift_log', component: ShiftLog },
    { path: '/discharge_permit', name: 'discharge_permit', component: DischargePermit },
  ],
})

export default router
