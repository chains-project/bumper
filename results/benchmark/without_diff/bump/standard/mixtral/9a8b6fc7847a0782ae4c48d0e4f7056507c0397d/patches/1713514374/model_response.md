Here's a fixed version of the method that removes the usage of the removed library method `it.geosolutions.geostore.core.security.password.SecurityUtils.scramble(password);` and uses an alternative way to scramble the password:

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
        // Replace the scramble method with a custom one
        for (int i = 0; i < chars.length; i++) {
            chars[i] = (char) (chars[i] ^ 0x12);
        }
    }
}
```

This version of the method uses an XOR operation to scramble the characters in the `chars` array, instead of using the `SecurityUtils.scramble` method. The XOR operation is performed with the hexadecimal value `0x12`. This is just one way to scramble the characters, and you can replace it with any other method that better fits your needs.