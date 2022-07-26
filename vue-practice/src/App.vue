<template>
  <div>
    <h1>hello vue!!</h1>
    <h1>머스타치: {{ animal }}</h1>
    <h2>원숭이는 {{ food }}를 좋아합니다.</h2>
    <h3 v-text="food"></h3>
    <input type="text" v-model="food" />
    <div v-html="alertMessage"></div>
    <div v-html="subscribeHTML"></div>
    <img v-bind:src="imageSource" alt="random" />
    <br />
    <a v-bind:href="naverUrl">naver</a>
    <br />
    <a :href="naverUrl">naver 2</a>
    <br />
    <a :href="food">{{ food }}</a>
    <hr />
    <h2 :class="{ red: food === 'apple', 'not-good': food === 'rice' }">
      원숭이는 {{}} 를 좋아합니다.
    </h2>
    <!-- <h2 :class="{'not-good': }">원숭이는 {{}} 를 좋아합니다.</h2> -->
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
      imageSource: 'https://placeimg.com/100/100/any',
      naverUrl: 'https://www.naver.com',
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

.orange {
  color: orange;
}

.salmon {
  color: salmon;
}

.red {
  color: red;
}

.not-good {
  text-decoration: line-through;
}
</style>
