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

In the updated code, I replaced the `PBEPasswordEncoder` with `TextEncryptor`, as the former is no longer available in the new library version. I then used the `TextEncryptor` to create a `BCryptPasswordEncoder` instance, which is the recommended way to handle password encoding in the new library version. The rest of the code remains unchanged.