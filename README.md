
## 🧠 Vue 3 从 0 到 1 

### 第1章：Vue 3 入门与环境搭建

[* 什么是 Vue？与 Vue 2 的关键区别](./examples/01/0101/README.md)
* 安装 Node.js 与构建工具 Vite
* 创建第一个 Vue 3 项目
* Vue 项目的目录结构详解
* 运行与调试技巧

**实战案例**：构建一个“自我介绍页面”，展示基本数据绑定和事件处理

---

### 第2章：模板语法与基础指令

* 插值表达式与 Mustache 语法
* v-bind 动态绑定
* v-on 事件绑定及修饰符
* 条件渲染 v-if / v-show
* 列表渲染 v-for
* 表单绑定 v-model 的各种类型

**实战案例**：开发一个“动态简历表单”，支持实时预览填写内容

---

### 第3章：响应式系统与 Composition API 基础

* reactive vs ref 的使用与区别
* computed 的惰性计算逻辑
* watch 和 watchEffect 的差异与高级用法
* 生命周期钩子函数（setup 中的钩子）

**实战案例**：开发一个“倒计时提醒小工具”，用 watch 实现倒计时逻辑

---

### 第4章：组件系统进阶

* 组件注册与通信（props, emits）
* v-model 双向绑定组件封装
* 插槽 slot / named slot / scoped slot
* 动态组件与异步组件
* 父子组件通信、兄弟通信、中间层传值

**实战案例**：实现一个“弹窗组件系统”，支持内容自定义与事件回调

---

### 第5章：组合式 API 深度解析

* setup 函数详解与返回值类型
* composables 复用逻辑封装
* provide / inject 使用与作用域陷阱
* Composition API vs Options API 实战对比

**实战案例**：开发一个“表单校验库”，通过 Composables 实现复用逻辑封装

---

### 第6章：路由系统（Vue Router 4）

* 安装与配置 Vue Router
* 动态路由 / 嵌套路由 / 路由懒加载
* 编程式导航与导航守卫
* 路由参数的响应式变化处理
* 多级 Tab 页面设计与缓存管理

**实战案例**：开发一个“博客文章系统”，支持分页、详情页、返回导航

---

### 第7章：状态管理（Pinia）

* 什么是状态管理？Vuex 与 Pinia 的区别
* 创建与使用 Store（state/getters/actions）
* Store 的模块化管理
* 在组合式 API 中使用 Pinia
* SSR 与持久化状态设计

**实战案例**：开发一个“购物车系统”，支持商品增删、总价计算、持久化保存

---

### 第8章：VueUse 实用函数库

* 什么是 VueUse？
* 常用功能模块：useFetch、useLocalStorage、useEventListener、useWindowScroll
* 与组合式 API 高度集成技巧
* 构建自定义 VueUse 函数

**实战案例**：开发一个“灵活的浏览器工具栏插件页面”，包含滚动监听、快捷访问设置等功能

---

### 第9章：动画与过渡效果

* Vue 的内置过渡组件：<transition> 与 <transition-group>
* 使用第三方动画库：Animate.css、GSAP
* 自定义进入/离开动画
* 条件渲染与动画结合技巧

**实战案例**：开发一个“待办事项列表”，新增与删除带有动效反馈

---

### 第10章：模块化开发与组合式逻辑封装

* 组件拆分原则
* Composables 模块设计模式
* useXxx 命名约定
* 跨页面逻辑共享设计

**实战案例**：构建一个“多页面日程提醒系统”，实现通用事件、跨组件计时、全局通知

---

### 第11章：项目工程化与构建优化

* 使用 Vite 插件优化开发体验
* 环境变量与配置文件管理
* 项目 alias 与路径优化
* 按需加载与 Tree Shaking
* ESLint + Prettier + Commitlint 全套规范

**实战案例**：配置一个“企业级项目脚手架”，内置开发规范与自动格式化

---

### 第12章：SSR 与 SEO 实践（可选进阶）

* 什么是 SSR？和 CSR 的区别
* 使用 Nuxt 3 或 Vite SSR 的基本实践
* SSR 中的路由与数据获取
* SEO 优化技巧（meta、title、结构化数据）

**实战案例**：打造一个“可被搜索引擎抓取的产品展示页”

---

### 第13章：组件库生态整合

* 使用 Element Plus / Ant Design Vue
* 国际化 i18n 与主题切换
* UI 与业务解耦原则
* 自定义主题与组件扩展

**实战案例**：开发一个“管理后台模板”，包含表格、表单、图表、图标集成

---

### 第14章：自动化测试与质量保障

* 使用 Vitest 或 Jest 编写单元测试
* 组件行为测试、事件模拟
* E2E 测试基础：Playwright / Cypress
* 使用 Git Hooks 保障提交质量

**实战案例**：给“购物车系统”添加测试用例并通过 CI 工具校验

---

### 第15章：部署与上线实战

* 打包构建 vue 项目
* 配置 Nginx 生产环境
* 结合 GitHub Actions 自动部署
* 性能优化建议（图片懒加载、资源压缩、SSR/CSP）

**实战案例**：将“博客系统”打包并部署至 Vercel/Netlify/Nginx

