Here's a fixed version of the method that uses the new library version:

```java
@Override
protected org.jasypt.spring.security.PasswordEncoder createStringEncoder() {
    org.jasypt.util.text.TextEncryptor encryptor = new org.jasypt.util.text.StrongTextEncryptor();
    encryptor.setPassword("your-password-here");

    org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
    encoder.setTextEncryptor(encryptor);
    return encoder;
}
```

Note that you'll need to replace "your-password-here" with an actual password that you want to use for encryption. Also, since the `PBEPasswordEncoder` class has been removed, I've used `TextEncryptor` instead for encryption.