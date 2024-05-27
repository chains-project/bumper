```java
@java.lang.Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.jasypt.util.password.StrongPasswordEncryptor encryptor = new org.jasypt.util.password.StrongPasswordEncryptor();
    org.springframework.security.crypto.password.DelegatingPasswordEncoder encoder = new org.springframework.security.crypto.password.DelegatingPasswordEncoder("noop");
    encoder.setPasswordEncoderForMatcher("noop", new org.springframework.security.crypto.password.NoOpPasswordEncoder());
    return encoder;
}
```