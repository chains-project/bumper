Here's a fixed version of the `createStringEncoder()` method that uses the new `PasswordEncoder` class from the updated library:

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

        PasswordEncoder encoder = new PasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```

In this version, I replaced the `PBEPasswordEncoder` class with the new `PasswordEncoder` class from the updated library. I also removed the `setAlgorithm()` method call, since it is no longer available in the new `PasswordEncoder` class.