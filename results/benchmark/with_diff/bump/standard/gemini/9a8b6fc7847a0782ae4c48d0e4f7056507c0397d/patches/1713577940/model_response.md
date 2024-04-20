```java
@org.springframework.context.annotation.Bean
public org.acegisecurity.providers.encoding.PasswordEncoder passwordEncoder() {
    org.jasypt.util.password.ConfigurablePasswordEncryptor passwordEncoder = new org.jasypt.util.password.ConfigurablePasswordEncryptor();
    passwordEncoder.setEncryptor(encryptor);
    passwordEncoder.setStringDigester(stringDigester); // Using added method to set StringDigester
    passwordEncoder.setPassword(password);
    return passwordEncoder;
}
``` 
