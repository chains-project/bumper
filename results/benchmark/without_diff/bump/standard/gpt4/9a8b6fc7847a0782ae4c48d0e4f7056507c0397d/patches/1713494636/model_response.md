```java
@java.lang.Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.springframework.security.crypto.password.Pbkdf2PasswordEncoder encoder = new org.springframework.security.crypto.password.Pbkdf2PasswordEncoder();
    return encoder;
}
```