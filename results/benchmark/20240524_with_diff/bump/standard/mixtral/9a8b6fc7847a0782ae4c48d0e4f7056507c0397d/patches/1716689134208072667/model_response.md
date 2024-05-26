Here's a patch that you can apply to the failing client code:
```java
@java.lang.Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setTextEncryptor(new org.jasypt.util.text.StrongTextEncryptor());
    return encoder;
}
```
In this patch, we replaced the deprecated `setPasswordEncryptor` method with the new `setTextEncryptor` method. We also replaced the `StrongPasswordEncryptor` class with the `StrongTextEncryptor` class, which is the new class that should be used for encryption.