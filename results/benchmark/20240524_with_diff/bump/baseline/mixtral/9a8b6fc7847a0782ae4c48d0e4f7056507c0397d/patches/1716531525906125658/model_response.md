Here's the fixed `createStringEncoder` method:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        PBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            encryptor.setProviderName(getProviderName());
        }
        encryptor.setAlgorithm(getAlgorithm());

        PasswordEncoder passwordEncoder = new PasswordEncoder();
        passwordEncoder.setPasswordEncryptor(encryptor);

        return passwordEncoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```

In the updated code, I replaced the usage of `PBEPasswordEncoder` with `PasswordEncoder` and used the new method `setPasswordEncryptor` instead of `setPbeStringEncryptor`.