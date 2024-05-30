Here's the proposed patch for the failing `createStringEncoder()` method:
```java
@Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setTextEncryptor(new org.jasypt.util.text.StrongTextEncryptor());
    return encoder;
}
```
In this patch, I replaced the `setPasswordEncryptor()` method with `setTextEncryptor()` to adapt to the new library version. The `StrongTextEncryptor` class is a direct replacement for the removed `StrongPasswordEncryptor` class.