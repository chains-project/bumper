```java
@Override
    protected PasswordEncoder createStringEncoder() {
        return new PasswordEncoder() {
            @Override
            public String encodePassword(String rawPassword, Object salt) {
                StrongPasswordEncryptor encryptor = new StrongPasswordEncryptor();
                return encryptor.encryptPassword(rawPassword);
            }

            @Override
            public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
                StrongPasswordEncryptor encryptor = new StrongPasswordEncryptor();
                return encryptor.checkPassword(rawPassword, encodedPassword);
            }
        };
    }
```