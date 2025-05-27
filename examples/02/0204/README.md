## ✅ 条件渲染：`v-if` / `v-else` / `v-else-if` / `v-show`

大家好，我是三日老师。

在很多网页中，某些内容**不是一直显示的**，而是根据用户状态、按钮点击或数据加载来决定“要不要显示”。

在 Vue 里，这种“让某个区域有条件地出现或消失”的方式，就叫做：**条件渲染**。

---

### 🔹1. `v-if` 是什么？

`v-if` 会根据布尔表达式的值，**决定是否渲染这个元素到 DOM 中**。

```html
<p v-if="isLoggedIn">欢迎回来！</p>
```

当 `isLoggedIn` 是 `false`，这个 `<p>` 标签会**根本不会出现在页面中**。

---

### 🔹2. `v-else` / `v-else-if`

和 JavaScript 的 `if/else if/else` 很像，Vue 也可以链式写条件逻辑：

```html
<p v-if="score >= 90">优秀</p>
<p v-else-if="score >= 60">及格</p>
<p v-else>不及格</p>
```

注意：这几个元素之间**不能夹杂其他内容**，否则会报错。

---

### 🔹3. `v-show` 是什么？

`v-show` 不会从 DOM 中移除元素，它只是通过 `display: none` 让元素隐藏。

```html
<p v-show="loading">加载中...</p>
```

这个 `<p>` 一直都在，只是可见性被控制。

---

### 🔹4. `v-if` vs `v-show` 怎么选？

| 比较维度     | v-if           | v-show       |
| -------- | -------------- | ------------ |
| DOM 操作频率 | 动态添加/移除 DOM 节点 | 仅修改 CSS      |
| 性能适合     | 不频繁切换的内容       | 频繁显示/隐藏的内容   |
| 初始渲染     | 条件为 false 时不渲染 | 初始总是会渲染，只是隐藏 |

**一句话总结**：

* **频繁切换**用 `v-show`
* **条件复杂、切换少**用 `v-if`

---

### 🔹5. `template` 配合 v-if 渲染多个元素

有时候我们想让多个元素统一受 `v-if` 控制，可以用 `<template>` 包裹：

```html
<template v-if="isAdmin">
  <p>欢迎管理员</p>
  <button>进入后台</button>
</template>
```

---

### 总结

`v-if` 和 `v-show` 让页面变得“更智能”，它们是数据驱动视图变化的关键工具之一。

下一节，我们会学习另一个必杀技 —— `v-for` 循环渲染列表。

本节讲解完毕，我们来看代码示例！

---

## 💻 条件渲染：v-if / v-show（代码部分）

将以下代码写入 `App.vue` 即可运行：

```vue
<template>
  <div class="panel">
    <h2>分数：{{ score }}</h2>
    <button @click="increase">+10</button>
    <button @click="reset">重置</button>

    <!-- v-if / v-else-if / v-else -->
    <p v-if="score >= 90">成绩：优秀</p>
    <p v-else-if="score >= 60">成绩：及格</p>
    <p v-else>成绩：不及格</p>

    <!-- v-show 示例 -->
    <p v-show="score >= 60">🎉 你通过了！</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const score = ref(55)

function increase() {
  score.value += 10
}

function reset() {
  score.value = 0
}
</script>

<style scoped>
.panel {
  padding: 20px;
  border: 1px solid #ccc;
}
button {
  margin-right: 10px;
}
</style>
```

---

✅ 本示例涵盖：

* `v-if / v-else-if / v-else` 的条件链判断
* `v-show` 用于展示“通过”提示
* 如何通过按钮动态改变绑定值
