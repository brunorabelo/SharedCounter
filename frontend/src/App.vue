<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div>
      <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
          <a class="navbar-item"> VueDjango </a>

          <a
            role="button"
            class="navbar-burger burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbarBasicExample"
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
          <div class="navbar-start">
            <RouterLink class="navbar-item" to="/">Home</RouterLink>
          </div>
          <div class="navbar-end">
            <div class="navbar-item">
              <div class="buttons">
                <a class="is-primary button" href="http://localhost:8000/admin"
                  ><strong>Admin</strong></a
                >
              </div>
            </div>
          </div>
        </div>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style>
@import "bulma/css/bulma.css";
</style>
