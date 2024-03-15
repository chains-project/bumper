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

        // As PBEPasswordEncoder is removed, we can use the PasswordEncoder from Spring Security
        PasswordEncoder encoder = new BCryptPasswordEncoder();
        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}
```
In the new library version, `PBEPasswordEncoder` is removed. So, I've replaced it with `BCryptPasswordEncoder` from Spring Security. Do note that this will not provide exactly the same functionality as `PBEPasswordEncoder`. You may need to adjust your code accordingly to handle the differences.