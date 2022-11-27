<template>
	
	<nav class="navbar navbar-light bg-light rounded">
		<div class="container-fluid">
			<a class="navbar-brand d-flex align-items-center gap-2 fw-bold" href="/">
				<img src="/android-chrome-512x512.png" alt="" width="30" height="30">
				CRUD
			</a>
			<LogoutBtn />
		</div>
	</nav>

	<main>
		<form id="item-form" @submit="saveItem($event)">
			<div class="d-flex flex-row flex-wrap align-items-end gap-3">
				<div>
					<label class="form-label">Nome</label>
					<input type="text" class="form-control" placeholder="Nome" name="name" autocomplete="off" required>
				</div>
				<div>
					<label class="form-label">Description</label>
					<textarea class="form-control" rows="1" placeholder="Descrição" name="description"></textarea>
				</div>
				<div>
					<label class="form-label">Imagem</label>
					<input class="form-control" type="file" name="img">
				</div>
				<button class="btn btn-primary" type="submit">Salvar</button>
			</div>
		</form>

		<section>
			<div v-for="(item, index) in items" class="card">
				<div class="img-wrapper">
					<img :src="backendHost + item.img" class="card-img-top" alt="img">
				</div>
				<div class="card-body">
					<h5 class="card-title">{{ item.name }}</h5>
					<p class="card-text">{{ item.description }}</p>
					<button class="btn btn-danger" @click="deleteItem(item)">Delete</button>
				</div>
			</div>
		</section>

	</main>

</template>

<script setup>
	import axios from 'axios'
	import Swal from 'sweetalert2'
	import { getUserData, refreshAccessToken } from '@/auth/jwtUtils'
	import LogoutBtn from '@/components/LogoutBtn.vue'
</script>

<script>
	export default {
		data() {
			return {
				items: []
			}
		},
		computed: {
			backendHost() {
				return import.meta.env.VITE_BACKEND_HOST
			},
		},
		created() {
			this.getItems()
		},
		methods: {
			axiosInstance() {
				const instance = axios.create({
					baseURL: this.backendHost
				})
				instance.defaults.headers.common['Authorization'] = 'Bearer ' + getUserData().access
				return instance
			},
			async getItems() {
				const response 	    = await axios.get(this.backendHost + '/core/api/item/list/')
				.catch(e => e.response)
				this.items = this.treatResponse(response)
			},
			async saveItem(event) {
				event.preventDefault()

				var formData = new FormData(event.target)
				
				var axiosInstance = this.axiosInstance()
				var response = await axiosInstance.post('/core/api/item/create/', formData)
				.catch(e => e.response)

				
				if (response.status == 401) {
					await refreshAccessToken(getUserData().refresh)
					
					axiosInstance = this.axiosInstance()
					response 	  = await axiosInstance.post('/core/api/item/create/', formData)
					.catch(e => e.response)
				}

				this.items.unshift(this.treatResponse(response))
				event.target.reset()
			},

			async deleteItem(item) {
				var formData = new FormData()
				formData.append('item_id', item.id)

				var axiosInstance = this.axiosInstance()
				var response 	  = await axiosInstance.delete('/core/api/item/delete/', {'data': formData})
				.catch(e => e.response)


				if (response.status == 401) {
					await refreshAccessToken(getUserData().refresh)
					
					axiosInstance = this.axiosInstance()
					response = await axiosInstance.delete('/core/api/item/delete/', {'data': formData})
					.catch(e => e.response)
				}
				
				if (response.status == 200) {
					this.items.splice(this.items.indexOf(item), 1)

					Swal.fire({
						title: 'Success!',
						text: 'The Item has ben deleted!',
						icon: 'success',
						confirmButtonText: 'Ok'
					})
				}
			},

			treatResponse(response) {
				if (response.status < 400) {
					return response.data
				} else {
					var error = ''
					if (response.data.hasOwnProperty('error')) {
						error = response.data.error
					} else {
						error = response.statusText
					}

					Swal.fire({
						title: 'Error!',
						text: error,
						icon: 'error',
						confirmButtonText: 'Ok'
					})
				}
			}
		}
	}
</script>

<style lang="scss">

	@import "~bootstrap/scss/functions";
	@import "~bootstrap/scss/variables";
	@import "@/assets/scss/variables";
	@import '@sweetalert2/themes/dark/dark.scss';

	main {
		width: 100%;

		section {
			margin-top: 4rem;
			display: flex;
			gap: 1rem;
			flex-wrap: wrap;
			flex-direction: row;

			.card {
				background-color: $body-bg !important;
				border: 2px solid $body-color;
				width: 300px;
				
			}
			.img-wrapper {
				height: 250px; 
				overflow: hidden;

				img {
					transition: transform .5s ease;
					width: 100%;
					height: 100%;
					transform: scale(1.1);
					object-fit: cover;
				}
				&:hover img{
					transform: scale(1);
				}
			}
		}
	}

	#item-form {
		margin-top: 2rem;

		div:not(flex-row) {
			flex: 1 1;
			min-width: 200px;
		}		

		label {
			color: $warning;
		}
	}
</style>
