Here's the patched method with the error fixed:

```java
@Override
protected org.acegisecurity.providers.encoding.PasswordEncoder createStringEncoder() {
    byte[] password = lookupPasswordFromKeyStore();
    char[] chars = toChars(password);
    try {
        stringEncrypter = new org.jasypt.encryption.pbe.StandardPBEStringEncryptor();
        ((org.jasypt.encryption.pbe.StandardPBEStringEncryptor) stringEncrypter).setPasswordCharArray(chars);
        if ((getProviderName() != null) && (!getProviderName().isEmpty())) {
            stringEncrypter.setProviderName(getProviderName());
        }
        stringEncrypter.setAlgorithm(getAlgorithm());
        it.geosolutions.geostore.core.security.password.PBEPasswordEncoder encoder = new it.geosolutions.geostore.core.security.password.PBEPasswordEncoder();
        encoder.setPbeStringEncryptor(stringEncrypter);
        return encoder;
    } finally {
        scramble(password);
        scramble(chars);
    }
}

private char[] toChars(byte[] password) {
    return new String(password).toCharArray();
}

private void scramble(char[] chars) {
    for (int i = 0; i < chars.length; i++) {
        chars[i] = (char) (chars[i] ^ 0xFF);
    }
}

private void scramble(byte[] bytes) {
    for (int i = 0; i < bytes.length; i++) {
        bytes[i] = (byte) (bytes[i] ^ 0xFF);
    }
}
```

The changes include:

1. Added a new `toChars` method that converts a `byte[]` to a `char[]` using `String.toCharArray()`.
2. Changed the call to `it.geosolutions.geostore.core.security.password.SecurityUtils.toChars` to use the new `toChars` method.
3. Changed the call to `it.geosolutions.geostore.core.security.password.SecurityUtils.scramble` to use a new `scramble` method that operates on `byte[]`.
4. Added a new `scramble` method that scrambles a `char[]` by XORing each character with `0xFF`.
5. Casted `stringEncrypter` to `org.jasypt.encryption.pbe.StandardPBEStringEncryptor` to access the `setPasswordCharArray` method.

The added `toChars`, `scramble` and `scramble` methods can be added at the end of the class after the `createStringEncoder` method.