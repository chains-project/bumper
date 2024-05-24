Here's the proposed patch:
```java
import org.cactoos.scalar.LengthOf;

// ...

public double taxBeneficiaries(String... beneficiaries) {
  double sum = 0;
  for (String beneficiary : beneficiaries) {
    sum += new LengthOf<>(beneficiary).longValue();
  }
  return sum;
}
```
This patch replaces the usage of `org.cactoos.iterable.LengthOf` with `org.cactoos.scalar.LengthOf`, which is available in the new library version. The `longValue()` method is used to get the length as a `long` and then it's implicitly cast to `double`.