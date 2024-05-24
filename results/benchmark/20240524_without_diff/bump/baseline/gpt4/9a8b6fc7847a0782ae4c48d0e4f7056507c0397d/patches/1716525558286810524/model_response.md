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

		PBEPasswordEncoder encoder = new PBEPasswordEncoder();
		encoder.setPbeStringEncryptor(stringEncrypter);

		return new PasswordEncoder() {
			@Override
			public String encode(CharSequence rawPassword) {
				return encoder.encodePassword(rawPassword.toString(), null);
			}

			@Override
			public boolean matches(CharSequence rawPassword, String encodedPassword) {
				return encoder.isPasswordValid(encodedPassword, rawPassword.toString(), null);
			}
		};
	} finally {
		scramble(password);
		scramble(chars);
	}
}
```