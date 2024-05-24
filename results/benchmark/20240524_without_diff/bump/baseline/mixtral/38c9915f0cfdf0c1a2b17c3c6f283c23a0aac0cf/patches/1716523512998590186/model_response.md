Sure, I can help you fix the error in your code. The issue is caused by the fact that the `LengthOf` class has been moved from the `org.cactoos.iterable` package to the `org.cactoos.scalar` package.

Here is the fixed version of the code:

```java
import org.cactoos.scalar.LengthOf;

// ...

@Override
public String taxBeneficiaries() throws IOException {
  return new LengthOf(beneficiaries()).toString();
}
```

In this version, I have imported the `LengthOf` class from the `org.cactoos.scalar` package instead of the `org.cactoos.iterable` package. I have also updated the argument of the `LengthOf` constructor to be an `Iterable` instead of an `Iterator`. This is because the `LengthOf` class now expects an `Iterable` as its argument, rather than an `Iterator`.

I hope this helps! Let me know if you have any other questions.