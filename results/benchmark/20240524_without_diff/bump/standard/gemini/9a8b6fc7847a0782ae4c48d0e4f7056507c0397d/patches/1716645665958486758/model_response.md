```java
@java.lang.Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.springframework.security.crypto.password.PasswordEncoder encoder = new org.springframework.security.crypto.password.NoOpPasswordEncoder.getInstance();
    encoder.setPasswordEncryptor(new org.jasypt.util.password.StrongPasswordEncryptor());
    return encoder;
}
```