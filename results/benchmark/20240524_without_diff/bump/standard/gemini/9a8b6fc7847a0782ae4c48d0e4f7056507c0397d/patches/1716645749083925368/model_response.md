```java
@java.lang.Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.jasypt.util.password.StrongPasswordEncryptor encryptor = new org.jasypt.util.password.StrongPasswordEncryptor();
    return new org.springframework.security.crypto.password.DelegatingPasswordEncoder("bcrypt",
            new org.springframework.security.crypto.password.MessageDigestPasswordEncoder("MD5"),
            encryptor);
}
```