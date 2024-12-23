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

		return new PasswordEncoder() {
			@Override
			public String encode(CharSequence rawPassword) {
				return stringEncrypter.encryptString(rawPassword.toString());
			}

			@Override
			public boolean matches(CharSequence rawPassword, String encodedPassword) {
				return stringEncrypter.decryptString(encodedPassword).equals(rawPassword.toString());
			}
		};
	} finally {
		scramble(password);
		scramble(chars);
	}
}
```