<template>
  <div>
    <h1>hello vue!!</h1>
    <h1>머스타치: {{ animal }}</h1>
    <h2>원숭이는 {{ food }}를 좋아합니다.</h2>
    <h3 v-text="food"></h3>
    <input type="text" v-model="food" />
    <div v-html="alertMessage"></div>
    <div v-html="subscribeHTML"></div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      animal: 'Monkey',
      food: 'banana',
      alertMessage: '<h2>경고 ! !</h2>',
      subscribeHTML: `<button onclick="document.querySelector('body').style.display = 'none'">구독하기</button>`,
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
input {
  font-size: 30px;
}
</style>
