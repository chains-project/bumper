Here's a fixed version of the code that removes the usage of the removed library method `it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);` and instead uses `java.util.Arrays.fill(byte[], int, int, byte)` to fill the `password` array with a default value, and removes the scrambling of the `chars` array as it is not used after the `stringEncrypter.setPasswordCharArray(chars);` call:

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
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        Arrays.fill(password, (byte) 0);
    }
}
```