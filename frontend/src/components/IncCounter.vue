<template>
  <div class="container">
    <div class="columns is-centered">
      <div class="column is-half">
        <div class="content has-text-centered">
          <button class="my-button" @click="$emit('inc-event')">+</button>
        </div>
      </div>
    </div>
  </div>
</template>