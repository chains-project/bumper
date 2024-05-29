Here's a fixed version of the code that replaces the failing import statement with a working one:
```java
import org.jasypt.util.text.BasicTextEncryptor;
```
Note that this version uses the `BasicTextEncryptor` class from the `org.jasypt.util.text` package instead of the `PBEPasswordEncoder` class from the `org.jasypt.spring.security` package. This should fix the error message you provided.

However, it's important to note that this change may not be sufficient to fully fix the issue, depending on how the `PBEPasswordEncoder` class is used in the rest of the code. If the code relies on specific features or behavior of `PBEPasswordEncoder` that are not available in `BasicTextEncryptor`, additional changes may be necessary.