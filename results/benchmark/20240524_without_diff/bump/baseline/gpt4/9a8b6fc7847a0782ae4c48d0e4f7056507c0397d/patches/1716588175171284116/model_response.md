```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new BasicTextEncryptor());
    return encoder;
}
```