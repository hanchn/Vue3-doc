## ✅ 运行与调试技巧

大家好，我是三日老师。

这节我们来聊聊 Vue 项目的「运行与调试」，也就是你本地开发时经常会用到的一些技巧和注意事项。

---

### 🔹1. 如何运行 Vue 项目？

运行命令非常简单：

```bash
npm run dev
```

或者如果你是用的 pnpm：

```bash
pnpm dev
```

这条命令会启动 Vite 的开发服务器，然后自动打开浏览器，默认端口是 `5173`。

---

### 🔹2. 热更新是怎么回事？

Vue + Vite 项目自带热更新。也就是说：

> 你每次保存代码，页面会自动刷新并展示新内容，完全不需要手动刷新。

但有几点注意事项：

* 有些配置变更（比如 `vite.config.js`）修改后需要重启服务器
* 某些 CSS 变量变更也可能触发完整刷新

---

### 🔹3. 调试推荐使用 VS Code

VS Code + Vue 插件可以大大提升你的开发体验。推荐安装这些插件：

* **Volar**（Vue 3 支持，替代 Vetur）
* **ESLint**（代码规范提示）
* **Prettier**（自动格式化）

---

### 🔹4. 控制台调试技巧（浏览器 DevTools）

在调试过程中，浏览器控制台是你最好的朋友：

* `console.log()` 是最直接的调试方式
* 打断点、查看 DOM、监听事件流，也都非常方便
* 切换到「Vue Devtools 插件」后，你可以看到 Vue 组件树、Props、Data 等内容，非常直观

---

### 🔹5. 如果项目启动失败怎么办？

* 检查 Node/npm 是否安装正确，版本是否兼容
* 看终端报错内容，常见的如端口占用、依赖没装
* 实在不行，删除 `node_modules` 再重新 install

```bash
rm -rf node_modules
npm install
```

---

### 总结

调试能力，是所有开发者的核心能力。
一个简单的热更新系统，加上控制台观察力，就能帮你快速定位大多数问题。

这一节我们算是打通了开发流程中的「运行 + 调试 + 插件环境」这条线。

本节课就到这里，我们即将进入真正的 Vue 编程核心部分 —— 模板语法与事件系统。

---

## 💻 运行与调试技巧（代码 / 工具展示部分）

### ✅ 启动项目

```bash
# 启动 Vite 开发服务器
npm run dev
# or
pnpm dev
```

输出如下：

```bash
➜  Local:   http://localhost:5173/
➜  Network: http://192.168.1.xx:5173/
```

---

### ✅ 推荐调试工具列表

#### 📦 VS Code 插件

* Volar（Vue 3 推荐）
* ESLint + Prettier
* GitLens（看每行谁写的）
* Vue Language Features（自动补全和提示）

---

#### 🧪 浏览器插件

* [Vue Devtools](https://devtools.vuejs.org/)
* 安装后打开 F12 → Vue 标签，可查看组件结构、props、响应式数据等

---

### ✅ 常见调试代码

```js
// App.vue 中 setup 里
console.log('当前用户名为：', username.value)
```

