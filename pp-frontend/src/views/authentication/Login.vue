<template>

	<form id="form-sign-in" v-on:submit="userLogin($event)">

		<img class="logo" src="/android-chrome-512x512.png" alt="logo" width="56" height="56">
		<h1 class="h3 mb-3 fw-normal">Faça login para continuar</h1>

		<div class="form-floating mb-2">
			<input type="text" class="form-control" placeholder="john Doe" v-model="postBody.username">
			<label>Username</label>
		</div>
		<div class="form-floating mb-4">
			<input type="password" class="form-control" placeholder="Password" v-model="postBody.password">
			<label>Password</label>
		</div>
		<button class="w-100 btn btn-lg btn-primary" type="submit">Login</button>
	</form>

</template>


<script>

	import axios from 'axios';

	export default {
		data() {
			return {
				postBody: {
					username: '',
					password: ''
				}
			}
		},
		created() {
			localStorage.removeItem('userData')
		},	
		methods: {
			async userLogin(event) {
				event.preventDefault()

				const payload = this.postBody

				await axios.post('http://localhost:8000/authentication/api/token/', this.postBody)
				.then(response => {
					localStorage.setItem('userData', JSON.stringify(response.data))
					window.location.href = '/'
				})
				.catch(e => {
					console.log(e)
					alert('Credenciais inválidas')
				})
			}
		}
	}

</script>

<style lang="scss">

	body {
		justify-content: center;
	}

	#app {
		display: flex;
		place-items: center;
		height: 100%;
	}

	#form-sign-in {
		display: flex;
		flex-direction: column;
		max-width: 400px;
		margin: auto;

		.logo {
			margin: 0 auto 1rem;
		}
		
	}

</style>