<template>
  <div class="testrin">
    <h1>登录</h1>
    <input type="text" v-model="username"><br>
    <a type="button" @click="doLogin">提交</a>
  </div>
</template>

<script>
export default {
  name: 'testrin',
  data () {
    return {
      username: ''
    }
  },
  methods: {
    doLogin () {
      this.$axios.request(
        {
          url: 'http://127.0.0.1:8033/regist/',
          method: 'POST',
          data: {
            'username': this.username
          },
          responseType: 'json'
        }
      ).then(function (response) {
        console.log(response.data)
      })
      console.log(this.username)
    }
  }
}
</script>
