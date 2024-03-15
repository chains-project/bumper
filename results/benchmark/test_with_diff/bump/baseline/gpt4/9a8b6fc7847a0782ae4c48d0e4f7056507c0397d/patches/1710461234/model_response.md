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

        PasswordEncoder encoder = PasswordEncoderFactories.createDelegatingPasswordEncoder();
        encoder = (PasswordEncoder) stringEncrypter;

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```
In this patch, the `PBEPasswordEncoder` class has been replaced with the `PasswordEncoderFactories.createDelegatingPasswordEncoder()` method, as the `PBEPasswordEncoder` class is no longer available in the new library version. The `createDelegatingPasswordEncoder()` method returns a `PasswordEncoder` which is a required return type for the `createStringEncoder()` method. The `stringEncrypter` is then cast to `PasswordEncoder` to fit the required return type.