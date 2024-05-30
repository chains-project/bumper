Here's the fixed version of the `createStringEncoder()` method:
```java
@Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setTextEncryptor(new org.jasypt.util.text.StrongTextEncryptor());
    return encoder;
}
```
The change is to replace `setPasswordEncryptor()` with `setTextEncryptor()` because the `PBEPasswordEncoder` class has been removed, and the new `PasswordEncoder` class uses a `TextEncryptor` instead of a `PasswordEncryptor`.