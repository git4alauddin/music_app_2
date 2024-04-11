<template>
  
  <div class="form-group">
    <i class="user icon"></i>
    <input
      type="text"
      placeholder="Full Name"
      class="form-control"
      autocomplete="off"
      @input="$emit('update:modelValue', $event.target.value)"
      v-model="input"
      @keyup="validateInput"
      @blur="validateInput"
    />
  
  <small class="text-danger" v-if="errors.name">
    {{ errors.name }}
  </small>
</div>

</template>

<script>
import { ref } from "vue";
import useFormValidation from "@/modules/useFormValidation";
export default {
setup() {
  let input = ref("");
  const { validateNameField, errors } = useFormValidation();
  const validateInput = () => {
    validateNameField("name", input.value);
  };
  return { input, errors, validateInput };
},
};
</script>




