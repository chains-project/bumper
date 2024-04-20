```java
@org.springframework.context.annotation.Bean
public org.acegisecurity.providers.encoding.PasswordEncoder passwordEncoder() {
    org.jasypt.util.password.ConfigurablePasswordEncryptor passwordEncoder = new org.jasypt.util.password.ConfigurablePasswordEncryptor();
    passwordEncoder.setEncryptor(encryptor); // Existing line
    passwordEncoder.setPassword(password); // Existing line

    // New code to set the algorithm:
    passwordEncoder.setAlgorithm("PBEWITHMD5ANDDES");

    return passwordEncoder;
}
``` 
