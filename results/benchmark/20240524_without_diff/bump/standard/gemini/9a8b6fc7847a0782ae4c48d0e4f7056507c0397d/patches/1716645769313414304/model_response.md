```java
@java.lang.Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.springframework.security.crypto.password.PasswordEncoder encoder = new org.springframework.security.crypto.password.PasswordEncoder();
    encoder.setPasswordEncoder(new org.jasypt.util.password.StrongPasswordEncryptor());
    return encoder;
}
```