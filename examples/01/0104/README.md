## ✅ Vue 项目的目录结构详解

大家好，我是三日老师。

这节我们来看看刚刚用 Vite 创建的 Vue 3 项目，它的目录到底是怎么组织的？
搞清楚结构，后面写组件、加页面、接接口的时候才不会迷路。

---

### 🔹1. 项目根目录有哪些重要文件？

```bash
vue3-demo/
├─ index.html
├─ package.json
├─ vite.config.js
├─ /public
├─ /src
```

我们来逐个拆解：

* `index.html` 是真正的网页入口，页面模板就在这里。
* `package.json` 用来管理依赖和脚本命令。
* `vite.config.js` 是 Vite 的配置文件，后面我们会配置别名、插件等。
* `/public` 目录里的文件会原封不动地被拷贝到最终构建结果中。
* `/src` 才是开发主战场，Vue 的所有代码都在这儿。

---

### 🔹2. src 目录中的关键结构

```bash
src/
├─ main.js
├─ App.vue
├─ assets/
├─ components/
```

* `main.js` 是项目入口文件，里面挂载 Vue 应用，类似“启动器”。
* `App.vue` 是整个应用的根组件，其他页面、模块都嵌在它里面。
* `assets/` 放静态资源，比如图片、字体、样式。
* `components/` 是你自定义的 Vue 组件，比如按钮、卡片、弹窗等。

---

### 🔹3. 后续常见目录拓展（实际开发中）

```bash
src/
├─ router/        # 路由配置
├─ store/         # 全局状态（如 Pinia）
├─ views/         # 页面级组件（一级路由页面）
├─ composables/   # 组合式函数（逻辑复用）
├─ utils/         # 工具函数封装
├─ api/           # 接口请求文件
├─ styles/        # 公共样式
```

这些目录在你做项目大一点的时候会自然长出来，配合 Vue 的模块化机制，越拆越清晰。

---

### 🔹4. 我们后面会重点操作哪些文件？

* 修改 `App.vue` 显示内容
* 往 `components/` 里写组件
* 在 `main.js` 中注册路由或状态管理
* 根据项目体量新增 `/router`、`/store` 等

---

### 总结

本节我们拆解了 Vue 3 项目的结构，搞懂了每个目录和文件的职责。
**一个 Vue 项目就像一座房子，结构稳了，才方便搭建更多功能模块。**

本节就到这里，我们下节课继续。

---

## 💻 Vue 项目的目录结构详解（代码展示部分）

以下是 Vite + Vue 3 项目的目录结构：

```bash
vue3-demo/
├── index.html              # HTML 模板入口
├── package.json            # 项目信息 + 依赖管理
├── vite.config.js          # Vite 构建配置
├── public/                 # 静态文件目录
│   └── favicon.svg         # 图标资源
└── src/                    # 项目主目录
    ├── main.js             # 应用入口文件，挂载 Vue 实例
    ├── App.vue             # 根组件，所有页面从这里开始
    ├── assets/             # 静态资源（图片、图标）
    └── components/         # 可复用组件（如按钮、弹窗等）
```

🎯 **运行时关注的重点文件**：

📁 `src/main.js`

```js
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).mount('#app')
```

📁 `src/App.vue`

```vue
<template>
  <h1>Hello Vue 3</h1>
</template>
```

