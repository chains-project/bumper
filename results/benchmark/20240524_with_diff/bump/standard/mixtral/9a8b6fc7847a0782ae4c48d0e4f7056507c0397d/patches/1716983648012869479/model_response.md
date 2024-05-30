Here's a possible patch that you can apply to the code to fix the error:

```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        stringEncrypter.setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        org.jasypt.util.text.TextEncryptor encryptor = new org.jasypt.util.text.BasicTextEncryptor();
        encryptor.setPassword(new String(chars));
        encryptor.setAlgorithm(getAlgorithm());
        org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setPasswordEncryptor(encryptor);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

The changes I made include:

* Replacing `org.jasypt.spring.security.PBEPasswordEncoder` with `org.jasypt.spring.security.PasswordEncoder`, as the former has been removed.
* Using a `TextEncryptor` instance instead of a `PBEStringEncryptor` instance to encrypt the password.
* Configuring the `TextEncryptor` instance with the same algorithm as the `PBEStringEncryptor`.
* Setting the password of the `TextEncryptor` instance to a string representation of the password char array.
* Calling the `setPasswordEncryptor` method of the `PasswordEncoder` instance instead of the `setPbeStringEncryptor` method.

These changes should allow the code to compile and run correctly with the new library version.