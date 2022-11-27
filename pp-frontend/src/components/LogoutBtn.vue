<template>
    <button id="logout-btn" class="btn btn-outline-danger" @click="logout()">{{ userData.username }}</button>
</template>


<script>
	export default {
		data() {
			return {
				userData: {}
			}
		},
		created() {
			this.userData = JSON.parse(localStorage.getItem('userData'))
		},	
		methods: {
            logout() {
                window.location.href = '/login'
            }
			
		}
	}

</script>

<style lang="scss">

    @import "~bootstrap/scss/functions";
    @import "~bootstrap/scss/variables";

    #logout-btn {
        transition: all ease .7s;

        &:hover {
            background-color: $danger !important;
            
            &::after {
                content: ": sair 👋";

            }
        }
    }

</style>