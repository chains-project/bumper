```java
@Override
	protected PasswordEncoder createStringEncoder() {
		byte[] password = lookupPasswordFromKeyStore();

		char[] chars = toChars(password);
		try {
			StandardPBEByteEncryptor byteEncrypter = new StandardPBEByteEncryptor();
			byteEncrypter.setPasswordCharArray(chars);

			if (getProviderName() != null && !getProviderName().isEmpty()) {
				byteEncrypter.setProviderName(getProviderName());
			}
			byteEncrypter.setAlgorithm(getAlgorithm());

			PBEPasswordEncoder encoder = new PBEPasswordEncoder();
			encoder.setPbeByteEncryptor(byteEncrypter);

			return encoder;
		} finally {
			scramble(password);
			scramble(chars);
		}
	}
```
I have replaced the `StandardPBEStringEncryptor` with `StandardPBEByteEncryptor` and `setPbeStringEncryptor` with `setPbeByteEncryptor` because the error message indicates that the symbol `StandardPBEStringEncryptor` and `setPbeStringEncryptor` cannot be found. The `StandardPBEByteEncryptor` and `setPbeByteEncryptor` are the alternative methods that can be used in this context.