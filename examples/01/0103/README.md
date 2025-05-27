## ✅ 创建第一个 Vue 3 项目

大家好，我是三日老师。

在前面我们讲了环境安装，这一节我们就来动手，创建人生中第一个 Vue 3 项目。

---

### 🔹1. 我们选择的工具是 Vite

Vite 是当前最流行的前端构建工具之一，官方推荐 Vue 3 项目使用它。
它的特点有三点：

* 创建快
* 运行快
* 配置少，开箱即用

一句话：新手用起来没门槛，高手用起来很爽。

---

### 🔹2. 创建项目的步骤是什么？

第一步，我们在命令行中通过 Vite 提供的脚手架命令去生成项目骨架。
第二步，进入目录安装依赖。
第三步，运行开发服务器，就能看到效果。

整个过程不到 2 分钟。

---

### 🔹3. 创建时选择 Vue 模板

当命令提示你选择框架时，选 Vue；提示你选择语言时，可以先选 JavaScript，后续我们会用到 TypeScript 时再切换。

---

### 🔹4. 启动成功后，观察项目结构

你会看到：

* `main.js` 是程序的主入口，挂载 Vue 应用
* `App.vue` 是我们写组件的起点
* `components/` 文件夹可以放你自己写的功能模块

我们在 `App.vue` 中修改一下文字，就能看到页面热更新了。

---

总结一下：

* 我们通过一条命令创建了 Vue 3 项目
* 学会了安装依赖、运行项目
* 对项目目录有了初步了解

这一节我们算是正式上路了。
下一节，我们会进入模板语法部分，开始真正的 Vue 开发之旅。

本节课就到这里，我们下节课见。

---

## 💻 创建第一个 Vue 3 项目（代码操作部分）

### ✅ 步骤 1：创建项目

```bash
# 使用 npm 创建
npm create vite@latest vue3-demo -- --template vue

# 或使用 pnpm（推荐）
pnpm create vite@latest vue3-demo -- --template vue
```

安装过程中选择：

```
✔ Project name: » vue3-demo
✔ Select a framework: » vue
✔ Select a variant: » JavaScript
```

---

### ✅ 步骤 2：进入目录并安装依赖

```bash
cd vue3-demo
npm install   # 或 pnpm install
```

---

### ✅ 步骤 3：运行开发服务器

```bash
npm run dev   # 或 pnpm dev
```

你会看到终端输出：

```
  ➜  Local:   http://localhost:5173/
```

浏览器打开后显示：

> "You did it!" 的欢迎界面

---

### ✅ 步骤 4：修改 App.vue 做首次改动

编辑 `src/App.vue`：

```vue
<template>
  <h1>你好，Vue 3！</h1>
</template>

<script setup>
</script>

<style scoped>
h1 {
  color: #42b983;
}
</style>
```

保存后浏览器页面会**自动热更新**，你刚写的文字就出现了！

