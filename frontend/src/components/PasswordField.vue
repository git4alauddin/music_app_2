<template>
  
    <div class="form-group">
      
      <input
        type="password"
        placeholder="Password"
        autocomplete="off"
        v-model="input"
        @input="$emit('update:modelValue', $event.target.value)"
        @keyup="validateInput"
        @blur="validateInput"
        class="form-control"
      />
    
    <small class="text-danger" v-if="errors.password">
      {{ errors.password }}
    </small>
    </div>
  
</template>

 <script>
import { ref } from "vue";
import useFormValidation from "@/modules/useFormValidation";
export default {
  setup() {
    let input = ref("");
    const { validatePasswordField, errors } = useFormValidation();
    const validateInput = () => {
      validatePasswordField("password", input.value);
    };
    return { input, errors, validateInput };
  },
};
</script>