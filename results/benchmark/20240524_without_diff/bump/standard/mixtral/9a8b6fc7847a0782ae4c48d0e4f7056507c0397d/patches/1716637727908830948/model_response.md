Here's the proposed patch:
```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new StrongPasswordEncryptor());
    return encoder;
}
```
In this patch, I replaced the fully qualified class names with their simple names, assuming that the required classes are imported. This should fix the "cannot find symbol" error.