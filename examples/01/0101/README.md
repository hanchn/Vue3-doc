
## ✅ 什么是 Vue？与 Vue 2 的关键区别

大家好，我是三日老师。

我们今天来聊聊 Vue 的本质——到底什么是 Vue？以及 Vue 3 和 Vue 2 相比，到底有哪些本质性的不同。

---

### 🔹1. 什么是 Vue？

Vue 是一个专注于构建「用户界面」的 JavaScript 框架。它的核心理念是：

> **数据驱动视图，组件化构建 UI。**

通俗点说就是：

* 你改数据，页面会自动更新（这是响应式）
* 你把页面拆成小块（组件），每块负责自己的逻辑和样式

这让我们开发复杂网页时更容易维护、更容易复用。

---

### 🔹2. Vue 的组成模块有哪些？

Vue 主要由三部分组成：

* **核心库**（数据绑定 + 组件系统）
* **Vue Router**（页面跳转 / 单页应用）
* **Pinia**（状态管理）

在大项目中，我们还会配合使用：

* **Vite**：构建工具
* **VueUse**：实用组合式工具函数集
* **Element Plus / Ant Design Vue**：UI 组件库

---

### 🔹3. Vue 2 和 Vue 3 有什么关键区别？

| 对比点    | Vue 2              | Vue 3                      |
| ------ | ------------------ | -------------------------- |
| 核心写法   | Options API        | Composition API 为主         |
| 性能     | 普通响应式，较慢           | Proxy + Tree Shaking，更快    |
| 组件通信方式 | 事件 / Vuex          | Composables / Pinia        |
| 生命周期命名 | created, mounted 等 | onMounted, onBeforeMount 等 |
| 类型支持   | TS 支持一般            | 原生支持 TypeScript            |
| 打包体积   | 比较大                | 更小、更易优化                    |

简而言之：

* **Vue 2 更适合传统入门写法**
* **Vue 3 更现代、更灵活、更高效**

我们这个系列课程采用的就是 Vue 3，因为：
✅ 它已经成为主流
✅ 写法更贴近函数式思维
✅ 后续大型项目更容易维护和扩展

---

本节内容的重点是让你明白：

* Vue 是做什么的
* Vue 3 相比 Vue 2 的优势在哪里

理解这个框架背后的设计哲学，能帮你更好地掌控项目开发。

本节讲解到这里，我们下节课开始实战代码。

---

## 💻 示例展示（建议搭配讲解演示）

在 Vue 2 中你会看到这样的写法：

```js
export default {
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    }
  }
}
```

在 Vue 3 中推荐写法是这样的：

```vue
<script setup>
import { ref } from 'vue'

const count = ref(0)
const increment = () => count.value++
</script>
```

这是 **Composition API**，通过引入函数式写法让逻辑更清晰、易组合。

