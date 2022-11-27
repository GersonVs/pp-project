<template>
    <button class="btn btn-outline-secondary" @click="counter++">
        {{ counter }}
    </button>
</template>

<script>

    export default {
        props: {
            counter: {
                type: Number,
                default: 0
            } 
        }
    }

</script>

<style lang="scss">
    button {
        &:hover {
            background-color: unset !important; 
            color: unset !important;
        }
    }
</style>