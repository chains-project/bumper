```java
@java.lang.Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.springframework.security.crypto.password.PasswordEncoder encoder = new org.springframework.security.crypto.password.DelegatingPasswordEncoder("bcrypt",
            "MD4", "MD5", "SHA-1", "SHA-256", "SHA-384", "SHA-512", "noop", "pbkdf2", "scrypt");
    return encoder;
}
```