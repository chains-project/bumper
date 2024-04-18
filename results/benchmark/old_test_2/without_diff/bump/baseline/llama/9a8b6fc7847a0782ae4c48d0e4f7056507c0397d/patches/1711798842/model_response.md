```
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new StrongPasswordEncryptor());
    return encoder;
}
```

Replace with:
```
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new BCryptPasswordEncryptor());
    return encoder;
}
```

The `StrongPasswordEncryptor` class has been removed in the latest version of the library, so we need to replace it with the `BCryptPasswordEncryptor` class which is the suggested replacement.