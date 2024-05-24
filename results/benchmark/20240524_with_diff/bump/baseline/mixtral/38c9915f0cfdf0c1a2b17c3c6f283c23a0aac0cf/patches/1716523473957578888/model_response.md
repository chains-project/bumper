Here is the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

@Override
public Iterable<TaxBeneficiary> beneficiaries() throws IOException {
  return new IterableOf<>(
    new Mapped<>(
      beneficiary -> new TaxBeneficiary(
        beneficiary.id(),
        new LengthOf(beneficiary.payments())
      ),
      this.beneficiaries()
    )
  );
}
```
In this patch, we have imported the new `LengthOf` class from the `org.cactoos.scalar` package instead of the old `org.cactoos.iterable` package. The `LengthOf` class in the new package takes an `Iterable` as its constructor argument, which is what we need for our code to work.

I have also updated the `Mapped` function to use the new `LengthOf` constructor that takes an `Iterable`.

Note that the `IterableOf` and `TaxBeneficiary` classes are not shown in the code snippet you provided, so I assumed they are unchanged in the new library version. If that's not the case, you may need to adjust the code accordingly.