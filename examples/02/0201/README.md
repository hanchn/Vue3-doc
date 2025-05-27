## ✅ 插值表达式与 Mustache 语法（讲解部分）

大家好，我是三日老师。

这节我们要讲的是 Vue 最基础也是最直观的能力：**插值表达式**，也叫 Mustache 语法，形式是 `{{ someData }}`。

---

### 🔹1. 插值表达式的作用是什么？

它可以让你在 HTML 模板中动态显示 JavaScript 中的数据。

比如你定义了一个变量 `username = '小明'`，只需要写：

```html
<h1>你好，{{ username }}</h1>
```

页面上就能实时显示“你好，小明”。

---

### 🔹2. 它支持哪些内容？

你可以在里面写任意**表达式**，比如：

```html
{{ username.toUpperCase() }}
{{ age + 1 }}
{{ isVip ? '尊贵会员' : '普通用户' }}
```

但注意，它**不支持语句**，比如 `if/for/while` 这些结构不能写在里面。

---

### 🔹3. 它是响应式的吗？

是的，只要你绑定的变量是 `ref` 或 `reactive` 创建的，一旦值发生变化，插值表达式渲染的内容就会自动更新。

---

### 🔹4. 插值不仅限于文本

你也可以结合 `v-bind` 把插值用在属性上，比如：

```html
<img :src="avatarUrl" />
```

或者在 class、style 中动态使用。

---

### 🔹5. 插值表达式与 HTML 标签

默认 Vue 会自动对插值内容进行 **HTML 转义**，防止 XSS 攻击。
如果你**确实**需要插入原始 HTML，可以使用 `v-html` 指令，但使用它必须确保内容安全。

---

### 总结

插值表达式是 Vue 中数据驱动 UI 的最基本方式。
它语法简单、功能强大，是你与“响应式视图”连接的第一步。

下一节我们会继续学习 Vue 的第二大法宝 —— 动态属性绑定（v-bind）。

本节讲解完毕，我们来看代码示例！

---

## 💻 插值表达式与 Mustache 语法（代码部分）

你可以将以下代码放入 `App.vue` 的 `<template>` 区块测试：

```vue
<template>
  <div class="box">
    <h2>你好，{{ username }}！</h2>
    <p>你今年 {{ age }} 岁，明年就是 {{ age + 1 }} 岁了。</p>
    <p>你的状态：{{ isVip ? '尊贵会员' : '普通用户' }}</p>
    <p>用户名大写：{{ username.toUpperCase() }}</p>

    <!-- 警示：不推荐这样使用 HTML -->
    <p v-html="rawHtml"></p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const username = ref('小明')
const age = ref(18)
const isVip = ref(true)
const rawHtml = '<strong style="color:red">这是一段危险的 HTML</strong>'
</script>

<style scoped>
.box {
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 6px;
}
</style>
```

