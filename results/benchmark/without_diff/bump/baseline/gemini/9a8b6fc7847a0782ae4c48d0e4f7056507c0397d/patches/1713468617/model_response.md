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
			encoder.setSalt(getSalt());
			encoder.setIterationCount(getIterationCount());
			encoder.setDigestAlgorithm(getDigestAlgorithm());
			encoder.setKeyLength(getKeyLength());
			encoder.setEncodingStrength(getEncodingStrength());
			encoder.setSaltSource(getSaltSource());
			encoder.setRandom(getRandom());
			encoder.setPbeStringEncryptor(stringEncrypter);

			return encoder;
		} finally {
			scramble(password);
			scramble(chars);
		}
	}
```