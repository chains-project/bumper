```java
protected PasswordEncoder createStringEncoder() {
    return new PasswordEncoder() {
        @Override
        public String encode(CharSequence rawPassword) {
            StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
            return passwordEncryptor.encryptPassword(rawPassword.toString());
        }

        @Override
        public boolean matches(CharSequence rawPassword, String encodedPassword) {
            StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
            return passwordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
        }
    };
}
```