```java
  protected PasswordEncoder createStringEncoder() {
		byte[] password = lookupPasswordFromKeyStore();

		char[] chars = toChars(password);
		try {
			StandardPBEStringEncryptor stringEncrypter = new StandardPBEStringEncryptor();
			stringEncrypter.setPasswordCharArray(chars);

			if (getProviderName() != null && !getProviderName().isEmpty()) {
				stringEncrypter.setProviderName(getProviderName());
			}
			stringEncrypter.setAlgorithm(getAlgorithm());

			PBEPasswordEncoder encoder = new PBEPasswordEncoder();
			encoder.setStringEncryptor(stringEncrypter);

			return encoder;
		} finally {
			scramble(password);
			scramble(chars);
		}
	}
```