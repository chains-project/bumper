```java
@org.springframework.context.annotation.Bean
public org.acegisecurity.providers.encoding.PasswordEncoder passwordEncoder() {
    org.jasypt.util.password.ConfigurablePasswordEncryptor passwordEncoder = new org.jasypt.util.password.ConfigurablePasswordEncryptor();
    passwordEncoder.setStringEncryptor(encryptor); // ++ using setStringEncryptor instead of setEncryptor
    passwordEncoder.setPassword(password);
    return passwordEncoder;
}
```