## ✅ 安装 Node.js 与构建工具 Vite（讲解部分）

大家好，我是三日老师。

本节课我们来完成前端开发最关键的第一步：**安装开发环境**。
我们要安装两样东西：一个是 **Node.js**，另一个是现代的构建工具 **Vite**。

---

### 🔹1. 为什么需要 Node.js？

Node.js 是我们运行前端开发工具链的基础。比如我们用的包管理器 npm 或 pnpm，本质上都是 Node.js 提供的能力。

简单理解：你不写 Node.js 后端，也得装它，前端构建工具、脚手架、依赖管理都依赖它。

---

### 🔹2. Node.js 安装推荐版本？

建议下载 **长期支持版本 LTS**，稳定性最好，官网就是：[https://nodejs.org/](https://nodejs.org/)
Windows、macOS 都有图形化安装包，一路点“下一步”就好。

---

### 🔹3. 安装完 Node 后怎么验证？

命令行输入：

```bash
node -v
npm -v
```

分别显示版本号，就说明安装成功。

---

### 🔹4. 什么是 Vite？为什么选它？

Vite 是尤雨溪团队打造的构建工具，比传统的 Webpack 快很多。

它有两个关键词值得记住：

* **极速冷启动**：几百毫秒就能起一个 Vue 项目
* **原生 ES Module 支持**：更贴近浏览器的真实执行逻辑

Vue 3 官方推荐首选就是 Vite。

---

### 🔹5. 我们今天要做的目标是什么？

通过命令行一步步创建一个基于 Vue 3 的 Vite 项目，并在浏览器里跑起来，为后面的学习打下基础。

---

本节课我们主要是「搭建环境 + 初始运行项目」，为后面写代码扫清障碍。
下一节，我们就要开始写 Vue 语法啦！

本节课就到这里，我们下节课继续。

---

## 💻 安装 Node.js 与构建工具 Vite（代码操作部分）

### ✅ 第一步：安装 Node.js

前往官网 [https://nodejs.org/](https://nodejs.org/) 下载 LTS 版本

安装完成后，打开终端或命令提示符，验证安装：

```bash
node -v   # 显示 Node.js 版本
npm -v    # 显示 npm 版本
```

### ✅ 第二步：创建 Vue 3 + Vite 项目

```bash
# 使用官方推荐的方式创建项目
npm create vite@latest vue3-demo -- --template vue

# 或者使用 pnpm（推荐，更快）
pnpm create vite@latest vue3-demo -- --template vue
```

### ✅ 第三步：进入项目并安装依赖

```bash
cd vue3-demo
npm install     # 或 pnpm install
```

### ✅ 第四步：启动开发服务器

```bash
npm run dev     # 或 pnpm dev
```

浏览器中访问 `http://localhost:5173`，看到 Vue 欢迎页面说明启动成功。

---
