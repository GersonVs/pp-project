<template>
	<div class="custom-nav-link">
		<router-link 
			:to="{ name: 'home' }" 
			:class="{'active': currentPage == 'home'}, 'btn btn-outline-waring'"> 
			Home 
		</router-link>
		<router-link 
			:to="{ name: 'about' }"  
			:class="{'active': currentPage == 'about'}, 'btn btn-outline-waring'">
			About
		</router-link>
	</div>
</template>

<script>
	import { RouterLink } from 'vue-router'

	export default {
		props: {
			currentPage: String,
		}
	}
</script>

<style lang="scss">

	@import "~bootstrap/scss/functions";
    @import "~bootstrap/scss/variables";

	.custom-nav-link {
		display: flex;
		justify-content: center;
		gap: 1rem;

		a {
			border: 2px solid #FFB400;
			padding: .5rem 1rem;
			color: #FFB400;
			text-decoration: none;
			border-radius: $border-radius;
			
			&:focus, &.active {
				background-color: #FFB400;
				color: #fff;
			}
		}
	}

</style>
