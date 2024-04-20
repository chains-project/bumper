```java
@org.springframework.context.annotation.Bean
public org.acegisecurity.providers.encoding.PasswordEncoder passwordEncoder() {
    org.jasypt.util.password.ConfigurablePasswordEncryptor passwordEncoder = new org.jasypt.util.password.ConfigurablePasswordEncryptor();
    passwordEncoder.setAlgorithm("PBEWITHSHA256AND128BITAES-CBC-BC");
    passwordEncoder.setPoolSize(4);
    passwordEncoder.setProviderName("SunJCE");
    passwordEncoder.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
    passwordEncoder.setStringOutputType("base64");
    return passwordEncoder;
}
```