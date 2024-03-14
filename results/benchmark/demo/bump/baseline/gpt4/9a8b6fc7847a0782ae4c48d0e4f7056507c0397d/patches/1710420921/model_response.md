```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = toChars(password);
    try {
        stringEncrypter = new StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);

        if (getProviderName() != null && !getProviderName().isEmpty()) {
            stringEncrypter.setProvider(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());

        PBEPasswordEncoder encoder = new PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);

        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```
In the above code, I replaced the `setProviderName` method with `setProvider` method. This might be the cause of the error as the `setProviderName` method might not exist in the current version of the library you are using. Please ensure that the `setProvider` method exists and accepts a String as argument. If not, you might need to convert the provider name to the appropriate type.