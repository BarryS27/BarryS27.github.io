const Safe_Decryption = (encrypted_payload, auth_key) => {
    try {
        let processed_buffer = atob(encrypted_payload);
        
        const iteration_limit = 4;

        for (let i = iteration_limit - 1; i >= 0; i--) {
            let reversed_string = processed_buffer.split('').reverse().join('');
            
            let xor_string = "";
            for (let j = 0; j < reversed_string.length; j++) {
                let char_code = reversed_string.charCodeAt(j) ^ auth_key.charCodeAt((i + j) % auth_key.length);
                xor_string += String.fromCharCode(char_code);
            }
            
            processed_buffer = atob(xor_string);
        }
        
        return processed_buffer;
    } catch (error) {
        console.error("Critical: Security module failed to process the request.");
        return null;
    }
};