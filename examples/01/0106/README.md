## ✅ 构建一个「自我介绍页面」

大家好，我是三日老师。

今天我们来做一个简单又实用的 Vue 小项目：**自我介绍页面**。

这个项目看似基础，却可以帮你一次性掌握以下 Vue 3 的核心知识点：

---

### 📌 你将用到的知识点：

* 插值表达式 `{{ }}`
* 数据绑定 `v-bind`（或简写 `:`）
* 表单双向绑定 `v-model`
* 条件渲染 `v-if`
* 列表渲染 `v-for`
* 事件处理 `@click`
* 基础样式与响应式逻辑

---

### 💡 项目逻辑设计：

我们要做一个「自我介绍卡片」，用户可以输入自己的名字、性别、兴趣爱好、一句话介绍，然后点击“生成”，页面会展示这张信息卡。

如果没有填写，提示用户填写完整信息。

---

### 🧠 实战的训练目标：

通过这个案例，你可以：

1. 掌握 Vue 数据如何双向绑定
2. 学会让“按钮”控制视图变化
3. 理解 Vue 是如何让数据驱动视图更新的

---

本节内容非常适合新手，也能打下后续深入学习的基础。

接下来我们来实现这个功能。

本节讲解完毕，我们看代码！

---

## 💻 构建一个「自我介绍页面」（代码部分）

你可以直接将以下代码写入 `App.vue` 文件中：

```vue
<template>
  <div class="card">
    <h2>填写你的信息</h2>

    <input v-model="name" placeholder="你的名字" />
    <select v-model="gender">
      <option disabled value="">请选择性别</option>
      <option>男</option>
      <option>女</option>
    </select>
    <textarea v-model="bio" placeholder="一句话介绍你自己"></textarea>

    <button @click="showIntro = true" :disabled="!name || !gender || !bio">
      生成介绍卡片
    </button>

    <div v-if="showIntro" class="intro">
      <h3>👋 你好，我是 {{ name }}</h3>
      <p>性别：{{ gender }}</p>
      <p>自我介绍：{{ bio }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('')
const gender = ref('')
const bio = ref('')
const showIntro = ref(false)
</script>

<style scoped>
.card {
  width: 300px;
  margin: 30px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}
input,
select,
textarea {
  display: block;
  width: 100%;
  margin-bottom: 12px;
  padding: 6px;
}
button {
  padding: 8px 16px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.intro {
  margin-top: 20px;
  padding: 12px;
  border-top: 1px dashed #aaa;
}
</style>
```

---

🔄 页面交互说明：

1. 输入信息后点击按钮，才会展示自我介绍区域；
2. 表单使用 `v-model` 进行数据绑定；
3. `v-if="showIntro"` 控制介绍卡片的出现；
4. 使用了 Vue 最常见的指令：`v-model`, `v-if`, `@click`, `{{ }}`。

