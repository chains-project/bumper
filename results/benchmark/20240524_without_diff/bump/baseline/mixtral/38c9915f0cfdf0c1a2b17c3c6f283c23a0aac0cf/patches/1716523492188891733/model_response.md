Sure, here is a possible patch for the failing code:
```java
import org.cactoos.scalar.LengthOf;

// ...

@Override
public Beneficiary tax(Beneficiary beneficiary) throws IOException {
  long length = new LengthOf(new IterableOf(new BeneficiaryToBytes(beneficiary))).longValue();
  // ...
}
```
In this patch, I replaced the import statement to use the new `LengthOf` class from the `org.cactoos.scalar` package. I also changed the instantiation of `LengthOf` to use the new constructor that takes an `Iterable` as an argument. Finally, I called the `longValue()` method to get the length as a `long` value.

Note that this patch assumes that the `BeneficiaryToBytes` class implements the `Iterable` interface. If that's not the case, you may need to modify the code accordingly.