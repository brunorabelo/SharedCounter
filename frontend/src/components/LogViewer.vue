<template>
  <div>
    <label class="label">Logs</label>
    <div class="control">
      <textarea
        class="textarea"
        cols="50"
        rows="10"
        v-model="messages"
      ></textarea>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    messages: String,
  },
};
</script>