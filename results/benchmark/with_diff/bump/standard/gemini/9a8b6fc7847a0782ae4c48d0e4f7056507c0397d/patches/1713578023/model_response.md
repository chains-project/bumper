```java
@org.springframework.context.annotation.Bean
public org.acegisecurity.providers.encoding.PasswordEncoder passwordEncoder() {
    org.jasypt.util.password.ConfigurablePasswordEncryptor passwordEncoder = new org.jasypt.util.password.ConfigurablePasswordEncryptor();
    passwordEncoder.setAlgorithm("PBEWITHMD5ANDDES");
    passwordEncoder.setPoolSize(4);
    passwordEncoder.setProviderName("SunJCE");
    passwordEncoder.setSaltGenerator(new org.jasypt.salt.RandomSaltGenerator());
    passwordEncoder.setStringOutputType("base64");
    return passwordEncoder;
}
```