```
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new StrongPasswordEncryptor());
    return encoder;
}
```