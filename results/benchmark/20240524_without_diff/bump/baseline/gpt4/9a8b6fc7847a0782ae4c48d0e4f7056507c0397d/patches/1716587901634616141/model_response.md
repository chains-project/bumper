```java
@Override
protected PasswordEncoder createStringEncoder() {
	byte[] password = lookupPasswordFromKeyStore();

	char[] chars = toChars(password);
	try {
		stringEncrypter = new StandardPBEStringEncryptor();
		stringEncrypter.setPassword(new String(chars));

		if (getProviderName() != null && !getProviderName().isEmpty()) {
			stringEncrypter.setProviderName(getProviderName());
		}
		stringEncrypter.setAlgorithm(getAlgorithm());

		PBEPasswordEncoder encoder = new PBEPasswordEncoder();
		encoder.setPbeStringEncryptor(stringEncrypter);

		return encoder;
	} finally {
		scramble(password);
		scramble(chars);
	}
}
```