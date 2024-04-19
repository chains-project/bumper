```
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
			scramble(password);
			scramble(chars);
		}
	}
```

Replace the line:
```
stringEncrypter.setAlgorithm(getAlgorithm());
```
with:
```
stringEncrypter.setAlgorithm(getAlgorithm() != null ? getAlgorithm() : "PBEWithMD5AndDES");
```
The error was caused by the fact that the `getAlgorithm()` method was returning `null`, which was causing the `setAlgorithm()` method to fail. The proposed patch checks if `getAlgorithm()` returns `null`, and if so, it sets the algorithm to "PBEWithMD5AndDES" instead. This should fix the error and allow the code to compile correctly.