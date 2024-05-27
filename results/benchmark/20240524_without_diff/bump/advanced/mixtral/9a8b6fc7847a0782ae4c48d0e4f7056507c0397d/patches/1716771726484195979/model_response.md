Here's the fixed `createStringEncoder()` method:
```java
@Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setPasswordEncryptor(new org.jasypt.util.password.ConfigurablePasswordEncryptor());
    return encoder;
}
```
The change is in the instantiation of `org.jasypt.util.password.ConfigurablePasswordEncryptor()`.
`StrongPasswordEncryptor` is deprecated in newer versions of Jasypt, and the `ConfigurablePasswordEncryptor` should be used instead.
This should resolve the "cannot find symbol" error you've encountered.