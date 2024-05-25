Here's a patch that you can apply to the code in order to fix the error:

```java
import org.cactoos.text.TextEnvelope;
import org.cactoos.text.Joined;

// ...

@Override
public TextEnvelope<Double> one(String wallet) {
  Double sum = 0.0;
  for (String id : ids(wallet)) {
    sum += balance(id);
  }
  return new Joined<>("", asDoubleList(sum));
}
```

In this patch, I replaced the usage of `JoinedText` with `Joined`, which is an added library method identified with `++`. The `Joined` class can be found in the same package as `JoinedText`. Also, I replaced the `TextEnvelope` type parameter from `String` to `Double`, and updated the `asDoubleList` method accordingly.