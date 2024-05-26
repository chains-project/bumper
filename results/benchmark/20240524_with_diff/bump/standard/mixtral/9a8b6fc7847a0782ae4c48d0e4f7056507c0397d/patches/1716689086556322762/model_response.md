Here's the patched version of the `createStringEncoder` method that should fix the error:
```java
@java.lang.Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setTextEncryptor(new org.jasypt.util.text.StrongTextEncryptor());
    return encoder;
}
```
The change here is that I replaced `setPasswordEncryptor` with `setTextEncryptor` to match the new method name in the updated library. I also changed the constructor call from `StrongPasswordEncryptor` to `StrongTextEncryptor` for consistency.