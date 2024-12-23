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

		return encoder;
	} finally {
		Arrays.fill(password, (byte) 0);
		Arrays.fill(chars, '\0');
	}
}
```