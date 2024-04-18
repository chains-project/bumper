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
			encoder.setAlgorithm(getAlgorithm());
			encoder.setIterations(getIterations());
			encoder.setSalt(getSalt());
			encoder.setSecretKeyFactory(new PBEKeySpec(chars, getSalt(), getIterations(), getKeyLength()));

			return encoder;
		} finally {
			scramble(password);
			scramble(chars);
		}
	}
```