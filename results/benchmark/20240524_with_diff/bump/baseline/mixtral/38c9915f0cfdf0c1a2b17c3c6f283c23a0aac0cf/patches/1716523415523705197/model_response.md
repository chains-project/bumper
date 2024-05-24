Here's the proposed patch for the failing client code:
```java
import org.cactoos.scalar.LengthOf;

// ...

public class TaxBeneficiaries {
	// ...

	@Override
	public int length() {
		return new LengthOf<>(beneficiaries).intValue();
	}
}
```
The patch imports the new `LengthOf` class from `org.cactoos.scalar` and uses it in the `length()` method.