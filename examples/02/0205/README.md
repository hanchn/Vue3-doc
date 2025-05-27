## ✅ 列表渲染：`v-for`（讲解部分）

大家好，我是三日老师。

页面中经常会出现**重复结构的内容**，比如：商品列表、评论列表、菜单导航……
Vue 提供了一个非常强大的指令：**`v-for`**，用来循环渲染这些结构。

---

### 🔹1. `v-for` 的基本用法

基本语法是：

```html
<li v-for="item in items">{{ item }}</li>
```

这行意思是：**对 items 这个数组中的每一项，都渲染一个 `<li>` 元素，并展示它的内容。**

---

### 🔹2. 获取索引

除了当前项 item，还可以获取索引 index：

```html
<li v-for="(item, index) in items">
  第{{ index + 1 }}项：{{ item }}
</li>
```

---

### 🔹3. 使用对象数组

如果你的数组是对象组成的，比如：

```js
const users = [
  { name: '小明', age: 18 },
  { name: '小红', age: 20 }
]
```

你可以这样写：

```html
<div v-for="(user, i) in users" :key="i">
  {{ user.name }} - {{ user.age }}岁
</div>
```

---

### 🔹4. 为什么要加 `:key`？

Vue 在渲染列表时用 `key` 来追踪每个节点的身份，提升性能、避免错误。

建议使用唯一值，比如 ID：

```html
<div v-for="user in users" :key="user.id">{{ user.name }}</div>
```

如果没有 ID，也可以临时用索引 `:key="index"`，但不推荐在复杂场景中使用索引作为 key。

---

### 🔹5. 多层嵌套循环

你可以在嵌套结构中使用多个 `v-for`：

```html
<div v-for="group in groups" :key="group.id">
  <h3>{{ group.name }}</h3>
  <ul>
    <li v-for="user in group.members" :key="user.id">
      {{ user.name }}
    </li>
  </ul>
</div>
```

---

### 总结

`v-for` 让你可以快速构建出任意形式的重复结构，是构建动态页面不可或缺的能力。

下一节我们将进入表单绑定：`v-model`，让用户输入的数据同步到 Vue 中。

本节讲解完毕，我们来看代码！

---

## 💻 列表渲染：v-for（代码部分）

将以下代码写入 `App.vue`：

```vue
<template>
  <div class="list">
    <h2>我的任务清单</h2>
    <ul>
      <li v-for="(task, index) in tasks" :key="index">
        {{ index + 1 }}. {{ task }}
        <button @click="remove(index)">删除</button>
      </li>
    </ul>
    <input v-model="newTask" placeholder="添加任务" />
    <button @click="add">添加</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const tasks = ref(['学习 Vue', '练习代码', '喝水休息'])
const newTask = ref('')

function add() {
  if (newTask.value.trim()) {
    tasks.value.push(newTask.value)
    newTask.value = ''
  }
}

function remove(index) {
  tasks.value.splice(index, 1)
}
</script>

<style scoped>
.list {
  padding: 20px;
}
ul {
  list-style: none;
  padding-left: 0;
}
li {
  margin-bottom: 8px;
}
input {
  margin-right: 10px;
}
</style>
```

---

这段代码实现了一个任务清单：

* 用 `v-for` 渲染任务列表
* 支持输入新任务并添加
* 每一项支持点击“删除”按钮移除
