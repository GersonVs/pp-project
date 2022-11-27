<template>
	
	<nav class="navbar navbar-light bg-light rounded">
		<div class="container-fluid">
			<a class="navbar-brand d-flex align-items-center gap-2 fw-bold" href="/">
				<img src="/android-chrome-512x512.png" alt="" width="30" height="30">
				Vote
			</a>
		</div>
	</nav>

	<main>
		<section>
			<div v-for="(item, index) in items" class="card">
				<div class="img-wrapper">
					<img :src="backendHost + item.img" class="card-img-top" alt="img">
				</div>
				<div class="card-body">
					<h5 class="card-title">{{ item.name }}</h5>
					<p class="card-text">{{ item.description }}</p>
					<div class="d-flex flex-row align-items-center justify-content-between">
						<button class="btn btn-primary" @click="voteItem(item)">Vote</button>
						<span class="badge bg-secondary">{{ item.votes }}</span>
					</div>
				</div>
			</div>
		</section>
	</main>

</template>

<script setup>
	import Swal from 'sweetalert2'
	import axios from 'axios';
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
			}
		},
		created() {
			this.getItems()
		},
		methods: {
			async getItems() {
				const response = await axios.get(`${this.backendHost}/core/api/item/list/`)
				.catch(e => e.response)
				
				this.items = this.treatResponse(response)
			},

			async voteItem(item) {
				const formData = new FormData()
				formData.append('item_id', item.id)

				const response = await axios.post(`${this.backendHost}/core/api/item/vote/`, formData)
				.catch(e => e.response)

				if (response.status < 400) {

					Swal.fire({
						title: 'Success!',
						text: 'Your vote has been saved!',
						icon: 'success',
						confirmButtonText: 'Ok'
					}).then(action => {
						item.votes = this.treatResponse(response).votes
					})
				}

			},
			treatResponse(response) {
				if (response.status < 400) {
					return response.data
				} 
				else {
					if (response.data.hasOwnProperty('error')) {
						console.log(response.data.error)
					} else {
						console.log(response.statusText)
					}
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
</style>
