<template>
    <main>
        <NavLink currentPage='about'/>
        <h1>About</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias quis rerum animi doloribus neque quam facere voluptas mollitia ex voluptatem ipsum dolore distinctio dignissimos, sint itaque porro labore natus. Magnam!</p>
    </main>
</template>

<script setup>
    import NavLink from '@/components/NavLink.vue';
</script>

<style lang="scss">
    main {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 2rem;

        p {
            margin: 0;
            text-align: justify;
            max-width: 600px;
        }
    }
</style>
