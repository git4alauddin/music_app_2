import { computed } from "vue";

export default function useSubmitButtonState(user, errors) {

    const isSignupButtonDisabled = computed(() => {
        let disabled = true;
        for (let prop in user) {
            if (!user[prop] || errors[prop]) {
                disabled = true;
                break;
            }
            disabled = false;
        }
        return disabled;
    });

    return { isSignupButtonDisabled }
}