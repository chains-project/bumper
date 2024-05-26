Here is a patch that you can apply to the failing client code:

```java
@java.lang.Override
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
        org.jasypt.spring.security.PasswordEncoder encoder = new org.jasypt.spring.security.PasswordEncoder();
        encoder.setPasswordEncryptor(stringEncrypter);
        return encoder;
    } finally {
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
        it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

The changes I made are:

* I replaced the deprecated constructor `PBEPasswordEncoder()` with the constructor `PasswordEncoder()`.
* I replaced the deprecated method `setPbeStringEncryptor()` with the method `setPasswordEncryptor()`.

I also added the fully qualified names for the classes and methods that were removed, to make the code compile.

Note that the `PBEPasswordEncoder` class has been deprecated, and the `PasswordEncoder` class should be used instead. However, since the method signature must not be changed, I had to use the `PasswordEncoder` class in a way that is compatible with the original `PBEPasswordEncoder` class. This means that the `setPasswordEncryptor()` method is used to set the `stringEncrypter` object, and the `encodePassword()` and `isPasswordValid()` methods are used in the same way as before.