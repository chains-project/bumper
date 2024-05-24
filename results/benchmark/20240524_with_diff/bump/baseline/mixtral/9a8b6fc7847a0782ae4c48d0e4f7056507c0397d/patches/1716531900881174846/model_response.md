Here's the proposed patch:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setPasswordEncryptor(new org.jasypt.util.password.StrongPasswordEncryptor());
    return encoder;
}
```

I replaced the old `PasswordEncoder` and `StrongPasswordEncryptor` classes with their fully-qualified names from the new library version.