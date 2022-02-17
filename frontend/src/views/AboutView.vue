<template>
  <section class="hero is-fullheight-with-navbar">
    <div class="hero-head">
      <div class="container has-text-centered mt-6">
        <div class="is-size-1">Meet our team</div>
      </div>
    </div>
    <div class="hero-body">
      <div class="container">
        <div class="columns">
          <div class="column"></div>
          <div class="column">
            <Bruno />
          </div>
          <div class="column jordan"><Jordan /></div>
          <div class="column"><Guile /></div>
          <div class="column"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Bruno from "@/components/about/Bruno.vue";
import Jordan from "@/components/about/Jordan.vue";
import Guile from "@/components/about/Guile.vue";
export default {
  components: {
    Bruno,
    Jordan,
    Guile,
  },
};
</script>

<style>
.jordan {
  height: 100%;
}
</style>
