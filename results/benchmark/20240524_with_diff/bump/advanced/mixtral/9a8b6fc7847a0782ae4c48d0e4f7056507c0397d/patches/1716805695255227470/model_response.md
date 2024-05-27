Here's a fixed version of the `createStringEncoder()` method that takes into account the changes in the new library version:

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

The changes I made are:

* Replacing `PBEPasswordEncoder` with `PasswordEncoder` for the `encoder` variable.
* Removing the import for `org.jasypt.spring.security.PBEPasswordEncoder` since it is no longer needed.
* Adding an import for `org.jasypt.spring.security.PasswordEncoder` since it is now used instead.