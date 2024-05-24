Here's the proposed patch:

```java
import org.cactoos.Scalar;
import org.cactoos.scalar.ScalarEnvelope;

// ...

Scalar<Bytes> bytes = ...; // initialize your Bytes scalar
Scalar<Double> amount = ...; // initialize your Double scalar

// Use ScalarEnvelope to ensure the scalar is not null
UncheckedScalar<Bytes> uncheckedBytes = new ScalarEnvelope<>(bytes);

// Use the new UncheckedBytes constructor
UncheckedBytes checkedBytes = new UncheckedBytes(uncheckedBytes);

// Use the new NumberOfScalars constructor
NumberOfScalars numberOfScalars = new NumberOfScalars(checkedBytes, amount);

// Use the new methods added to NumberOfScalars
double doubleValue = numberOfScalars.doubleValue();

// ...
```

This patch introduces two new classes, `ScalarEnvelope` and `NumberOfScalars`, which replace the usage of the removed `UncheckedScalar` class. The `ScalarEnvelope` class ensures that the scalar value is not null, while the `NumberOfScalars` class calculates the number of scalars based on the given scalars and provides methods to retrieve the result as different numeric types.