## ✅ v-on：事件绑定及修饰符

大家好，我是三日老师。

在上一节我们让页面可以“看起来会动”，但这节我们要真正让用户“操作页面”，让它**响应点击、输入、提交等行为**。

这就是 Vue 提供的事件绑定功能：**`v-on` 指令**。

---

### 🔹1. 什么是 `v-on`？

`v-on` 是 Vue 用来绑定 DOM 事件的指令。

基本语法是：

```html
v-on:事件名="方法名"
```

简写为：

```html
@事件名="方法名"
```

比如点击按钮调用 `sayHi` 方法：

```html
<button @click="sayHi">点我</button>
```

---

### 🔹2. 如何定义方法？

在 Vue 3 的 `<script setup>` 中，方法直接用函数定义：

```js
function sayHi() {
  console.log('你好呀！')
}
```

注意：函数必须定义在 `<script setup>` 的作用域内。

---

### 🔹3. 常用事件有哪些？

* `click`：点击
* `input`：输入变化（input 框）
* `change`：值变化（下拉、复选框）
* `submit`：表单提交
* `keydown` / `keyup`：键盘事件

---

### 🔹4. 事件修饰符，让事件更可控

Vue 提供了一些简洁语法，帮助我们更好地控制事件行为：

| 修饰符        | 作用            |
| ---------- | ------------- |
| `.stop`    | 阻止事件冒泡        |
| `.prevent` | 阻止默认行为（如表单提交） |
| `.once`    | 只触发一次         |
| `.capture` | 使用事件捕获模式      |
| `.self`    | 仅在事件源是自身时触发   |
| `.enter`   | 仅在按下回车键时触发    |

例如：

```html
<form @submit.prevent="onSubmit">...</form>
```

可以防止页面跳转。

---

### 🔹5. 传参事件处理函数

需要传参时可以这样写：

```html
<button @click="sayHi('小明')">打招呼</button>
```

但注意，这样会变成“立即执行”，不是“点击再执行”。

正确写法是使用箭头函数：

```html
<button @click="() => sayHi('小明')">打招呼</button>
```

---

### 总结

事件绑定是 Vue 和用户交互的核心桥梁。
通过 `v-on` 和事件修饰符，你可以精确控制什么时候、如何触发行为。

下一节我们会学习条件渲染——让页面根据状态显示不同内容。

本节讲解完毕，我们来看代码！

---

## 💻 v-on：事件绑定及修饰符（代码部分）

你可以将以下代码写入 `App.vue` 文件：

```vue
<template>
  <div class="box">
    <h2>点了 {{ count }} 次</h2>
    <button @click="increment">+1</button>
    <button @click="reset">重置</button>

    <form @submit.prevent="submitForm">
      <input v-model="name" placeholder="输入名字" />
      <button type="submit">提交</button>
    </form>

    <p v-if="submitted">你输入的是：{{ name }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const count = ref(0)
const name = ref('')
const submitted = ref(false)

function increment() {
  count.value++
}

function reset() {
  count.value = 0
}

function submitForm() {
  submitted.value = true
}
</script>

<style scoped>
.box {
  padding: 20px;
}
button {
  margin-right: 10px;
  padding: 6px 12px;
}
</style>
```

---

这段代码涵盖了：

* `@click` 基础点击事件
* `@submit.prevent` 表单提交阻止默认行为
* 方法定义与组合式响应式变量配合
