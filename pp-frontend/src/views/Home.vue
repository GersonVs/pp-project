<template>
    <main>
        <NavLink currentPage='home'/>
        <h1>Home</h1>
        <CounterButton />
    </main>
</template>

<script setup>
    import CounterButton from '@/components/CounterButton.vue';
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
    }
</style>
