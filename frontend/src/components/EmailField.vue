<template>

    
      
  <div class="form-group">

  <input
    
    type="email"
    placeholder="Email"
    class="form-control"
    autocomplete="off"
    @input="$emit('update:modelValue', $event.target.value)"
    v-model="input"
    @keyup="validateInput"
    @blur="validateInput"
    
  />

<small class="text-danger" v-if="errors.email">
  {{ errors.email }}
</small>
</div>

</template>

<script>
import { ref } from "vue";
import useFormValidation from "@/modules/useFormValidation";
export default {

setup() {
let input = ref("");
const { validateEmailField, errors } = useFormValidation();
const validateInput = () => {
  validateEmailField("email", input.value);
};
return { input, errors, validateInput };
},
};
</script>
