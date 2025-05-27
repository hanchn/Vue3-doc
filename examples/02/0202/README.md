## ✅ v-bind：动态绑定属性

大家好，我是三日老师。

在上一节我们讲了插值表达式是如何把「数据」插到「文本内容」中。
但很多时候我们想要绑定的是**HTML 属性值**，比如图片地址、按钮状态、元素样式，这就需要用到今天的主角：`v-bind`。

---

### 🔹1. 什么是 `v-bind`？

`v-bind` 是 Vue 提供的指令，用于将 JavaScript 数据**绑定到 HTML 属性上**。
格式是：

```html
v-bind:属性名="变量"
```

可以简写成：

```html
:属性名="变量"
```

比如绑定图片地址：

```html
<img :src="avatarUrl" />
```

---

### 🔹2. 绑定 class 和 style 是重点用法

#### 动态 class（字符串形式）：

```html
<div :class="themeClass"></div>
```

#### 动态 class（对象形式）：

```html
<div :class="{ active: isActive, disabled: !isActive }"></div>
```

#### 动态 style（对象形式）：

```html
<div :style="{ color: textColor, fontSize: fontSize + 'px' }"></div>
```

这是开发中非常常见的做法，可以根据状态变化实时改变样式。

---

### 🔹3. 动态绑定 disabled / title / href 等属性

你还可以绑定各种布尔值、文本值属性：

```html
<button :disabled="isLoading">提交</button>
<a :href="link" :title="title">跳转</a>
```

---

### 🔹4. 绑定多个属性的写法（v-bind 对象展开）

```html
<img v-bind="{ src: avatarUrl, alt: '头像', width: 100 }" />
```

这种形式适合同时绑定多个属性值，是对象展开的高级用法。

---

### 总结

`v-bind` 是 Vue 连接 JS 和 HTML 的“桥梁”。
它让你不仅可以控制“显示什么”，还可以控制“怎么显示”。

掌握 `v-bind`，就可以灵活控制页面元素的各种行为和状态。

下一节我们将进入用户交互的第一步 —— 事件绑定 `v-on`。

本节讲解完毕，我们看代码！

---

## 💻 v-bind：动态绑定属性（代码部分）

将以下代码放入 `App.vue` 中即可测试：

```vue
<template>
  <div class="card" :class="{ vip: isVip }" :style="{ borderColor: borderColor }">
    <h2>{{ name }}</h2>
    <img :src="avatarUrl" :alt="name" width="100" />

    <p>当前状态：<span :title="isVip ? 'VIP 用户' : '普通用户'">{{ isVip ? '尊贵' : '普通' }}</span></p>

    <button :disabled="isVip">成为 VIP</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('小王')
const avatarUrl = 'https://placekitten.com/100/100'
const isVip = ref(true)
const borderColor = ref('#42b983')
</script>

<style scoped>
.card {
  border: 2px solid #ddd;
  padding: 20px;
  width: 280px;
  margin: 20px auto;
  border-radius: 8px;
}
.vip {
  background-color: #f0fff0;
}
</style>
```

---

这一小节展示了：

* 动态绑定 `src`、`alt`、`title`
* 动态绑定 class 和 style
* 控制按钮的禁用状态

