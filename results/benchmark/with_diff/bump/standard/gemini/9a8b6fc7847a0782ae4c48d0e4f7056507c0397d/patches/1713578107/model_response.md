```java
@org.springframework.context.annotation.Bean
public org.acegisecurity.providers.encoding.PasswordEncoder passwordEncoder() {
    org.jasypt.util.password.ConfigurablePasswordEncryptor passwordEncoder = new org.jasypt.util.password.ConfigurablePasswordEncryptor();
    passwordEncoder.setAlgorithm("PBEWithMD5AndDES");
    passwordEncoder.setPlainDigest(true);
    passwordEncoder.setPassword(password);
    return passwordEncoder;
}
```