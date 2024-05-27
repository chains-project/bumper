Here's a fixed version of the `createStringEncoder` method that uses the new `PasswordEncoder` class from the updated library:

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

* Replace `PBEPasswordEncoder` with `PasswordEncoder` for the `encoder` variable.
* Remove the `setAlgorithm` call from `encoder`, since it's not available in the new `PasswordEncoder` class.
* Change the import statement for `PasswordEncoder` to use the new class in the updated library.

Note that I did not remove the `@Override` annotation, since the method signature has not changed.