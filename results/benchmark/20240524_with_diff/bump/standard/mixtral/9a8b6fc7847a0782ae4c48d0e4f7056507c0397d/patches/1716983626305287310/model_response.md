Here's the fixed version of the method using the new library version:

```java
@Override
protected PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = SecurityUtils.toChars(password);
    try {
        StringEncryptor stringEncrypter = new StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        PasswordEncoder encoder = new PasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        SecurityUtils.scramble(password);
        SecurityUtils.scramble(chars);
    }
}
```

The main changes are:

* `PBEPasswordEncoder` is replaced with `PasswordEncoder`
* `PBEStringEncryptor` is injected directly instead of being wrapped in a `PBEPasswordEncoder`
* `setProviderName` and `setAlgorithm` are called on `StringEncryptor` instead of `PBEStringEncryptor`
* `scramble` is called on the original `password` array instead of the `chars` array