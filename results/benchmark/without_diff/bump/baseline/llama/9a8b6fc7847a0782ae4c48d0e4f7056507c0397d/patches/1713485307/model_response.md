```
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new StrongPasswordEncryptor() {
        @Override
            protected void encryptPassword(char[] password, String algorithm, int iterationCount) {
                // Remove this line to fix the error
                //super.encryptPassword(password, algorithm, iterationCount);
                // Add this line to fix the error
                PasswordEncoder.super.encryptPassword(password, algorithm, iterationCount);
            }
        });
        return encoder;
    }
```