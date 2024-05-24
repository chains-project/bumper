Here's the patched method:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setPasswordEncryptor(new org.jasypt.util.password.StrongPasswordEncryptor());
    return encoder;
}
```

I replaced the fully qualified class name of `PasswordEncoder` and `StrongPasswordEncryptor` with the new ones from the updated library version.