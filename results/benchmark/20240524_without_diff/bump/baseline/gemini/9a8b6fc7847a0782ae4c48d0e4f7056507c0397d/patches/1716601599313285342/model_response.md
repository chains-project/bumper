```java
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
		encoder.setAlgorithm(getAlgorithm());
		encoder.setProviderName(getProviderName());
		encoder.setSalt(getSalt());

		return encoder;
	} finally {
		scramble(password);
		scramble(chars);
	}
}
```