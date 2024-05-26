```java
@java.lang.Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.springframework.security.crypto.password.PasswordEncoder encoder = new org.springframework.security.crypto.password.MessageDigestPasswordEncoder("SHA-256");
    return encoder;
}
```