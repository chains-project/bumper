```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PooledPasswordEncoder();
    encoder.setPoolablePasswordEncryptor(new StrongPasswordEncryptor());
    return encoder;
}
```