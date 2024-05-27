Here's the fixed version of the `createStringEncoder()` method using the new library version:
```java
@Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setTextEncryptor(new org.jasypt.util.text.StrongTextEncryptor());
    return encoder;
}
```
The method signature remains unchanged, and the `setPasswordEncryptor` method has been replaced with the `setTextEncryptor` method. Additionally, the `StrongTextEncryptor` class is used instead of `StrongPasswordEncryptor`.