Sure, here's the fixed version of the failing client code:
```java
import org.cactoos.scalar.LengthOf;

// ...

public class TaxBeneficiaries implements Beneficiaries {
    // ...

    @Override
    public int length() {
        return new LengthOf<>(beneficiaries).intValue();
    }

    // ...
}
```
In this patch, I changed the import statement to use `org.cactoos.scalar.LengthOf` instead of `org.cactoos.iterable.LengthOf`, since the latter has been removed in the new library version. The `LengthOf` class in `org.cactoos.scalar` package can take an `Iterable` as its constructor argument, so it can still be used to calculate the length of the `beneficiaries` field.

Note that the `LengthOf` class now returns a `Scalar` instead of an `Iterable`, so we need to call the `intValue()` method to get the length as an `int`.