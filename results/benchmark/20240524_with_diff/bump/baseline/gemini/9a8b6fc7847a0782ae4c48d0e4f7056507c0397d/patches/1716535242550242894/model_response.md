```java
@Override
	protected PasswordEncoder createStringEncoder() {
		StrongPasswordEncryptor encryptor = new StrongPasswordEncryptor();
		return new PasswordEncoder() {
			@Override
			public String encodePassword(String rawPassword, Object salt) {
				return encryptor.encryptPassword(rawPassword);
			}

			@Override
			public boolean isPasswordValid(String encPassword, String rawPassword, Object salt) {
				return encryptor.checkPassword(rawPassword, encPassword);
			}
		};
	}
```