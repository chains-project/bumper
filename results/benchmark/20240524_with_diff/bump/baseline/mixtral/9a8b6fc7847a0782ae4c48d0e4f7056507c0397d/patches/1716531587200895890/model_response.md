Here's the fixed `createStringEncoder` method:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();

    char[] chars = toChars(password);
    try {
        stringEncrypter = new StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());

        TextEncryptor encryptor = new TextEncryptor();
        encryptor.setPbeStringEncryptor(stringEncrypter);

        return new BCryptPasswordEncoder(12, encryptor);
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```

I replaced the `PBEPasswordEncoder` with `BCryptPasswordEncoder`, and used `TextEncryptor` to set the `PBEStringEncryptor`.