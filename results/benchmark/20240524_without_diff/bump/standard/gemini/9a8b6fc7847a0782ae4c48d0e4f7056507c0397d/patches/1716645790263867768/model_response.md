```java
@java.lang.Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.springframework.security.crypto.password.PasswordEncoder encoder = new org.springframework.security.crypto.password.DelegatingPasswordEncoder("bcrypt", new org.springframework.security.crypto.password.MessageDigestPasswordEncoder("MD4"), new org.springframework.security.crypto.password.MessageDigestPasswordEncoder("MD5"));
    encoder.setPasswordEncryptor(new org.jasypt.util.password.StrongPasswordEncryptor());
    return encoder;
}
```