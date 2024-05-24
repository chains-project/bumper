Here's the fixed version of the method:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setPasswordEncryptor(new org.jasypt.util.password.StrongPasswordEncryptor());
    return encoder;
}
```

I replaced the import for `PasswordEncoder` and `StrongPasswordEncryptor` with their full package names from the updated library version. This ensures that the correct classes are used.