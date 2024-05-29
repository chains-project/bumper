Here's a fixed version of the code, using the `BCryptPasswordEncoder` from Spring Security instead of the deprecated `StrongPasswordEncryptor`:

```java
@Override
protected org.springframework.security.crypto.password.PasswordEncoder createStringEncoder() {
    org.springframework.security.crypto.password.PasswordEncoder encoder = new org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder();
    return encoder;
}
```

This code uses the `BCryptPasswordEncoder` from the `org.springframework.security.crypto.bcrypt` package, which is a more secure and recommended alternative to the deprecated `StrongPasswordEncryptor` from Jasypt.