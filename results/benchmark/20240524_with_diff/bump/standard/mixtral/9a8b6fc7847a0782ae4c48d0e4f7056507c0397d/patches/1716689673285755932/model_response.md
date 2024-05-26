Here is the updated `createStringEncoder` method with the necessary changes to fix the error:

```java
@java.lang.Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = it.geosolutions.geostore.core.security.password.SecurityUtils.toChars(password);
    try {
        org.jasypt.util.text.TextEncryptor textEncryptor = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        ((org.jasypt.encryption.pbe.PBEStringEncryptor) textEncryptorg).setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            ((org.jasypt.encryption.pbe.PBEStringEncryptor) textEncryptorg).setProviderName(getProviderName());
        }
        ((org.jasypt.encryption.pbe.PBEStringEncryptor) textEncryptorg).setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setTextEncryptor(textEncryptorg);
        return encoder;
} finally {
    it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);
    it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(chars);
    }
}
```

In this updated version, I replaced the `org.jasypt.spring.security.PBEPasswordEncoder` class with the new `org.jasypt.util.text.TextEncryptor` class, which has the same functionality but is not deprecated. I also updated the way the `PBEStringEncryptor` is set on the `PBEPasswordEncoder` to use the new `setTextEncryptor` method.

Note that I had to cast the `textEncryptorg` variable to `org.jasypt.encryption.pbe.PBEStringEncryptor` in a few places to access the deprecated methods that were removed in the new version.

I hope this helps!