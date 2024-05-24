Here's the updated method with the necessary changes to fix the error:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setPasswordEncryptor(new org.jasypt.util.password.StrongPasswordEncryptor());
    return encoder;
}
```

This code replaces the old `PasswordEncoder` and `StrongPasswordEncryptor` imports with their fully-qualified names from the updated library version.