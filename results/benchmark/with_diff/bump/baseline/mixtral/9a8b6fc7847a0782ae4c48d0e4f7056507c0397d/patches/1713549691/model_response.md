Here's the fixed `passwordEncoder()` method:

```java
@Bean
public PasswordEncoder passwordEncoder() {
    PasswordEncryptor passwordEncryptor = new PasswordEncryptor();
    TextEncryptor textEncryptor = new TextEncryptor();

    passwordEncryptor.setAlgorithm("PBEWithMD5AndTripleDES");
    textEncryptor.setAlgorithm("PBEWithMD5AndTripleDES");

    return new PasswordEncoder() {
        @Override
        public String encode(CharSequence rawPassword) {
            return passwordEncryptor.encryptPassword(rawPassword.toString());
        }

        @Override
        public boolean matches(CharSequence rawPassword, String encodedPassword) {
            return passwordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
        }
    };
}
```

Changes:

1. Replaced the deprecated constructor for `PasswordEncoder` with the new constructor for `PasswordEncryptor`.
2. Removed the unused `textEncryptor` parameter from the method.
3. Added the `setAlgorithm()` method to initialize the `PasswordEncryptor` and `TextEncryptor` instances with the required algorithm, as the default constructor no longer initializes the algorithm.

Note: I assumed that the algorithm "PBEWithMD5AndTripleDES" is still suitable for your use case. If not, you can change it accordingly.