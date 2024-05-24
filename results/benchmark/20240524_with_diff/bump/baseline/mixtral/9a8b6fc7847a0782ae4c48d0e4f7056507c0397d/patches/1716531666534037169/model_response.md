Here's the updated `createStringEncoder` method that should resolve the error:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        StringEncryptor stringEncrypter = new StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());

        PasswordEncoder encoder = new PasswordEncoder();
        encoder.setPasswordEncryptor(stringEncrypter);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```

The changes include replacing the `PBEPasswordEncoder` class with the `PasswordEncoder` class and updating the method `setPbeStringEncryptor` to `setPasswordEncryptor`.